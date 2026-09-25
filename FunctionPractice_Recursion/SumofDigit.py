# WAF to find the sum of all digits of a number using recursion.
n = int(input("Enter a Number to find the digit Sum: "))
def digitSum(n):
    if(n < 10):
        return n
    else:
      return (n % 10) + digitSum(n // 10) 

print(digitSum(n))
     