'''sum = 0
for x in (2,4,6,8):
    m = x
    while (m > 4):
        sum = sum + x
        m = m - 1'''

total_sum = 0
for x in (2, 4, 6, 8):  # Correcting the range usage
    m = x
    while m > 4:
        total_sum += x  # Using a different variable name to avoid conflicts
        m -= 1

print("Total sum =", total_sum)
