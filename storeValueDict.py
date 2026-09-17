# WPA to marks of 3 subject from the user and store them in a dictionary .start with an empty dict and add one by one use subject name as a key and marks as value
dict = {}
dict.update({"sub1" :input("Enter 1st subject marks:")})
dict.update({"sub2" :input("Enter 2nd subject marks:")})
dict.update({"sub3" :input("Enter 3rd subject marks:")})
print(dict)