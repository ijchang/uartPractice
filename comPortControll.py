import serial

ser = serial.Serial('/dev/ttyS4', baudrate=115200) #open serial port
print(ser.name) #check which port was really used

#ser.open()
#ser.write(b'\x01\x03\x0c\x00') #write a string
while 1:
    evtHd = ser.read_until(b'\x04\x3E', 100)
    evtHdStr = evtHd.hex()
    lenEvtHdStr = len(evtHdStr)
    tmp = evtHdStr[lenEvtHdStr-4:lenEvtHdStr]
    strtmp = "043E"
    if (tmp.upper() != strtmp):#check if evtHd string does have 043E as the last two bytes
        continue

    evtLen = ser.read(1)#get the len of the data of this hci le meta event
    evtLenStr = evtLen.hex()
    #print(type(evtLenStr))
    #print(evtLenStr)
    evtData = ser.read(int(evtLenStr, 16)) #read the data of this le meta event
    evtAll = '043E' + evtLenStr + evtData.hex() #compose the full hci event
    print(evtAll) #print the result
    stop = input('please enter 1 to stop')
    if int(stop) == 1:
        break
ser.close()
