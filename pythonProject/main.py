import usb.core
import usb.backend.libusb1

VID = 0x2B7F
PID = 0x0001

device = usb.core.find(idVendor=VID, idProduct=PID)



