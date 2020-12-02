import serial

def ExtAdvProc(evtLenStr):
    evtData = ser.read(int(evtLenStr, 16)-1) #read the data of this le meta event
    numOfRpts = hex(evtData[0])
    evtTypes = hex(evtData[1]) + hex(evtData[2])[2:]
    addrTypes = hex(evtData[3])
    addr = hex(evtData[9]).zfill(2) + hex(evtData[8])[2:].zfill(2)+ hex(evtData[7])[2:].zfill(2) + hex(evtData[6])[2:].zfill(2) + hex(evtData[5])[2:].zfill(2) + hex(evtData[4])[2:].zfill(2)
    priPhy = hex(evtData[10])
    secPhy = hex(evtData[11])
    advSid = hex(evtData[12])
    txPwr = hex(evtData[13])
    rssi = hex(evtData[14])
    priAdvInterval = hex(evtData[15]) + hex(evtData[16])[2:0]
    dirAddrType = hex(evtData[17])
    dirAddr = hex(evtData[23]).zfill(2) + hex(evtData[22])[2:].zfill(2)+ hex(evtData[21])[2:].zfill(2) + hex(evtData[20])[2:].zfill(2) + hex(evtData[19])[2:].zfill(2) + hex(evtData[18])[2:].zfill(2)
    dataLen = hex(evtData[24])
    data = evtData[25:(25+evtData[24]-1)]
 
    print('numOfRpts = ', numOfRpts)
    print('evtTypes = ', evtTypes)
    print('addrTypes = ', addrTypes)
    print('addr = ', addr)
    print('priPhy = ', priPhy)
    print('secPhy = ', secPhy)
    print('advSid = ', advSid)
    print('txPwr = ', txPwr)
    print('rssi = ', rssi)
    print('priAdvInterval = ', priAdvInterval)
    print('dirAddrType = ', dirAddrType)
    print('dirAddr = ', dirAddr)
    print('dataLen = ', dataLen)
    print('data = ', data)

    #evtAll = '043E' + evtLenStr + evtData.hex() #compose the full hci event
    #print(evtAll) #print the result

ser = serial.Serial('/dev/ttyS4', baudrate=115200) #open serial port
print(ser.name) #check which port was really used

#ser.open()
#ser.write(b'\x01\x03\x0c\x00') #write a string
while 1:
    evtSelect = input('please select evt code: 1: cmdComplete evt; 2: le meta evt\n')
    if evtSelect == str(1):
        prefixByte = b'\x04\x0E'
        break
    elif evtSelect == str(2):
        prefixByte = b'\x04\x3E'
        break
    else:
        print("please select another evt code")
        break

while 1:
    evtHd = ser.read_until(prefixByte, 500)
    #evtHdStr = evtHd.hex()
    #lenEvtHdStr = len(evtHdStr)
    #tmp = evtHdStr[lenEvtHdStr-4:lenEvtHdStr]
    #strtmp = "043E"
    #if (tmp.upper() != strtmp):#check if evtHd string does have 043E as the last two bytes
    #    print('skip')
    #    continue
    if(prefixByte == b'\x04\x0E'):
        evtLen = ser.read(1)
        evtLenStr = evtLen.hex()
        evtLenInt = int(evtLenStr, 16)
        evtData = ser.read(evtLenInt)
        print('============== command complete event received ===========')
        print('opcode = ', hex(evtData[1]) + hex(evtData[2]))
    if(prefixByte == b'\x04\x3E'):
        evtLen = ser.read(1)#get the len of the data of this hci le meta event
        subEvtCode = ser.read(1)#get the subevent code
        print(subEvtCode)
        evtLenStr = evtLen.hex()
        subEvtCodeStr = subEvtCode.hex()
    #print(type(evtLenStr))
    #print(evtLenStr)
        if subEvtCodeStr == '0d':
            print('============= ExtAdvRpt is received ===============')
            ExtAdvProc(evtLenStr)
    
    #stop = input('please enter 1 to stop')
    #if int(stop) == 1:
    #    break
ser.close()
