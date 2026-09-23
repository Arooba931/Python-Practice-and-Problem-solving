#WPA to find first n number factorial using for loop
n = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(n,0,-1):
    factorial = factorial* i

print(factorial)
