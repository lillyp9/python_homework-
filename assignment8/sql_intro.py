import sqlite3

print("sql_intro.py is running")

with sqlite3.connect("db/magazines.db") as conn:
    print("Database created and connected successfully.")

print("Done")

#Task 2 
try:
 with sqlite3.connect("db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    
    
    #create table for publishers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE
    )
    """)
    
    #create table for maginezines
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
      title TEXT NOT NULL UNIQUE,
      publisher_id INTEGER,
      FOREIGN KEY (publisher_id) REFERENCES publishers(id)
    )
    """)
    #create table for subscribers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    );
    """)
    
    #create table for subscriptions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id  INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    )
    """)
    print("Tables created successfully.")

except Exception as e:
 print("An error occurred:", e)


#Task 3 

# ----- FUNCTIONS TO ADD RECORDS -----
#Publisher name   
def add_publisher(conn, cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,)
        )
        conn.commit()
        print(f"Publisher '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")
 
 #Magazine title and publisher id   
def add_magazine(conn, cursor, title, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id)
        )
        conn.commit()
        print(f"Magazine '{title}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Magazine '{title}' already exists or publisher is invalid .")

#Subscriber name and address
# Check for existing subscriber with SAME name and address
def add_subscriber(conn, cursor, name, address):
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address)
        )
    existing = cursor.fetchone()
    if existing:
        print(f"Subscriber '{name}' added successfully.")
        return
    try:
        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )
        conn.commit()
        print(f"Subscriber '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' could not be added.")
 
#  enforced foreign key constraints 
def add_subscription(conn, cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date)
        )
        conn.commit()
        print(f"Subscription for subscriber ID '{subscriber_id}' to magazine ID '{magazine_id}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Subscription could not be added. Check subscriber ID and magazine ID.")
        
# --- Main Program to test the functions ---
with sqlite3.connect("db/magazines.db") as conn:
    #Forgien key enforcement 
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    
    # Test adding publishers
    add_publisher(conn, cursor, "Tech World")
    add_publisher(conn, cursor, "Health Weekly")
    add_publisher(conn, cursor, "Tech Today")  # Duplicate to test integrity
    
    # Test adding magazines
    add_magazine(conn, cursor, "AI Innovations", 1)
    add_magazine(conn, cursor, "Wellness Tips", 2)
    add_magazine(conn, cursor, "Space Today", 3)  # Duplicate to test integrity
    # last number us publisher id
    
    # Test adding subscribers
    add_subscriber(conn, cursor, "Alice Smith", "123 Maple St")
    add_subscriber(conn, cursor, "Bob Johnson", "456 Oak St")
    add_subscriber(conn, cursor, "Alice Smith", "123 Maple St")  # Duplicate to test integrity    
   
    # Test adding subscriptions
    add_subscription(conn, cursor, 1, 1, "2024-12-31")
    add_subscription(conn, cursor, 2, 2, "2024-11-30")
    add_subscription(conn, cursor, 3, 1, "2024-10-31")  # Invalid subscriber ID to test integrity
    
#Notes
#SQLite assigns IDs starting 1

#Task 4 
with sqlite3.connect("db/magazines.db") as conn:
    cursor = conn.cursor()
    
#Queries to retrieve information from subscribers table 
    cursor.execute("SELECT * FROM subscribers")
    subscribers = cursor.fetchall()
    print("Subscribers:")
    for subscriber in subscribers:
        print(subscriber)
    


#Queries to retrieve all magazines sorted by name 
    cursor.execute("SELECT * FROM magazines ORDER BY title")
    magazines = cursor.fetchall()
    print("Magazines:")
    for magazine in magazines:
        print(magazine)

#Queries to find magazines for certain publisher , one publisher created . That requires a JOIN 
    publisher_name = "Health Weekly"
    cursor.execute("""
    SELECT magazines.title 
    FROM magazines 
    JOIN publishers ON magazines. publisher_id = publishers.id
    WHERE publishers.name = ?
    """, (publisher_name,))
    magazines_by_publisher = cursor.fetchall()
    print(f"Magazines published by '{publisher_name}':")
    for magazine in magazines_by_publisher:
        print(magazine)
        
conn.commit()
conn.close()

