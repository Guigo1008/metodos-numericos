x = 4
normalized_x = x # y
counter = 0 # m

while normalized_x >= 1:
    normalized_x /= 2
    counter += 1

for i in range(counter):
    normalized_x = normalized_x * 2

print(normalized_x)