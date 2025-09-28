import string

# Example text
my_str = "Hello!!!, he said ---and went."

# Remove punctuation using string.punctuation
no_punct = "".join(char for char in my_str if char not in string.punctuation)

print(no_punct)
