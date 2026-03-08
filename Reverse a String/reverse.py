# How do you reverse a string without creating another variable?


text= list(input("Enter a string"))
left=0
right =len(text) -1
while left<right:
    text[left],text[right]=text[right],text[left]
    left +=1
    right-=1
print(" ".join(text))