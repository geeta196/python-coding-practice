numbers =[10,20,30,40,50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
        
print("Largest number in the list is:", largest)
