#Text Cleaning & Formatting tool:

text = input("Enter the Text: ")

print("The length of your text is: " , len(text))

words = text.split()
count = len(words)
print("The number of words in text is: ", count)

print("Enter the type of format you want: ")
print("A - Uppercase")
print("B - Lowercase")
print("C - Title Case")

choice = input("Enter A, B , C: ")

if choice == 'A':
    print("Uppercase: ", text.upper())
elif choice == 'B':
    print("Lowercase: ", text.lower())
elif choice == 'C':
    print("Title case: " , text.title())
else:
    print("Invalid choice")
