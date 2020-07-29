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

NOPAGES = 50

HOST = "localhost"

USER = "username"

PSW="password"

TABLE1 = '''CREATE TABLE IF NOT EXISTS laptop (
                            Laptop_id INT AUTO_INCREMENT PRIMARY KEY,
                            Product_Name varchar(767) UNIQUE,
                            Price INT,
                            Rating REAL,
                            Reviews INT,
                            Link TEXT, 
                            Created_At TEXT,
                            Last_Update TEXT,
                            Valid INT
                            )'''
TABLE2 = '''CREATE TABLE IF NOT EXISTS laptop_features (
                            Laptop_id INT PRIMARY KEY,
                            Product_Name varchar(767) UNIQUE,
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
                            Date_First_Available TEXT,
                            Created_At TEXT,
                            Valid INT
                            )'''

TABLE3 = '''CREATE TABLE IF NOT EXISTS reviews (
                            Review_id INT AUTO_INCREMENT PRIMARY KEY,
                            Laptop_id INT,
                            User_id VARCHAR(30),
                            Username VARCHAR(30),
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

TABLE4 = '''CREATE TABLE IF NOT EXISTS profile ( 
                            User_id VARCHAR(30) PRIMARY KEY ,
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

KEY_TABLE3="""ALTER TABLE reviews
              ADD FOREIGN KEY (User_id) 
              REFERENCES profile (User_id)"""

