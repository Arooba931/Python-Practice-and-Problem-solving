# WPA to check if a list contains a palindrome of element,(hint:use copy()method)
list = [1,2,3]
listCopy = list.copy()

listCopy.reverse()
# print(f"After reversed {listCopy}")
if(listCopy == list):
    print("palindrome")
else:
    print("not a palindrome")