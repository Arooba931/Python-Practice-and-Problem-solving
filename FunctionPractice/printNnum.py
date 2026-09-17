# WAF to print numbers from n to 1 using recursion.
n = int(input("Enter a Number to find the Sum of N number: "))
def Natural_Sum(n):
    if (n == 0):
     pass 
    else:
       
       print(n )
       Natural_Sum(n-1)

Natural_Sum(n)
