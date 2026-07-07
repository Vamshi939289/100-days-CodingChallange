# 1. Count Total Vowels
# Task: Write a function that takes a string 
# and returns the total number of vowels (a, e, i, o, u).
# Example Input:
# programming

# def countVowels(str1):
#     count = 0
#     for char in str1:
#         if char in "aeiouAEIOU":
#             count+=1
#     return count
# print("Total Vowels:",countVowels('programming'))


# 2. Count Total Consonants
# Task: Write a function that takes a string and 
# returns the total number of consonants.
# Example Input:
# python
# Example Output:
# Total Consonants = 5
# def consonants(str1):
#     count = 0
#     for char in str1:
#         if char not in "AEIOUaeiou":
#             count+=1
#     return count
# print("Total Consonants:",consonants('python'))



# 3. Reverse a String
# Task: Write a function that takes a string and 
# returns the string in reverse order.
# Example Input:
# computer
# Example Output:
# Reversed String = retupmoc

# def reverseofstring(str1):
#     rev = " "
#     for char in str1:
#         rev = char+rev
#     return rev
# print("Reversed String:",reverseofstring('computer'))


# 4. Count Uppercase and Lowercase Letters
# Task: Write a function that takes a string and returns the number of uppercase and lowercase letters.
# Example Input:
# PyThOn
# Example Output:
# Uppercase = 3
# Lowercase = 3
# def upperlowercounter(str1):
#     upper_count = 0
#     lower_count = 0
#     for char in str1:
#         if 'A'<=char<='Z':
#             upper_count+=1
#         else:
#             lower_count+=1
#     print("UpperCase Count:",upper_count)
#     print("lowerCase Count:",lower_count)
#     return upper_count,lower_count
# upperlowercounter('PyThoN')


# 5. Count Digits in a String
# Task: Write a function that takes a string and returns how many digits are present.
# Example Input:
# abc12345xy
# Example Output:
# Digits = 5

# def countdigits(str1):
#     count = 0
#     for char in str1:
#         if '0'<=char<='9':
#             count+=1
#     return count
# print("The Total Digits:",countdigits('abc12345yu'))

# 6. Check Palindrome
# Task: Write a function that takes a string and checks whether it is a palindrome.
# Example Input:
# madam
# Example Output:
# # Palindrome
# def palindrome(str1):
#     rev=""
#     for char in str1:
#         rev = char + rev
#     if rev == str1:
#         print("palidrome")
#     else:
#         print("Not a palindrome")
#     return rev
# palindrome('madam')

# 7. Count Occurrences of a Character
# Task: Write a function that takes a string and a character and returns how many times that
# character appears.
# Example Input:
# banana
# a
# Example Output:
# Occurrences = 3

# def occurance(str1,char1):
#     count = 0
#     for char in str1:
#         if char == char1:
#             count+=1
#     return count
# print("Occurances:",occurance('banana','a'))


# 8. Find the Longest Word
# Task: Write a function that takes a sentence and returns the longest word.
# Example Input:
# Python is an amazing language
# Example Output:
# Longest Word = language


# def longestword(sen):
#     longest=""
#     for char in sen.split():
#         if len(char)>len(longest):
#             longest=char
#     print(longest)
# longestword('python is a amazing language')

# 9. Remove All Spaces
# Task: Write a function that takes a sentence and returns the same sentence after removing all
# spaces.
# Example Input:
# Data Science is fun
# Example Output:
# DataScienceisfun

# def removespace(sen):
#     sp=""
#     for char in sen:
#         if char!=" ":
#             sp=sp+char
#     return sp
# print(removespace('Data Science is fun'))


# 10. Count Words in a Sentence
# Task: Write a function that takes a sentence and returns the total number of words.
# Example Input:
# Learning Python is very interesting
# Example Output:
# Total Words = 5

def countwords(sen):
    count = 0
    for char in sen.split():
        count+=1
    return count
print("Total Words:",countwords('Learning Python is very interesting'))