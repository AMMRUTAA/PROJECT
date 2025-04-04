# First part
for i in range(1, 6):
    for j in range(1, 6):
        if i < 5:
            if j <= i:
                print(j, end="")
    print()

print()  # Adding a blank line for separation

# Second part
for i in range(1, 6):
    for j in range(1, 6):
        if i <= 5:
            if j <= i:
                print("*", end="")
    print()

# Third part
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    print()  # Print after each row is completed
    i = i - 1
