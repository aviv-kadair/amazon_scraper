"""
Create our database for the amazon project
Authors: Aviv & Serah
"""

import sqlite3
import config
from Logging import logger

DB_FILENAME = config.DB_FILENAME

con = sqlite3.connect(DB_FILENAME)
cur = con.cursor()
cur.execute('''DROP TABLE IF EXISTS laptop''')

cur.execute('''CREATE TABLE laptop (
                            Laptop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Product_Name TEXT UNIQUE,
                            Price INT,
                            Rating REAL,
                            Reviews INT,
                            Link TEXT, 
                            Created_At TEXT,
                            Last_Update TEXT,
                            Valid INT,
                            FOREIGN KEY (Laptop_id) REFERENCES laptop_features (Laptop_id) 
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                            FOREIGN KEY (Laptop_id) REFERENCES reviews (Laptop_id) 
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                            )''')

logger.info('Table laptop has been created')

cur.execute('''DROP TABLE IF EXISTS laptop_features''')
cur.execute('''CREATE TABLE laptop_features (
                            Laptop_id INT PRIMARY KEY,
                            Product_Name TEXT UNIQUE,
                            Link TEXT,
                            Screen_Size VARCHAR(30),
                            Max_Screen_Resolution VARCHAR(30), 
                            Chipset_Brand VARCHAR(30),
                            Card_Description VARCHAR(30),
                            Brand_Name VARCHAR(30), 
                            Item_Weight VARCHAR(30),
                            Operating_System VARCHAR(30), 
                            Computer_Memory_Type VARCHAR(30),
                            Batteries VARCHAR(30),
                            Created_At TEXT,
                            Valid INT
                            )''')

logger.info('Table laptop_features has been created')

cur.execute('''DROP TABLE IF EXISTS reviews''')

cur.execute('''CREATE TABLE reviews (
                            Review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Laptop_id INT,
                            Username VARCHAR(30),
                            Location TEXT,
                            Date TEXT,
                            UserRank REAL,
                            Profile_link TEXT,
                            Created_at TEXT
                            )''')

logger.info('Table reviews has been created')

cur.execute('''DROP TABLE IF EXISTS profile''')

cur.execute('''CREATE TABLE profile ( 
                            User_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Username TEXT UNIQUE,
                            Reviewer_Ranking INT,
                            Reviews INT,
                            Helpful_votes INT,
                            Created_at TEXT,
                            Last_Update,
                            Valid INT,
                            FOREIGN KEY (Username) REFERENCES reviews (Username)
                            )''')

logger.info('Table profile has been created')
