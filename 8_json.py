"""
Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
"""
import os
import json
# not able to import normally, because file starts with a digit
imported_5 = __import__('5_classes')
imported_6 = __import__('6_module_files')


def silently_create_jsons():
    file_content_news = {
        'type': 'News',
        'city': 'Prague',
        'text': 'teXt for new#10.'
    }
    file_content_ad = {
        'type': 'Ad',
        'text': 'This is ad#1',
        'expiration date': '2023-09-10'
    }
    file_content_random = {
        'type': 'Random thought',
        'text': 'It is a random sad thought :(',
        'city': 'Prague',
        'mood': 'sad'
    }
    if not os.path.exists('8_new_content_news.json'):
        json.dump(file_content_news, open('8_new_content_news.json', 'w'))
    if not os.path.exists('8_new_content_ad.json'):
        json.dump(file_content_ad, open('8_new_content_ad.json', 'w'))
    if not os.path.exists('8_new_content_random.json'):
        json.dump(file_content_random, open('8_new_content_random.json', 'w'))


class PostFromJSON:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def publish(self):
        path = os.path.join(self.filepath, self.filename)
        if os.path.exists(path):
            file_content = json.load(open(path))
            print(file_content)

            if file_content['type'] == 'News':
                text = file_content['text']
                city = file_content['city']
                item_to_publish = imported_5.News(text, city)
                item_to_publish.publish()
                os.remove(path)
            elif file_content['type'] == 'Ad':
                text = file_content['text']
                exp_date = file_content['expiration date']
                item_to_publish = imported_5.PrivateAd(text, exp_date)
                item_to_publish.publish()
                os.remove(path)
            elif file_content['type'] == 'Random thought':
                text = file_content['text']
                city = file_content['city']
                mood = file_content['mood']
                item_to_publish = imported_5.MyRandomThoughts(text, city, mood)
                item_to_publish.publish()
                os.remove(path)
            else:
                print('You JSON has invalid type')
        else:
            print('JSON file does not exist')


if __name__ == '__main__':
    print('What would you like to post?')
    user_input = ''
    while True:
        user_input = input(
            'Pick one:\n1) News\n2) Ad\n3) Random Thought\n4) Post from file\n5) Post from JSON\n[1/2/3/4/5]? ')

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
            item_to_publish = imported_6.PostFromFile(filepath, filename)
            item_to_publish.publish()
            imported_6.silently_create_file()
            break
        elif user_input == '5':
            print('You picked Post from JSON.  Please provide details')
            filepath = input('filepath: ')
            filename = input('filename: ')
            item_to_publish = PostFromJSON(filepath, filename)
            item_to_publish.publish()
            silently_create_jsons()
            break
        else:
            print('Type a number 1-5')
            continue



