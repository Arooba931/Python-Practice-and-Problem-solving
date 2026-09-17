# find Even and odd 
a = int(input("Enter a num for check either is Even or Odd: "))
def find(a):
    if(a %2 ==0):
      return("The number is Even!")
    else:
       return ("The number is odd!")

print(find(a))    