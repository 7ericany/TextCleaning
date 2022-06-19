# TextCleaning

A Python implementation for the rmgarbage R package (https://github.com/benmarwick/rmgarbage/). For each word, pass through all the checking functions to decide whether it is 'garbageable'. If true, disgard this word from the text.

Standards:
1. Length of the word, should not be over 40 characters.
2. Number of the special characters v.s. albetic letters or numerical characters.
3. Consecutive repeating characters, like "admisssion", "JIhhhsjf". Usually it's from a typo or ocr precision limit, with machine learning methods this word can be corrected. But here we're not able to detect what problem it is from. Can relax the repeating times from 3 to 4.
4. Lower case for first&last letter, and existing capital letter in the middle.
5. Four or more consecutive vowels in the string or five or more consecutive consonants in the string, it is garbage.

For now the output is a paragraph (all the empty sentences and words are removed). The precision is bad, but I will try to adjust the settings later.
