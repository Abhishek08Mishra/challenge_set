# 6. String and Dictionary Combination
#  Write a Python function that: ● Takes a string as input. ● Counts the frequency of each character in the string and stores it in a dictionary. ● Ignores spaces and considers case-insensitive comparisons.

user_input_string = input("Enter a string: ").lower()

frequency = {}

for character in user_input_string:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print(frequency)