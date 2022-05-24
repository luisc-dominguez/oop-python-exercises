#Palindrome exercise using Python

word = input("Enter a word: ")

if word == word[::-1]:
    print("Your word IS a palindrome\n")
else:
    print("Your word IS NOT a palindrome\n")