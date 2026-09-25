# WAF to print the element of a list in a single line(list is the parameter)
element = ["Arooba"]
fruit = ["Apple","Mango","Banana"]

def Single_Line(list):
   for el in list:
    print (el , end = " ")

print(Single_Line(fruit))
print(Single_Line(element))

