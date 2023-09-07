"""
Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
"""

import os
import xml.etree.ElementTree as ET
# not able to import normally, because file starts with a digit
imported_5 = __import__('5_classes')
imported_6 = __import__('6_module_files')
imported_8 = __import__('8_json')


def silently_create_xml():
    file_content = """<posts>
    <post type='News'>
        <text>text for news</text>
        <city>Prague1</city>
    </post>
    <post type='Ad'>
        <text>text for ad</text>
        <exp_date>2023-09-10</exp_date>
    </post>
    <post type='Random thought'>
        <text>text for my thought</text>
        <city>Prague1</city>
        <mood>happy</mood>
    </post>
</posts>
"""
    if not os.path.exists('9_new_content.xml'):
        xml_str = ET.fromstring(file_content)
        with open('9_new_content.xml', 'w') as xml_file:
            xml_file.write(file_content)


class PostFromXML:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def publish(self):
        path = os.path.join(self.filepath, self.filename)
        if os.path.exists(path):
            xml_entity = ET.parse(path)
            root = xml_entity.getroot()

            for i in root.iter('post'):
                if i.get('type') == 'News':
                    text = i.find('text').text
                    city = i.find('city').text
                    item_to_publish = imported_5.News(text, city)
                    item_to_publish.publish()
                elif i.get('type') == 'Ad':
                    text = i.find('text').text
                    exp_date = i.find('exp_date').text
                    item_to_publish = imported_5.PrivateAd(text, exp_date)
                    item_to_publish.publish()
                elif i.get('type') == 'Random thought':
                    text = i.find('text').text
                    city = i.find('city').text
                    mood = i.find('mood').text
                    item_to_publish = imported_5.MyRandomThoughts(text, city, mood)
                    item_to_publish.publish()
                else:
                    print('You XML has invalid value')
        else:
            print('XML file does not exist')


if __name__ == '__main__':
    print('What would you like to post?')
    user_input = ''
    while True:
        user_input = input(
            'Pick one:\n1) News\n2) Ad\n3) Random Thought\n4) Post from file\n5) Post from JSON\n6) Post from xml\n[1/2/3/4/5/6]? ')

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
            item_to_publish = imported_8.PostFromJSON(filepath, filename)
            item_to_publish.publish()
            imported_8.silently_create_jsons()
            break
        elif user_input == '6':
            print('You picked Post from XML.  Please provide details')
            filepath = input('filepath: ')
            filename = input('filename: ')
            item_to_publish = PostFromXML(filepath, filename)
            item_to_publish.publish()
            silently_create_xml()
            break
        else:
            print('Type a number 1-6')
            continue



