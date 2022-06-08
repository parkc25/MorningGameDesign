#Christan Park
#make a new file to put score name and date in
# 'r' read 
# 'a' append 
# 'w' write  
# open a file and make sure you close

import random
import os, datetime
os.system('cls')

Date = datetime.datetime.now() 
print(Date)
print(Date.strftime("%m-%d-%Y"))

score = 1820 
name = "Christan"
scrLine=str(score)+"\t "+name + "\t"+Date.strftime("%m-%d-%Y")+ "\n"

myFile = open("scre.txt", 'w') #create a file
myFile.write(scrLine) #write the scrLine in it
myFile.close() #close it, YOU MUST CLOSE IT

myFile = open("scre.txt", 'w') 
myFile.write(str(score))
myFile.write("\t"+name+"\t")
myFile.write(Date.strftime("%m/%d/%Y"))
myFile.write("\t")
myFile.close() 

myFile=open("scre.txt", 'a') 
myFile.write(scrLine)
myFile.close()

myFile = open("scre.txt", 'r')  
stuff = myFile.readlines()
stuff.sort(reverse=True)
myFile.close()
for line in stuff:
    print(line)



