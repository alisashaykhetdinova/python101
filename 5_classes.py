"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format

You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Private ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.

Each new record should be added to the end of file.
"""
from datetime import datetime


def write_to_file(output, filename='5_content_feed.txt'):
    f = open(filename, "a")
    f.write(output)
    f.close()


class News:
    def __init__(self, text, city):
        self.text = text
        self.city = city

    def publish(self):
        output = f'-----------------------------\nNews\n-----------------------------\n{self.text}\n{self.city}, {datetime.now()}\n\n'
        write_to_file(output)


class PrivateAd:
    def __init__(self, text, exp_date):
        self.text = text
        self.exp_date = exp_date

    def publish(self):
        date_format = '%Y-%m-%d'
        date_obj = datetime.strptime(self.exp_date, date_format)
        output = f'-----------------------------\nAd\n-----------------------------\n{self.text}\nActual until: {self.exp_date}, {(date_obj-datetime.now()).days} days left\n\n'
        write_to_file(output)


class MyRandomThoughts(News):
    def __init__(self, text, city, mood):
        News.__init__(self, text=text, city=city)
        self.mood = mood

    def publish(self):
        output = f'-----------------------------\nRandom {self.mood} thought\n-----------------------------\n{self.text}\n{self.city}, {datetime.now()}\n\n'
        write_to_file(output)


if __name__ == '__main__':
    print('What would you like to post?')
    user_input = ''
    while True:
        user_input = input(
            'Pick one: 1) News | 2) Ad | 3) Random Thought [1/2/3]? ')

        if user_input == '1':
            print('You picked News. Please provide details')
            text = input('Text: ')
            city = input('City: ')
            item_to_publish = News(text, city)
            item_to_publish.publish()
            break
        elif user_input == '2':
            print('You picked Ad.  Please provide details')
            text = input('Text: ')
            exp_date = input('Expiration date (YYYY-MM-DD format): ')
            item_to_publish = PrivateAd(text, exp_date)
            item_to_publish.publish()
            break
        elif user_input == '3':
            print('You picked Random Thought.  Please provide details')
            text = input('Text: ')
            city = input('City: ')
            mood = input('Mood: ')
            item_to_publish = MyRandomThoughts(text, city, mood)
            item_to_publish.publish()
            break
        else:
            print('Type a number 1-3')
            continue






