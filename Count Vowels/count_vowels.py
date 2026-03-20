text=input ("Enter a String:")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count +=1
print("Vowel count:",count)