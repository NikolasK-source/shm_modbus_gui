from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_SetValuesAddInt


class SetValues_AddInt(QtWidgets.QWidget, Ui_SetValuesAddInt):
    closed = QtCore.Signal()
    # name, register, addr, data_type, size, endian, value, emitter, endian_str, type_str
    add_cfg = QtCore.Signal(str, str, int, str, int, str, str, QtWidgets.QWidget, str, str)

    def __init__(self, num_AO: int, num_AI: int) -> None:
        super(SetValues_AddInt, self).__init__()
        self.setupUi(self)

        self.num_AO = num_AO
        self.num_AI = num_AI

        self.address.setMaximum(num_AO - 1)
        self.address_dec.setMaximum(num_AO - 1)

        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.size_1_lo.clicked.connect(lambda: self.on_size_changed(1))
        self.size_1_hi.clicked.connect(lambda: self.on_size_changed(1))
        self.size_2.clicked.connect(lambda: self.on_size_changed(2))
        self.size_4.clicked.connect(lambda: self.on_size_changed(4))
        self.size_8.clicked.connect(lambda: self.on_size_changed(8))

        self.button_add.clicked.connect(self.on_button_add)

        self.reg_AO.clicked.connect(self.on_reg_changed)
        self.reg_AI.clicked.connect(self.on_reg_changed)

    def set_addr_max(self, size):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI

        addr_max = num_regs - (size + 1) // 2
        self.address.setMaximum(addr_max)
        self.address_dec.setMaximum(addr_max)

    def on_size_changed(self, size: int):
        assert size in [1, 2, 4, 8]

        self.endian_little.setEnabled(size > 1)
        self.endian_big.setEnabled(size > 1)
        self.endian_reversed.setEnabled(size > 2)

        self.set_addr_max(size)

    def on_reg_changed(self):
        if self.size_1_lo.isChecked() or self.size_1_hi.isChecked():
            size = 1
        elif self.size_2.isChecked():
            size = 2
        elif self.size_4.isChecked():
            size = 4
        elif self.size_8.isChecked():
            size = 8
        else:
            raise RuntimeError("No size radio button checked")

        self.set_addr_max(size)

    def on_button_add(self):
        register = "AO" if self.reg_AO.isChecked() else "AI"

        register_addr = self.address.value()
        endian = ''

        if self.size_1_lo.isChecked():
            size = 8
            endian = "_lo"
        elif self.size_1_hi.isChecked():
            size = 8
            endian = "_hi"
        elif self.size_2.isChecked():
            size = 16
        elif self.size_4.isChecked():
            size = 32
        elif self.size_8.isChecked():
            size = 64
        else:
            raise RuntimeError("No size radio button checked")

        if self.type_signed.isChecked():
            data_type = 'i'
            type_str = "signed integer"
        else:
            data_type = 'u'
            type_str = "unsigned integer"

        if size > 8:
            endian += 'l' if self.endian_little.isChecked() else 'b'
            endian_str = "little" if self.endian_little.isChecked() else "big"
        else:
            endian_str = "low byte" if self.size_1_lo.isChecked() else "high byte"
        if size > 16 and self.endian_reversed.isChecked():
            endian += 'r'
            endian_str += "-swap16"

        # emit signal
        name = self.name.text()
        addr = register_addr
        value = "0"
        self.add_cfg.emit(name, register, addr, data_type, size, endian, value, self, endian_str, type_str)

        self.close()

    def closeEvent(self, event) -> None:
        super(SetValues_AddInt, self).closeEvent(event)
        self.closed.emit()
