max_number = 1000

ls = list(range(1, max_number))

# Sum up using `for loop`
total_1 = 0
for i in ls:
    if i % 3 == 0:
        total_1 += i
    elif i % 5 == 0:
        total_1 += i
    else:
        total_1 += 0

# Sum up using `lambda`
total_2 = sum(map(lambda i: i if (i % 3 == 0) or (i % 5 == 0) else 0, ls))

print('Total 1 (using `for loop`):', total_1)
print('Total 2 (using `lambda`):', total_2)