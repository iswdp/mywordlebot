import random

with open('wordlewords.txt') as fi:
    words = fi.readlines()

allwords = [i.strip() for i in words]
words = [i for i in allwords if len(i) == 5]

#------------------------------------------------------------------------------------------
#Starting suggestions: ROATE the SLING, TRAIN, CLOSE?

excludeList = []
includeList = []
certainList = [ [] ] #[ ['a',1],['c',4'] ]
notinPosition = [ [] ] #[ ['a',1],['c',4'] ]

for i in excludeList:
    words = [j for j in words if i not in j]
for i in includeList:
    words = [j for j in words if i in j]

if len(certainList[0]) > 0:
    for i in certainList:
        templist = []
        for word in words:
            if word[i[1]] == i[0]:
                templist.append(word)
        words = templist

if len(notinPosition[0]) > 0:
    for i in notinPosition:
        templist = []
        for word in words:
            if word[i[1]] != i[0]:
                templist.append(word)
        words = templist

guess = random.choice(words)
print(str(words) + '\n')
print(str(len(words)) + ' remaining possibilities.')
print('A random guess is: ' + str(guess))