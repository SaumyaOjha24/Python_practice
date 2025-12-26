"""Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant."""

word = input("Enter a letter or word: ")

if word.isalpha() and len(word)==1:
    if word in "aeiouAEIOU":
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid input")