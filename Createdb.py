import sqlite3
DB_FILENAME = 'projet.db'



con = sqlite3.connect(DB_FILENAME)
cur = con.cursor()
cur.execute('''DROP TABLE laptop''')
cur.execute('''CREATE TABLE laptop (
                            Laptop_id INT PRIMARY KEY AUTOINCREMENT,
                            Product_Name TEXT,
                            Price INT,
                            Ratings REAL,
                            Reviews INT,
                            Link TEXT,
                            FOREIGN KEY (Laptop_id) REFERENCES laptop_features (Laptop_id) 
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                            FOREIGN KEY (Laptop_id) REFERENCES reviews (Laptop_id) 
                                ON UPDATE CASCADE
                                ON DELETE CASCADE
                            )''')

cur.execute('''DROP TABLE laptop_features''')
cur.execute('''CREATE TABLE laptop_features (
                            Laptop_id INT PRIMARY KEY,
                            Screen_Size VARCHAR(30),
                            Max_Screen Resolution VARCHAR(30), 
                            Chipset_Brand VARCHAR(30),
                            Card_Description VARCHAR(30),
                            Brand_Name VARCHAR(30), 
                            Item_Weight VARCHAR(30),
                            Operating_System VARCHAR(30), 
                            Computer_Memory_Type VARCHAR(30),
                            Batteries VARCHAR(30)
                            )''')

cur.execute('''DROP TABLE reviews''')

cur.execute('''CREATE TABLE reviews (
                            Review_id INT PRIMARY KEY  AUTOINCREMENT,
                            Laptop_id INT,
                            Username VARCHAR(30),
                            Location TEXT,
                            UserRank REAL,
                            Profile_link TEXT
                            )''')

cur.execute('''DROP TABLE profiles''')

cur.execute('''CREATE TABLE profiles ( 
                            Username VARCHAR(30) PRIMARY KEY,
                            Reviewer_Ranking INT,
                            Reviews INT,
                            Helpful_votes INT,
                            FOREIGN KEY (Username) REFERENCES reviews (Username)
                            )''')
