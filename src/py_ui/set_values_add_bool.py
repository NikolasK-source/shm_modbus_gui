# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_values_add_bool.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_InspectSHMAddBool(object):
    def setupUi(self, InspectSHMAddBool):
        if not InspectSHMAddBool.objectName():
            InspectSHMAddBool.setObjectName(u"InspectSHMAddBool")
        InspectSHMAddBool.resize(320, 286)
        InspectSHMAddBool.setMinimumSize(QSize(320, 150))
        self.verticalLayout = QVBoxLayout(InspectSHMAddBool)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(InspectSHMAddBool)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 230))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 2, 1, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout.addWidget(self.widget_2, 8, 2, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.reg_DO = QRadioButton(self.widget)
        self.reg_DO.setObjectName(u"reg_DO")
        self.reg_DO.setChecked(True)

        self.verticalLayout_2.addWidget(self.reg_DO)

        self.reg_DI = QRadioButton(self.widget)
        self.reg_DI.setObjectName(u"reg_DI")

        self.verticalLayout_2.addWidget(self.reg_DI)


        self.gridLayout.addWidget(self.widget, 2, 2, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 4, 1, 3, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.address = QSpinBox(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        self.address.setDisplayIntegerBase(16)

        self.gridLayout.addWidget(self.address, 4, 2, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 0, 1, 1, 1)

        self.address_dec = QSpinBox(self.scrollAreaWidgetContents)
        self.address_dec.setObjectName(u"address_dec")

        self.gridLayout.addWidget(self.address_dec, 5, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.name = QLineEdit(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 2, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.button_add = QPushButton(InspectSHMAddBool)
        self.button_add.setObjectName(u"button_add")

        self.verticalLayout.addWidget(self.button_add)


        self.retranslateUi(InspectSHMAddBool)

        QMetaObject.connectSlotsByName(InspectSHMAddBool)
    # setupUi

    def retranslateUi(self, InspectSHMAddBool):
        InspectSHMAddBool.setWindowTitle(QCoreApplication.translate("InspectSHMAddBool", u"Add Bool", None))
        self.reg_DO.setText(QCoreApplication.translate("InspectSHMAddBool", u"DO", None))
        self.reg_DI.setText(QCoreApplication.translate("InspectSHMAddBool", u"DI", None))
        self.label.setText(QCoreApplication.translate("InspectSHMAddBool", u"Address (hex):", None))
        self.address.setPrefix(QCoreApplication.translate("InspectSHMAddBool", u"0x", None))
        self.label_3.setText(QCoreApplication.translate("InspectSHMAddBool", u"Register:", None))
        self.name.setText(QCoreApplication.translate("InspectSHMAddBool", u"Bool", None))
        self.label_4.setText(QCoreApplication.translate("InspectSHMAddBool", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("InspectSHMAddBool", u"Address (dec):", None))
        self.button_add.setText(QCoreApplication.translate("InspectSHMAddBool", u"Add", None))
    # retranslateUi

