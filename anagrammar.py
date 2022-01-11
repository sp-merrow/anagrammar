from os import system, name

anagrams = []
parts = []

clear = lambda: system('cls' if name=='nt' else 'clear')

def totalAnagram(source, check):
    if len(source) != len(check):
        return False

    for char in source:
        if char not in check:
            return False
        if source.count(char) != check.count(char):
            return False
    
    return True

def getNext(part, remaining):
    newAnagram = part.capitalize()
    for check in parts:
        if len(check) > len(remaining):
            continue
        
        isPartial = True
        for char in check:
            if char not in remaining:
                isPartial = False
                break

            if check.count(char) > remaining.count(char):
                isPartial = False
                break
        
        if isPartial:
            for char in check:
                remaining = remaining.replace(char, '', 1)

            newAnagram += check.capitalize()

    if len(remaining) == 0:
        return newAnagram
    return None


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

            if line.count(char) > sourceWord.count(char):
                partial = False
                break
        
        if partial and len(line) > 2:
            parts.append(line)
        
        if totalAnagram(sourceWord, line):
            anagrams.append(line)

for p in parts:
    remain = sourceWord
    for c in p:
        remain = remain.replace(c, '', 1)
    word = getNext(p, remain)
    
    
    if word and (word.lower() not in anagrams):
        anagrams.append(word)

#clear()
if not anagrams:
    print('No anagrams found.')
else:
    print('Anagrams found:\n')
    for i in anagrams:
        print(i)
