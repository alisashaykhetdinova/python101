"""
Create a tool which will calculate straight-line distance between different cities based on coordinates:
 1. User will provide two city names by console interface
 2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
 3. Return distance between cities in kilometers

"""
import geopy.distance
import sqlite3


class DBCityCoordinates:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_init_table(self):
        self.cursor.execute('create table if not exists city_coord (city TEXT, x_value REAL, y_value REAL)')

    def cleanup_table(self):
        self.cursor.execute('truncate table city_coord')

    def does_city_exist(self, city):
        self.cursor.execute('select count(*) from city_coord where city = ?', (city.lower(),))
        return self.cursor.fetchone()[0]

    def add_city_coordinates(self, city):
        print(f'Coordinates of {city} are unknown. Please provide coordinates.')
        while True:
            try:
                x_value = float(input('x_value = '))
                break
            except ValueError:
                print('that was not a float; try again...')

        while True:
            try:
                y_value = float(input('y_value = '))
                break
            except ValueError:
                print('that was not a float; try again...')

        self.cursor.execute('insert into city_coord(city, x_value, y_value) values (?, ?, ?)', (city.lower(), x_value, y_value))
        self.connection.commit()

    def get_city_coordinates(self, city):
        self.cursor.execute('select x_value, y_value from city_coord where city = ?', (city.lower(),))
        return self.cursor.fetchone()


def measure_distance_tool():
    db_item = DBCityCoordinates('final_task.db')
    db_item.create_init_table()

    print('This tool calculates distance between 2 cities. Enter city names.')
    city_first = input('City #1: ')
    city_second = input('City #2: ')

    if db_item.does_city_exist(city_first) == 0:
        db_item.add_city_coordinates(city_first)

    if db_item.does_city_exist(city_second) == 0:
        db_item.add_city_coordinates(city_second)

    coord_first = db_item.get_city_coordinates(city_first)
    coord_second = db_item.get_city_coordinates(city_second)

    print(f'Distance between {city_first} and {city_second} is {geopy.distance.geodesic(coord_first, coord_second).km} km')


if __name__ == '__main__':
    measure_distance_tool()
