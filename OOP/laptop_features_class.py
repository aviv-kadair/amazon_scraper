import contextlib
import sqlite3
from datetime import datetime
from configuration import config
from Logging.Logging import logger
import sys

DB_FILENAME = config.DB_FILENAME


class Features:
    def __init__(self, screen_size='', max_screen_resolution='', chipset_brand='', card_description='', brand_name='',
                 item_weight='', operating_system='', computer_memory_type='', batteries=''):
        self.screen_size = screen_size
        self.max_screen_resolution = max_screen_resolution
        self.brand = chipset_brand
        self.card_description = card_description
        self.brand_name = brand_name
        self.item_weight = item_weight
        self.operating_system = operating_system
        self.computer_memory_type = computer_memory_type
        self.batteries = batteries

        if self.screen_size != '' or self.max_screen_resolution != '' or self.brand != '' \
                or self.card_description != '' or self.brand_name != '' or self.item_weight != '' \
                or self.operating_system != '' or self.computer_memory_type != '' or self.batteries != '':
            self.valid = 1
        else:
            self.valid = 0

    def add_to_db(self, name, laptop_id, link):
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO laptop_features (Laptop_id, Product_Name, Link, Screen_Size, Max_Screen_Resolution, Chipset_Brand, Card_Description, Brand_Name, Item_Weight, Operating_System, Computer_Memory_Type, Batteries, Created_At, Valid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
                        [laptop_id, name, link, self.screen_size, self.max_screen_resolution, self.brand,
                         self.card_description, self.brand_name, self.item_weight, self.operating_system,
                         self.computer_memory_type, self.batteries, datetime.now(), self.valid])
                    con.commit()
            logger.info('Table features laptop: added -> ' + str(laptop_id))

        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when adding the features of laptop' + laptop_id)

    def update_db(self, laptop_id):
        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    query = "UPDATE laptop_features SET Screen_Size=:screensize, Max_Screen_Resolution=:maxscreen, Chipset_Brand=:chipset, Card_Description=:card, Brand_Name=:brand, Item_Weight=:weight, Operating_System=:operating, Computer_Memory_Type=:memory, Batteries=:batterie, Valid=:valid WHERE Laptop_id = :id"
                    cur.execute(query, {"screensize": self.screen_size, "maxscreen": self.max_screen_resolution,
                                        "chipset": self.brand, "card": self.card_description,
                                        "brand": self.brand_name, "weight": self.item_weight,
                                        "operating": self.operating_system, "memory": self.computer_memory_type,
                                        "batterie": self.batteries, "valid": self.valid, "id": laptop_id})
                    con.commit()

            logger.info('Table features laptop: updated -> ' + str(laptop_id))

        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when updating the features of laptop' + laptop_id)
            print('Write you arguments by using the laptop features table columns name ')

    @staticmethod
    def get_arg_db(name, *args):
        query = ''
        for arg in args:
            query += f'{arg} ,'

        try:
            with contextlib.closing(sqlite3.connect(DB_FILENAME)) as con:  # auto-closes
                with con:
                    cur = con.cursor()
                    get_query = "SELECT " + query[0:-1] + " FROM laptop_features WHERE Product_Name=:name"
                    cur.execute(get_query, {"name": name})
                    db_output = [item for item in cur.fetchall()[0]]
                    return db_output

        except:
            e = sys.exc_info()[0]
            logger.error(f'An error {e} occurs when selecting the features of laptop' + name)

    def get_arg(self, *args):
        output = []
        for option in args:
            if option == 'Screen_Size':
                output.append(self.screen_size)
            elif option == 'Max_Screen_Resolution':
                output.append(self.max_screen_resolution)
            elif option == 'Chipset_Brand':
                output.append(self.brand)
            elif option == 'Card_Description':
                output.append(self.card_description)
            elif option == 'Brand_Name':
                output.append(self.brand_name)
            elif option == 'Item_Weight':
                output.append(self.item_weight)
            elif option == 'Operating_System':
                output.append(self.operating_system)
            elif option == 'Computer_Memory_Type':
                output.append(self.computer_memory_type)
            elif option == 'Batteries':
                output.append(self.batteries)
            elif option == 'Valid':
                output.append(self.valid)
            else:
                print('Write you arguments by using the following 10 options:\n\
                 Screen_Size, Max_Screen_Resolution, Chipset_Brand, Card_Description, Brand_Name, Item_Weight, Operating_System, Computer_Memory_Type, Batteries, Valid')
        return output
