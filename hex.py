import serial    
def change(data):
    port = serial.Serial('/dev/ttyS0',9600)
    Cdata = hex(data)
    port.write((Cdata.encode()))

number = int(input("int number = "))
change(number)