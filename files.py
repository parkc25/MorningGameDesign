

import os, datetime
Date = datetime.datetime.now() 
score = 120 
name = "Christan"
print(Date) 
print(Date.strftime('%m  %d  %Y'))
print(score) 
myFile = open("scre.txt", 'w') 
myFile.write(str(score))
myFile.write("\t"+name+"\t")
myFile.write(Date.strftime("%m/%d/%Y"))
myFile.close() 
myFile=open("scre.txt", 'a') 
myFile = open("scre.txt", 'r')  
lines = myFile.readlines()
print(lines)
for line in myFile.readlines():
	print(line)
myFile.close()

