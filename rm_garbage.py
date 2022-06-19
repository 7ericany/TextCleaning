import re
import numpy as np
import sys

'''If a string is more than 40 characters in length, it is garbage. '''
def lengthChecker(word):
    threshold = 40
    return (len(word) == 0 or len(word) > threshold)


'''If the number of punctuation characters in a string is greater 
than the number of alphanumeric characters, it is garbage. 
Ignoring the first and last characters in a string, 
if there are two or more different punctuation characters in the string, it is garbage.
This rule was taken from rmgarbage.'''
def punc_alpha_num(word):
    count_punc = 0
    count_alpha = 0
    count_num = 0
    one_char = '0'
    for i in range(len(word)):
        # Checks whether given character is a punctuation mark
        if word[i].isalpha():
            count_alpha += 1
        elif word[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            if i != 0 and i != len(word)-1:
                if one_char == '0':
                    one_char = word[i]
                else:
                    if word[i] != one_char:
                        return True
            count_punc += 1
        elif word[i].isdigit():
            count_num += 1
        else:
            ## not recognizable
            return True
    if count_punc > count_alpha + count_num:
        return True


'''
If there are three or more identical characters in a row in a string, it is garbage. 
This rule was taken from rmgarbage, but shortened from four or more characters to three.

If the first and last characters in a string are both lowercase and 
any other character is uppercase, it is garbage.

If there are four or more consecutive vowels in the string or five 
or more consecutive consonants in the string, it is garbage.
This is a new rule we developed when we noticed that real English words with these traits are rare, 
but this property appeared often in OCR errors.'''
def repeat3Case(word):
    pattern1 = r'(.)\1\1'
    pattern2 = r'*[A-Z]*'
    pattern3 = r'[aeiou]{4}'
    pattern4 = r'[bcdfghjklmnpqrstvwxyz]{5}'
    if re.search(pattern1, word, re.IGNORECASE) != None:
        return True
    if re.search(pattern3, word, re.IGNORECASE) != None:
        return True
    if re.search(pattern4, word, re.IGNORECASE) != None:
        return True
#     if len(word) > 2:
#         if word[0].islower() and word[-1].islower() and re.search(pattern2, word[1:-1]) != None:
#             return True
    return False


def CheckGarbage(word):
    if word.isalnum():
        #         print("exit1")
        return False
    if word.isalpha():
        count = sum([1 for char in 'ajgjoier' if char in 'aeiouAEIOU'])
        if count * 8 > len(word):
            #             print("exit2")
            return True
    if lengthChecker(word) or punc_alpha_num(word):
        #         print("exit3")
        return True
    if repeat3Case(word):
        #         print("exit4")
        return True
    return False