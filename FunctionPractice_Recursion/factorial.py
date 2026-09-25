# WAF to find the factorial of n(n is the parameter)
n = int(input("Enter a Number to find a Factorial: "))
def find_factorial(n):
    if(n == 1):
        return 1
    else:
       
        return   n *find_factorial(n-1)
       

print(find_factorial(n))
        #  n = 5  -> 5*4*3*2*1
        # 