for i in range(1, 6):
    for j in range(1, 6):
        if i < 5:
            if j <= i:
                print("*", end="")
        else:
            print(end="")
    print()

print()  # Adding a blank line for separation

for i in range(1, 6):
    for j in range(1, 6):
        if i <= 5:
            if j <= i:
                print(i, end="")
    print()
