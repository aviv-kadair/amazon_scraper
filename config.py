DB_FILENAME = 'project'
PROXIES_LIST = ["128.199.109.241:8080", "113.53.230.195:3128", "125.141.200.53:80", "125.141.200.14:80",
                "128.199.200.112:138", "149.56.123.99:3128", "128.199.200.112:80", "125.141.200.39:80",
                "134.213.29.202:4444"]
HEADERS = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
LAPTOP_FEATURES = ['Screen Size', 'Max Screen Resolution', 'Chipset Brand', 'Card Description',
                   'Brand', 'Item Weight', 'Operating System', 'Computer Memory Type', 'Batteries','Date First Available']

AMAZON = 'https://www.amazon.com'

BROWSER = "chromedriver.exe"

NOPAGES = 100

HOST = "localhost"

USER = "username"

PSW="password"

TABLE1 = '''CREATE TABLE laptop (
                            Laptop_id INT AUTO_INCREMENT PRIMARY KEY,
                            Product_Name varchar(767) UNIQUE,
                            Price VARCHAR(30),
                            Rating REAL,
                            Reviews VARCHAR(100),
                            Link TEXT, 
                            Created_At TEXT,
                            Last_Update TEXT,
                            Valid INT
                            )'''
TABLE2 = '''CREATE TABLE laptop_features (
                            Laptop_id INT PRIMARY KEY,
                            Link TEXT,
                            Screen_Size VARCHAR(100),
                            Max_Screen_Resolution VARCHAR(100), 
                            Chipset_Brand VARCHAR(100),
                            Card_Description VARCHAR(100),
                            Brand_Name VARCHAR(100), 
                            Item_Weight VARCHAR(100),
                            Operating_System VARCHAR(100), 
                            Computer_Memory_Type VARCHAR(100),
                            Batteries VARCHAR(100),
                            Date_First_Available TEXT,
                            Created_At TEXT,
                            Valid INT
                            )'''

TABLE3 = '''CREATE TABLE reviews (
                            Review_id INT AUTO_INCREMENT PRIMARY KEY,
                            Laptop_id INT,
                            User_id VARCHAR(100),
                            Username VARCHAR(100),
                            Location TEXT,
                            Date TEXT,
                            UserRank REAL,
                            Profile_link TEXT,
                            Content TEXT,
                            Polarity VARCHAR(30),
                            Subjectivity VARCHAR(30), 
                            Polarity_confidence REAL,
                            Subjectivity_confidence REAL,
                            Created_at TEXT
                            )'''

TABLE4 = '''CREATE TABLE profile ( 
                            User_id VARCHAR(100) PRIMARY KEY ,
                            Reviewer_Ranking INT,
                            Reviews INT,
                            Helpful_votes INT,
                            Created_at TEXT,
                            Last_Update TEXT,
                            Valid INT
                            )'''

KEY_TABLE1="""ALTER TABLE laptop_features 
              ADD FOREIGN KEY (Laptop_id) 
              REFERENCES laptop (Laptop_id)"""

KEY_TABLE2="""ALTER TABLE reviews
              ADD FOREIGN KEY (Laptop_id) 
              REFERENCES laptop (Laptop_id)"""


QUERY_INSERT_LAPTOP = """INSERT INTO laptop (Product_Name, Price, Rating, Reviews, Link, Created_At, Last_Update, Valid) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"""
QUERY_INSERT_FEATURES = """INSERT INTO laptop_features (Laptop_id, Link, Screen_Size, Max_Screen_Resolution, Chipset_Brand, Card_Description, Brand_Name, Item_Weight, Operating_System, Computer_Memory_Type, Batteries, Date_First_Available, Created_At, Valid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
QUERY_INSERT_REVIEWS = """INSERT INTO reviews (Laptop_id, User_id, Username, Location, Date, UserRank, Profile_link, Content, Created_At) VALUES (%s, %s, %s, %s, %s, %s, %s, %s ,%s)"""
QUERY_INSERT_PROFILE = """INSERT INTO profile (User_id, Reviewer_Ranking, Reviews, Helpful_votes, Created_at,Last_Update, Valid) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
QUERY_UPDATE_LAPTOP = """UPDATE laptop SET Price=%s, Rating=%s, Reviews=%s, Last_Update=%s WHERE Product_Name = %s"""
QUERY_UPDATE_FEATURES = """UPDATE laptop_features SET Screen_Size=%s, Max_Screen_Resolution=%s, Chipset_Brand=%s, Card_Description=%s, Brand_Name=%s, Item_Weight=%s, Operating_System=%s, Computer_Memory_Type=%s, Batteries=%s, Date_First_Available=%s, Valid=%s WHERE Laptop_id =%s"""
QUERY_UPDATE_PROFILE = """UPDATE profile SET Reviewer_Ranking=%s, Reviews=%s, Helpful_votes=%s, Last_Update=%s WHERE User_id =%s"""
QUERY_GET_ARG = """SELECT Laptop_id, Link FROM laptop WHERE Product_name = %s"""
QUERY_LAPTOP_EXIST = """SELECT EXISTS (SELECT * from laptop WHERE Product_name=%s)"""
QUERY_REVIEW_EXIST = """SELECT EXISTS (SELECT * FROM reviews WHERE Username= %s AND Location=%s AND Date=%s)"""
QUERY_PROFILE_EXIST = """"SELECT COUNT(*) FROM profile WHERE User_id=%s"""
