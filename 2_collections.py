"""
1. create a list of random number of dicts (from 2 to 10)
- dict's random numbers of keys should be a letter,
- dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

2. get previously generated list of dicts and create one common dict:
- if dicts have same key, we will take max value, and rename key with dict number with max value
- if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

Each line of code should be commented with description.
"""

# import libraries
import random
import string

# create a list of random number of dicts (from 2 to 10)
# generate number of dicts using random library
random_number_dict = random.randint(2, 10)
print(f'Amount of dictionaries: {random_number_dict}\n')

# initialize main list of dictionaries
list_of_dicts = []

# go through each element of the list
for i in range(random_number_dict):
    # generate a number of items in the current dictionary; I limit it to (0,...,9)
    random_number_key = random.randint(0, 9)
    print(f'dictionary #{i + 1} has {random_number_key} items:')

    # initialize lists to story keys and values of the current dictionary
    current_dict_keys = []
    current_dict_values = []

    # start generating keys and values of the current dictionary
    while random_number_key > 0:
        # generate random lowercase letter
        random_letter = random.choice(string.ascii_lowercase)
        # skip this iteration if this letter is already used as a key in the dictionary, since keys can not be duplicated
        if random_letter in current_dict_keys:
            pass
        else:
            # if letter is not in use yet: add it to list of keys ...
            current_dict_keys.append(random_letter)
            # ... and generate random value (from 0 to 100) for the key
            current_dict_values.append(random.randint(0, 100))
            # one more item is prepared, so decrease counter
            random_number_key -= 1
    # create dictionary from 2 lists using zip method
    current_dict = dict(zip(current_dict_keys, current_dict_values))
    print(current_dict)
    # add this dictionary to the list
    list_of_dicts.append(current_dict)

print(f'list of dictionaries: {list_of_dicts}')

# creating 2 dictionaries using list_of_dicts
# max_values will contain letter as a key and maximum number from all dictionaries as a value
# max_value_sources will contain letter as a key and index of the list where this letter has maximum number
#   in case if letter is coming from single source - it will be ignored in max_value_sources
max_values = {}
max_value_sources = {}
# go through dictionaries
for dictionary in list_of_dicts:
    # go through keys (letters)
    for key in dictionary.keys():
        # if dictionary does not have a letter as a key yet - value is assumed to be 0
        max_values.setdefault(key, 0)
        # if found bigger value (number) of the key (letter) in the dictionary - replace it in max_values
        if dictionary[key] > max_values[key]:
            # if it is the first time the key gets inserted into max_values - do not add the index into max_value_sources
            if max_values[key] != 0:
                max_value_sources[key] = list_of_dicts.index(dictionary) + 1
            max_values[key] = dictionary[key]

# print(max_values)
# print(max_value_sources)

# initialize final dictionary
common_dict = {}
# go through all keys (letters)
for key in max_values.keys():
    # if letter is available in max_value_sources (meaning it was available in several dictionaries ...
    if key in max_value_sources.keys():
        # ... generate key as a concatenation
        common_dict[key + '_' + str(max_value_sources[key])] = max_values[key]
    else:
        common_dict[key] = max_values[key]
print(common_dict)
