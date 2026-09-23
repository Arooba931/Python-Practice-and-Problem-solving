# WPA to find the greater of 3 number entered by the user
a ,b ,c = map(int,input("Enter 3 number to check Greater One :").split())
if(a>b and a>c):
    print(f"{a} is a Greater Number")
elif(b>a and b>c):
    print(f"{b} is a Greater Number")
else:
    print(f"{c} is a Greater Number")