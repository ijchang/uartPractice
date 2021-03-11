#byteData = b'043@FF01200001979797671100'#the content is ascii character. So 0 here means 0x30 in ascii code
byteData = b'\x01@\x00\x01\x97\x97\x97\x40'#The leading \x sequence means the next tow characters are interpreted as hex digits for the character code;Even though you write x40 as the last byte, when you print the byteData, it will show '@' which is the same to the 2nd byte
Byte1 = byteData[0]
Byte2 = byteData[1]
Byte3 = byteData[2]
Byte4 = byteData[3]
Byte5 = byteData[4]

print('type of byteData is ', type(byteData))
print('byteData = ', byteData)
print('1st byte = ', hex(Byte1))
print('type of 1st byte = ', type(Byte1))
print('2nd byte = ', hex(Byte2))
print('3rd byte = ', hex(Byte3))
print('4th byte = ', hex(Byte4))
