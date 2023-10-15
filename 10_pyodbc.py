"""
Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
1. Different types of records require different data tables
2. New record creates new row in data table
3. Implement “no duplicate” check.

Comment: had issues setting up pyodbc and drivers on Mac M1, so used sqlite instead
"""
import sqlite3
from datetime import datetime

imported_5 = __import__('5_classes')


class DBConnection:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_init_tables(self):
        self.cursor.execute('create table if not exists news(text TEXT, city TEXT, post_time TIMESTAMP)')
        self.cursor.execute('create table if not exists ads(text TEXT, exp_date TEXT, days_left INT)')
        self.cursor.execute('create table if not exists random(text TEXT, city TEXT, mood TEXT, post_time TIMESTAMP)')

    def cleanup_tables(self):
        self.cursor.execute('truncate table news')
        self.cursor.execute('truncate table ads')
        self.cursor.execute('truncate table random')

    def add_news(self, text, city):
        self.cursor.execute('select count(*) from news where text = ? and city = ?', (text, city))
        if self.cursor.fetchone()[0] == 0:
            date_now = datetime.now()
            self.cursor.execute('insert into news(text, city, post_time) values (?, ?, ?)', (text, city, date_now))
            self.connection.commit()
        else:
            print('The news was not added to db, because it is duplicate')

    def add_ad(self, text, exp_date):
        self.cursor.execute('select count(*) from ads where text = ? and exp_date = ?', (text, exp_date))
        if self.cursor.fetchone()[0] == 0:
            date_format = '%Y-%m-%d'
            date_obj = datetime.strptime(exp_date, date_format)
            days = (date_obj-datetime.now()).days
            self.cursor.execute('insert into ads(text, exp_date, days_left) values (?, ?, ?)', (text, exp_date, days))
            self.connection.commit()
        else:
            print('The ad was not added to db, because it is duplicate')

    def add_random(self, text, city, mood):
        self.cursor.execute('select count(*) from random where text = ? and city = ? and mood= ?', (text, city, mood))
        if self.cursor.fetchone()[0] == 0:
            date_now = datetime.now()
            self.cursor.execute('insert into random(text, city, mood, post_time) values (?, ?, ?, ?)', (text, city, mood, date_now))
            self.connection.commit()
        else:
            print('The random thought was not added to db, because it is duplicate')


if __name__ == '__main__':
    db_item = DBConnection('10_database.db')
    db_item.create_init_tables()

    print('What would you like to post?')
    user_input = ''
    while True:
        user_input = input(
            'Pick one:\n1) News\n2) Ad\n3) Random Thought\n[1/2/3]? ')

        if user_input == '1':
            print('You picked News. Please provide details')
            text = input('Text: ')
            city = input('City: ')
            item_to_publish = imported_5.News(text, city)
            item_to_publish.publish()
            db_item.add_news(text, city)
            break
        elif user_input == '2':
            print('You picked Ad.  Please provide details')
            text = input('Text: ')
            exp_date = input('Expiration date (YYYY-MM-DD format): ')
            item_to_publish = imported_5.PrivateAd(text, exp_date)
            item_to_publish.publish()
            db_item.add_ad(text, exp_date)
            break
        elif user_input == '3':
            print('You picked Random Thought.  Please provide details')
            text = input('Text: ')
            city = input('City: ')
            mood = input('Mood: ')
            item_to_publish = imported_5.MyRandomThoughts(text, city, mood)
            item_to_publish.publish()
            db_item.add_random(text, city, mood)
            break
        else:
            print('Type a number 1-3')
            continue
