'''
Write a script that retrieves a list of words. For each word:
   - if is longer that 5 chars, remove the consonants
   - if is shorter(or equal) then 5 chars, remove the vowels
Order the resulting names alphabetically, and then print the concatenated string.

Use functions for each action: removing the vowels/consonants(use lambda functions), string concatenation, ordering alphabetically.
'''

LIST = ["anamaria", "are", "castele", "de", "nisip"]
VOWELS = ['a', 'e', 'i', 'o', 'u']

def parse_word(word):
    if len(word) > 5:
        onlyVowels = lambda word: [letter for letter in word if letter in VOWELS] 
        return "".join(onlyVowels(word))
    else:
        onlyConsonants = lambda word: [letter for letter in word if letter not in VOWELS] 
        return "".join(onlyConsonants(word))

def parse_words_in_list():
    newList = []
    for word in LIST:
        newList.append(parse_word(word))
    return newList

def concatenated_list(list):
    return "".join(list)

newList = parse_words_in_list()
print concatenated_list(sorted(newList))