import os
os.system("cls")


word5 = input('Your word is ')
lower = []
upper = []
for characters in word5:
    if characters.islower():
        lower.append(characters) #append moves characters to "free space" 
    else:
        upper.append(characters)

print(lower)
print(upper)
sortedWord = ''.join(lower + upper) # join() takes all items and joines them into one string
print('Sorted word is ', sortedWord)

'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','R','S','T','U','V','W','X','Y','Z'
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'