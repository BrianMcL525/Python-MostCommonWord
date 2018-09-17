"""
Program: mode.py
Author: Brian

Obtains the words from a source file and counts the occurences of each word. Output will indicatre which word occurs most frequently in the file
"""
fileName = input("")
f = open(fileName, 'r')

#Input the text, convert its words to uppercasem and add the words to a list
words = []
for line in f:
    for word in line.split():
        words.append(word.upper())
#Obtain the set of unique words and their frequencies, saving these assocations in a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        #word entered for the first time
        theDictionary[word] = 1
    else:
        #Word already seen, increment its number
        theDictionary[word] += 1
#Find the mode by obtaining the maximum value in the dictionary and determining its key
theMaximum = max(theDictionary.values())
theMinimum = min(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
    if theDictionary[key] == theMinimum:
        print("The least occured word is", key)
    