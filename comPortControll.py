import serial

def ExtAdvProc(evtLenStr):
    evtData = ser.read(int(evtLenStr, 16)) #read the data of this le meta event
    print(evtData)
    numOfRpts = hex(evtData[0])
    evtTypes = hex(evtData[1]) + hex(evtData[2])
    addrTypes = hex(evtData[3])
    addr = hex(evtData[4]) + hex(evtData[5]) + hex(evtData[6]) + hex(evtData[7]) + hex(evtData[8]) + hex(evtData[9])

    print('numOfRpts = ', numOfRpts)
    print('evtTypes = ', evtTypes)
    print('addr = ', addr)
    
    evtAll = '043E' + evtLenStr + evtData.hex() #compose the full hci event
    print(evtAll) #print the result

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
    evtCode = ser.read(1)#get the subevent code
    evtLenStr = evtLen.hex()
    evtCodeStr = evtCode.hex()
    #print(type(evtLenStr))
    #print(evtLenStr)
    if evtCodeStr == '0d':
        print('ExtAdvRpt\n')
        ExtAdvProc(evtLenStr)
    
    stop = input('please enter 1 to stop')
    if int(stop) == 1:
        break
ser.close()
