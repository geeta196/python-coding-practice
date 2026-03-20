text = input("Enter a string: ")

count = sum(1 for ch in text.lower() if ch in "aeiou")

print("Vowel count:", count)