"""
Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)
CSVs should be recreated each time new record added.
"""

import csv


def count_words(text_input):
    words_init = text_input.split()
    words = []
    for i in range(len(words_init)):
        new_word = ''.join([char for char in words_init[i] if char.isalpha()])
        if new_word:
            words.append(new_word.lower())
    # print(words)
    words_with_counts = [word + '-' + str(words.count(word)) for word in set(words)]
    # print(words_with_counts)
    return words_with_counts


def count_letters(text_input):
    chars_init = list(file_content)
    chars_cleaned = [char for char in chars_init if char.isalpha()]
    cnt = len(chars_cleaned)
    list_of_lists = [[char.lower(), chars_cleaned.count(char.upper()) + chars_cleaned.count(char.lower()), chars_cleaned.count(char.upper())] for char in chars_cleaned]
    dedup_list = []
    for i in list_of_lists:
        i.append(round(i[1]*100/cnt, 2))
        if i not in dedup_list:
            dedup_list.append(i)
    return dedup_list


with open('5_content_feed.txt', 'r') as file:
    file_content = file.read()

words_count = count_words(file_content)
letters_count = count_letters(file_content)
print(words_count)
print(letters_count)

with open('7_csv_words_count.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for record in words_count:
        print(record)
        writer.writerow([record])

with open('7_csv_letters_count.csv', 'w') as csvfile:
    headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for record in letters_count:
        print(record)
        writer.writerow({'letter': record[0], 'count_all': record[1], 'count_uppercase': record[2], 'percentage': record[3]})

