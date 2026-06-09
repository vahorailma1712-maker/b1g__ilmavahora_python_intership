word = input("enter a word:")

word_lower = word.lower()

reversed_word = word_lower[::-1]

if word_lower == reversed_word:
    print(f"'{word}' is a palindrome")

else:
    print(f"'{word}' is a not palindrom")