f=open('main.txt', 'r')
line1=f.readline()
firstline=line1[1] + line1[3] +line1[8] +line1[14]
line2=f.readline()
secondline=line2[0:3] +line2[12]
line3=f.readline()
testStr=line3.split()
splitString=testStr[1]
thirdline= line3[10] +line3[13]
line4=f.readline()
fourthline= line4[3]
testStr=line4.split()
splitString1= testStr[2]
line5=f.readline()
fifthline= line5[4:8]
line6=f.readline()
sixthline= line6[1:3]
testStr=line6.split()
splitString2=testStr[3]
line7=f.readline()
seventhline= line7[5] + line7[7] +line7[12] +line7[15]
line8=f.readline()
eigthline= line8[6:9] + line8[11:14]
line9=f.readline()
testStr=line9.split()
strangeString3=testStr[0]
ninthline= line9[10:12]
strangeString= firstline + secondline + splitString + thirdline + fourthline +splitString1 + fifthline +sixthline + splitString2 +seventhline +eigthline + strangeString3 + ninthline
print(strangeString)
import decipherHelper
testVar=decipherHelper.decipherHelper(strangeString)
File=open("decipheredMsg.txt", "w")
File.write(testVar)
