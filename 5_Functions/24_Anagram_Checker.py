from collections import Counter

def isAnagram(first, second):
    if(len(first) == len(second)):
        # first_letters = []
        # for letter in first:
        return Counter(first) == Counter(second)
    else:
        print("Strings are not the same length.")

print("Enter two strings and I'll tell you if they are anagrams.")
first = input("Enter the first string: ")
second = input("Enter the second string: ")

anagrams = "not "
anagram = isAnagram(first, second)
if (anagram == True):
    anagrams = ""

print("Strings \"%s\" and \"%s\" are %sanagrams." % (first, second, anagrams))
