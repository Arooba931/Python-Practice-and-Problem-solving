# WAF to find the sum and return the all element of the list
numbers = [10, 20, 30, 40, 50]
def sum_ele(list):
   sum = 0
   for i in list:
     sum = sum + i 
     i + 1
   return sum
   
print(sum_ele(numbers))