numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

n = int(input("Enter a number to find in the tuple: "))

i = 0

while i <= len(numbers) - 1:

    if n == numbers[i]:
        print(f"{numbers[i]} = {n}")
        break

    i += 1

else:
    print("Not found!")