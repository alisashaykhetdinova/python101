"""
Expand previous Homework 5 with additional class, which allow to provide records by text file:
1.Define your input format (one or many records) - my choice: one post per file
2.Default folder or user provided file path
3.Remove file if it was successfully processed
4.Apply case normalization functionality form Homework 3/4
"""
import os
# not able to import normally, because file starts with a digit
imported_5 = __import__('5_classes')
imported_4 = __import__('4_functions')


def silently_create_file():
    file_content = """-----------------------------
News
-----------------------------
teXt for new#10.
prague, 2023-09-25 14:21:07.042124
"""
    if not os.path.exists('6_new_content.txt'):
        file = open('6_new_content.txt', 'w')
        file.write(file_content)
        file.close()


class PostFromFile:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def publish(self):
        path = os.path.join(self.filepath, self.filename)
        if os.path.exists(path):
            source_file = open(path, 'r')
            file_content_init = source_file.read()
            file_content = ''
            for piece in file_content_init.split('\n'):
                piece_cleaned = imported_4.main_cleanup(piece)
                file_content = file_content + piece_cleaned + '\n'
            print(file_content)
            imported_5.write_to_file(file_content)
            os.remove(path)
        else:
            print('file does not exist')


if __name__ == '__main__':
    print('What would you like to post?')
    user_input = ''
    while True:
        user_input = input(
            'Pick one: 1) News | 2) Ad | 3) Random Thought | 4) Post from file [1/2/3/4]? ')

        if user_input == '1':
            print('You picked News. Please provide details')
            text = input('Text: ')
            city = input('City: ')
            item_to_publish = imported_5.News(text, city)
            item_to_publish.publish()
            break
        elif user_input == '2':
            print('You picked Ad.  Please provide details')
            text = input('Text: ')
            exp_date = input('Expiration date (YYYY-MM-DD format): ')
            item_to_publish = imported_5.PrivateAd(text, exp_date)
            item_to_publish.publish()
            break
        elif user_input == '3':
            print('You picked Random Thought.  Please provide details')
            text = input('Text: ')
            city = input('City: ')
            mood = input('Mood: ')
            item_to_publish = imported_5.MyRandomThoughts(text, city, mood)
            item_to_publish.publish()
            break
        elif user_input == '4':
            print('You picked Post from file.  Please provide details')
            filepath = input('filepath: ')
            filename = input('filename: ')
            item_to_publish = PostFromFile(filepath, filename)
            item_to_publish.publish()
            silently_create_file()
            break
        else:
            print('Type a number 1-4')
            continue




