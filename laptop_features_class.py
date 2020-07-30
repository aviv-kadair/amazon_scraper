"""
Define an OOP Features, with the corresponding attributes and functions for the features of the laptop
Authors: Serah
"""

from Createdb import connect_to_db
from datetime import datetime
import config
from Logging import logger
import sys

sys.path.append('../')
DB_FILENAME = config.DB_FILENAME


class Features:
    def __init__(self, screen_size='', max_screen_resolution='', chipset_brand='', card_description='', brand='',
                 item_weight='', operating_system='', computer_memory_type='', batteries='', date_first_available=''):
        self.screen_size = screen_size
        self.max_screen_resolution = max_screen_resolution
        self.brand = chipset_brand
        self.card_description = card_description
        self.brand_name = brand
        self.item_weight = item_weight
        self.operating_system = operating_system
        self.computer_memory_type = computer_memory_type
        self.batteries = batteries
        self.date = date_first_available

        # Check if we didn't get empty values from the scraping.
        # If valid is 0, I will retry the scraping.
        if self.screen_size != '' or self.max_screen_resolution != '' or self.brand != '' \
                or self.card_description != '' or self.brand_name != '' or self.item_weight != '' \
                or self.operating_system != '' or self.computer_memory_type != '' or self.batteries != '':
            self.valid = 1
        else:
            self.valid = 0
        self.con = connect_to_db()
        self.cur = self.con.cursor()

    def add_to_db(self, laptop_id, link):
        """Add the Features to the table laptop_features of the db"""
        try:
            query = config.QUERY_INSERT_FEATURES
            records = (laptop_id, link, self.screen_size, self.max_screen_resolution, self.brand,
                       self.card_description, self.brand_name, self.item_weight, self.operating_system,
                       self.computer_memory_type, self.batteries, self.date, datetime.now(), self.valid)
            self.cur.execute(query, records)
            self.con.commit()
            logger.info('Table features laptop: added -> ' + str(laptop_id))

        except Exception as e:
            logger.error(f'Adding Laptop features: {e}')
