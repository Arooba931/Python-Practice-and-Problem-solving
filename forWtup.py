# Search for a number in this tuple using for loop[1,4,9,16,25,36,49,64,81,100]
tup = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter a number for finding in tuple: "))

for el in tup:
    if(el == num):
        print("Found the num : {el}")
        break
    else:
        print("not found")
        

