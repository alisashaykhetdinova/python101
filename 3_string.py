initial_string = """  tHis iz your homeWork, copy these Text to variable.




  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# use count method to count spaces and tabs
count_of_whitespaces = initial_string.count(' ') + initial_string.count('\n')
print(f'Number of whitespace characters: {count_of_whitespaces}')

# bring all letters to lower case
lower_string = initial_string.lower().replace('\n', ' ')

# separate the string into separate words
split_string = lower_string.split()
# initialize list to keep the last words of each sentence
last_words = []
# go through indexes of the split_string list
for i in range(len(split_string)):
    # if previous word had a '.' in it capitalize current - it is beginning of a new sentence.
    if '.' in split_string[i - 1]:
        split_string[i] = split_string[i].capitalize()
    # replace all 'iz' words to 'is'
    if split_string[i] == 'iz':
        split_string[i] = 'is'
    # identify last words of each sentence by '.'
    if '.' in split_string[i]:
        # add last words to last_words list and remove '.'
        last_words.append(split_string[i].replace('.', ''))
# capitalize first word of last_words list
last_words[0] = last_words[0].capitalize()
# generate final_string using concats
final_string = ' '.join(split_string) + ' ' + ' '.join(last_words) + '.'

print(final_string)
