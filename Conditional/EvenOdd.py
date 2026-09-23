# WAP to check if a number entered by the user is odd or even
number = int(input("Enter a number to check to even and odd:"))
# For Even
if(number % 2 == 0):
 print(f"{number} is Even")
else:
 print(f"{number} is Odd")