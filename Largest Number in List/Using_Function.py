def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


nums = [12, 45, 2, 78, 34]

print("Largest number:", find_largest(nums))

