nums = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0

for num in nums:
    if num > 0:
        positive_num_count += 1
        print(num)

print("positive num count is: " , positive_num_count)