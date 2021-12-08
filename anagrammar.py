from os import system, name
from sys import setrecursionlimit

setrecursionlimit(10**6)

anagrams = []
parts = []

#clear = lambda: system('cls' if name=='nt' else '#clear')

def totalAnagram(source, check):
    if len(source) != len(check):
        return False

    for char in source:
        if char not in check:
            return False
        if source.count(char) != check.count(char):
            return False
    
    return True

def recursiveFind(word, remain, index):
    global parts
    isPartial = True

    try:
        check = parts[index]
    except IndexError:
        return None

    if len(check) > len(remain):
            isPartial = False
    else:
        for char in check:
            if char not in remain:
                isPartial = False
                break
            if check.count(char) > remain.count(char):
                isPartial = False
                break
    
    if isPartial:
        word += check.capitalize()
        print(word)
        for char in check.lower():
            remain = remain.replace(char, '')
    
    if remain:
        recursiveFind(word, remain, (index+1))
    else:
        return word
    

            

#clear()
print('*** Anagrammar ***')
sourceWord = input('\nEnter word to find anagrams of: ')
sourceWord = sourceWord.lower()

#clear()
print('Finding anagrams...')

with open('words.txt', 'r') as words:
    for line in words:
        line = line.replace('\n', '').lower()
        
        partial = True
        
        for char in line:
            if char not in sourceWord:
                partial = False
                break
        
        if partial:
            parts.append(line)
        
        if len(line) != len(sourceWord):
            total = False
        
        if totalAnagram(sourceWord, line):
            anagrams.append(line)

print(len(parts))

for i in range(len(parts)):
    potentialAnagram = recursiveFind('', sourceWord, i)
    if potentialAnagram and potentialAnagram not in anagrams:
        anagrams.append(potentialAnagram)

#clear()
print('Anagrams found:\n')
for i in anagrams:
    print(i)