def extract_evens_and_update(data, extra_value):
    
    evens_value = []
    for x in data:
        if x % 2 == 0:
            evens_value.append(x)
    
    # Convert the list of evens to a tuple
    evens_value = tuple(evens_value)

    # Converting the tuple to a list and adding the extra value
    updated_list = list(data)
    updated_list.append(extra_value)
    
    # Returning the tuple of evens and updated list
    return evens_value, updated_list

# Input data and additional value
input_data = (1, 2, 3, 4, 5, 6)
additional_value = 10

# Calling the function
evens_tuple, modified_list = extract_evens_and_update(input_data, additional_value)

# Printing the results
print("Tuple of evens:", evens_tuple)
print("Modified list:", modified_list)
