# Ask the user to enter a word or number
text = input("Enter a word or number: ")

# Convert the text to lowercase (to ignore case sensitivity)
text = text.lower()

# Reverse the text using slicing
reverse_text = text[::-1]

# Compare the original text with the reversed one
if text == reverse_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
