import serial
import serial.tools.list_ports


def print_ports():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print("The Serial port can't find!")
    else:
        for port in port_list:
            print(port)


def open_serial(port_name, bps):
    ser = serial.Serial(port_name, bps)
    if ser.isOpen():
        print("port \"%s\" is open at %s bps" % (port_name, bps))
    else:
        print("port \"%s\" is closed" % port_name)
    return ser


if __name__ == '__main__':
    print_ports()
    handle = open_serial("/dev/cu.usbserial-1410", 9600)
    while True:
        data = handle.readline()
        print(data)
