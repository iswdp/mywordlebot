import random

with open('wordlewords.txt') as fi:
    words = fi.readlines()

allwords = [i.strip() for i in words]
words = [i for i in allwords if len(i) == 5]

#------------------------------------------------------------------------------------------
firstGuess = random.choice(words)
print(str(len(words)) + ' remaining possibilities.')
print('First guess is: ' + str(firstGuess))

excludeList = ['f','u','g']
includeList = ['l', 'e']
firstCertains = [[]] #[['a',1],['c',4']]

for i in excludeList:
    words = [j for j in words if i not in j]
for i in includeList:
    words = [j for j in words if i in j]
for i in firstCertains:
    templist = []
    for word in words:
        if word[i[1]] == i[0]:
            templist.append(word)
    words = templist

#------------------------------------------------------------------------------------------
print(str(len(words)) + ' remaining possibilities.')
secondGuess = random.choice(words)
print('Second guess is: ' + str(secondGuess))

secondExludes = ['r','p','y']
secondIncludes = []
secondCertains = [[]]
for i in secondExludes:
    words = [j for j in words if i not in j]
for i in secondIncludes:
    words = [j for j in words if i in j]
for i in secondCertains:
    templist = []
    for word in words:
        if word[i[1]] == i[0]:
            templist.append(word)
    words = templist

#------------------------------------------------------------------------------------------
print(str(len(words)) + ' remaining possibilities.')
thirdGuess = random.choice(words)
print('Third guess is: ' + str(thirdGuess))

thirdExcludes = []
thirdIncludes = []
thirdCertains = [[]]
for i in thirdExcludes:
    words = [j for j in words if i not in j]
for i in thirdIncludes:
    words = [j for j in words if i in j]
for i in thirdCertains:
    templist = []
    for word in words:
        if word[i[1]] == i[0]:
            templist.append(word)
    words = templist

#------------------------------------------------------------------------------------------
print(str(len(words)) + ' remaining possibilities.')
fourthGuess = random.choice(words)
print('Fourth guess is: ' + str(fourthGuess))

fourthExcludes = []
fourthIncludes = []
fourthCertains = [[]]
for i in fourthExcludes:
    words = [j for j in words if i not in j]
for i in fourthIncludes:
    words = [j for j in words if i in j]
for i in fourthCertains:
    templist = []
    for word in words:
        if word[i[1]] == i[0]:
            templist.append(word)
    words = templist

#------------------------------------------------------------------------------------------
print(str(len(words)) + ' remaining possibilities.')
fifthGuess = random.choice(words)
print('Fifth guess is: ' + str(fifthGuess))


fifthExcludes = []
fifthIncludes = []
fifthCertains = [[]]

for i in fifthExcludes:
    words = [j for j in words if i not in j]

for i in fifthIncludes:
    words = [j for j in words if i in j]

for i in fifthCertains:
    templist = []
    for word in words:
        if word[i[1]] == i[0]:
            templist.append(word)
    words = templist

#------------------------------------------------------------------------------------------
print(str(len(words)) + ' remaining possibilities.')
sixthGuess = random.choice(words)
print('Sixth guess is: ' + str(sixthGuess))