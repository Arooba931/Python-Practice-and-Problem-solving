# write a recursive function to print all element in a list Hint: use list and index as parameter
list1 = [1,4,9,16,25,36,49,64,81,100]
def ele_list(list , index=0):
    if (index == len(list)):
     return list
    print(list[index])
    print(ele_list(list, index +1))
 

print(ele_list(list1))

 