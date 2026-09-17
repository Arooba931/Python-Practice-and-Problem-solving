# WAF to find the sum of first n natural numbers using recursion
n = int(input("Enter a number to find Some of Natural number: "))
def Natural_add(n):
    if n == 1:
        return 1
    else:
        return n + Natural_add(n-1)

print(Natural_add(n))    
