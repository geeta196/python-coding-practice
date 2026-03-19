nums = [10]

if len(nums) < 2:
    print("No second largest element")
else:
    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        print("No second largest element")
    else:
        print("Second Largest:", second)