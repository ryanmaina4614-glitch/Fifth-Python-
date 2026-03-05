# Dictionary Exercises

# 1. Given a list of tuples, create a dictionary
list_of_tuples = [("name", "Elie"), ("job", "Instructor")]
dict1 = dict(list_of_tuples)
print("1.", dict1)

# 2. Given two lists, create a dictionary
states_abbr = ["CA", "NJ", "RI"]
states_full = ["California", "New Jersey", "Rhode Island"]
dict2 = dict(zip(states_abbr, states_full))
print("2.", dict2)

# 3. Create a dictionary with vowels as keys and 0 as values
vowels = ['a', 'e', 'i', 'o', 'u']
dict3 = {}
for vowel in vowels:
    dict3[vowel] = 0
print("3.", dict3)