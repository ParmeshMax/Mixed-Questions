# Program to check whether the word is palindrome or not!!

word=str(input("Enter the word:"))
word=word.lower()
if word==word[::-1]:
    print("The word is Palindrome!!")
else:
    print("NO")