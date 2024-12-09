# 5. Dictionaries (Basics) 
# Write a Python program that: 
# ● Creates a dictionary with keys as numbers from 1 to 5 and values as their squares. 
# ● Prints all the keys and values. 
# ● Updates the value of key 3 to 27. 
# ● Deletes the key 5 from the dictionary.



#creaying a dicitionary with keys as numbers from 1 to 5 and their value as their squares
squares_dict = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2
}


print("Original dictionary:")
print(squares_dict) # prints all the key and their value as squares


squares_dict[3] = 27 #updating the value of key 3 to 27 as per requriment
print("\nAfter updating key 3 to 27:")
print(squares_dict) 


del squares_dict[5] #deleting the key 5 from dicitionary
print("\nAfter deleting key 5:")
print(squares_dict) #prints the squares of dicitionary after deleting the key 5