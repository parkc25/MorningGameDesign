

import os, datetime
Date = datetime.datetime.now() 
screLine = 120 
print(Date) 
print(Date.strftime('%m  %d  %Y'))
print(screLine) 
myFile = open("scre.txt", 'w') 
myFile.write(str(screLine))
myFile.close() 
myFile=open("scre.txt", 'a') 
myFile = open("scre.txt", 'r')  
lines = myFile.readlines()
print(lines)
for line in myFile.readlines():
	print(line)
myFile.close()

