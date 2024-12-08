#3. List
# Write a Python function that: 
# ● Accepts a list of integers as input. (use split method) 
# ● Returns the largest and smallest number in the list. 
# ● Removes duplicates from the list. 
# ● Sorts the list in descending order.

input_string = input("Enter numbers separated by spaces: ")

string_list = input_string.split()

int_list = []

for num in string_list:
    int_list.append(int(num))

unique_list = list(set(int_list))

unique_list.sort(reverse=True)

largest = unique_list[0]

smallest = unique_list[-1]

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number in desceding order:", unique_list)