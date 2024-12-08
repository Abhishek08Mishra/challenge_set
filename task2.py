# 2. Strings
#  Write a Python program that: ● Takes a string as input. ● Reverses the string. ● Counts the number of vowels (a, e, i, o, u) in the string. ● Converts the string to uppercase.

user_input=input("\nEnter vowels alphabet with comma(,) separated between them x= ") 

reversed_string=user_input[::-1]
print("\nyour reversed string  is ",reversed_string.split(","))

uppercase_string=user_input.upper()
print("\nyour string as uppercase is ",uppercase_string.split(","))

print("\nyour string length is ",len(user_input.split(",")))