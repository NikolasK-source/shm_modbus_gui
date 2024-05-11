APP_NAME = "shm-modbus-gui"
VERSION = "2.1.0"

NAME_REGEX = r"^(\d|[a-z]|[A-Z]|\.|:|-|_)*$"
BYTE_REGEX = (r"(([0-9])|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))((,{1,2}(([0-9])|([1-9][0-9])|(1[0-9]["
              r"0-9])|(2[0-4][0-9])|(25[0-5])))*)|(,))?$")
DEVICE_REGEX = r"^((/?\w+)+)?$"
BAUD_REGEX = r"^(0|([1-9]\d{0,8}))?$"
