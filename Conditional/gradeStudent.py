# Question 
# mark 90 -> grade A
# mark 80 -> grade B
# mark 70 -> grade C
# mark 60 -> grade D

mark = int(input("Enter a science subject student Number:"))
if(mark == 90):
    print("Grade is A")
elif(mark <= 90 and mark == 80):
 print("Grade is B")
elif(mark <= 80 and mark == 70):
  print("Grade is C")
elif(mark <= 70 and mark == 60):
        print("Grade is D")
else:
    print("Fail")
