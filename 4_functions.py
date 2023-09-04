"""
Refactor homeworks from module 2 and 3 using functional approach with decomposition.
"""
import random
import string


def generate_list_of_dicts(amount_of_dicts):
    list_of_dicts = []

    for i in range(amount_of_dicts):
        random_number_key = random.randint(0, 9)
        print(f'dictionary #{i + 1} has {random_number_key} items:')

        current_dict_keys = []
        current_dict_values = []

        while random_number_key > 0:
            random_letter = random.choice(string.ascii_lowercase)
            if random_letter in current_dict_keys:
                pass
            else:
                current_dict_keys.append(random_letter)
                current_dict_values.append(random.randint(0, 100))
                random_number_key -= 1
        current_dict = dict(zip(current_dict_keys, current_dict_values))
        print(current_dict)
        list_of_dicts.append(current_dict)
    return list_of_dicts


def generate_max_value_list(list_of_dicts):
    max_values = {}
    max_value_sources = {}
    for dictionary in list_of_dicts:
        for key in dictionary.keys():
            max_values.setdefault(key, 0)
            if dictionary[key] > max_values[key]:
                if max_values[key] != 0:
                    max_value_sources[key] = list_of_dicts.index(dictionary) + 1
                max_values[key] = dictionary[key]
    return max_values, max_value_sources


def generate_final_dict(max_values, max_value_sources):
    common_dict = {}
    for key in max_values.keys():
        if key in max_value_sources.keys():
            common_dict[key + '_' + str(max_value_sources[key])] = max_values[key]
        else:
            common_dict[key] = max_values[key]
    return common_dict


def count_of_whitespaces(str):
    return str.count(' ') + str.count('\n')


def lower_string(str):
    return str.lower().replace('\n', ' ')


def main_cleanup(string_input):
    list_param = string_input.split()
    last_words = []
    for i in range(len(list_param)):
        if '.' in list_param[i - 1]:
            list_param[i] = list_param[i].capitalize()
        if list_param[i] == 'iz':
            list_param[i] = 'is'
        if '.' in list_param[i]:
            last_words.append(list_param[i].replace('.', ''))
    # if last_words:
    #    last_words[0] = last_words[0].capitalize()
    #    return ' '.join(list_param) + ' ' + ' '.join(last_words) + '.'
    #else:
    return ' '.join(list_param)



if __name__ == "__main__":
    print('Start of task #2:')

    random_number_dict = random.randint(2, 10)
    print(f'Amount of dictionaries: {random_number_dict}\n')

    list_of_dicts = generate_list_of_dicts(random_number_dict)
    print(f'list of dictionaries: {list_of_dicts}')

    max_values, max_value_sources = generate_max_value_list(list_of_dicts)
    print(f'list of max_values: {max_values}')
    print(f'list of max_value_sources: {max_value_sources}')

    final_dict = generate_final_dict(max_values, max_value_sources)
    print(f'final dictionary: {final_dict}')

    ##############################################################################################

    print('\nStart of task #3:')
    initial_string = """  tHis iz your homeWork, copy these Text to variable.
    
    
    
    
      You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    
    
    
      it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    
    
    
    
      last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    print(f'Number of whitespace characters: {count_of_whitespaces(initial_string)}')
    lower_string = lower_string(initial_string)
    print(f'Final string is: {main_cleanup(lower_string)}')




