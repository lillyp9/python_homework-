import sqlite3
import csv

#Connect to the database
conn = sqlite3.connect("../lesson.db")
cursor = conn.cursor()
#Turn on  foreign key 
conn.execute("PRAGMA foreign_keys = 1;")
#Create Table 
#create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL   
   
)
""")

#Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT
    )
""")


#Create products table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL
)
""")


#Added order table and order_id  
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    employee_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)
""")

#Create line_items table
cursor.execute("""
CREATE TABLE IF NOT EXISTS line_items (
    line_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
)
""")

conn.commit()

#Load csv data 
#Load customers from csv
with open("../csv/customers.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            "INSERT OR IGNORE INTO customers (customer_id, customer_name) VALUES (?, ?)",
            (row['customer_id'], row['customer_name']))
        
#Load employees from csv
with open("../csv/employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        full_name = f"{row['first_name']} {row['last_name']}"
        
        cursor.execute(
            "INSERT OR IGNORE INTO employees (employee_id, first_name, last_name) VALUES (?, ?, ?)",
            (row["employee_id"], row["first_name"], row["last_name"]))
conn.commit()        
#Load products from csv
with open("../csv/products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            "INSERT OR IGNORE INTO products (product_id, product_name, price) VALUES (?, ?, ?)",
            (row['product_id'], row['product_name'], row['price'])
        )
conn.commit()
#Load orders.csv
with open("../csv/orders.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            "INSERT OR IGNORE INTO orders (order_id, customer_id, employee_id) VALUES (?, ?, ?)",
            (row['order_id'], row['customer_id'], row['employee_id'])
        )

#INSTRUCTIONS:
#find the total price of each first 5 orders:
#Join orders table with the line_items table and the products table.
#GROUP_BY the order_id 
#SELECT the order_id and SUM  of the product price items the line_item quantity
#ORDER BY order_id and LIMIT 5
#print out order_id and total price for each of the rows returned 


query = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
 JOIN line_items li 
ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

cursor.execute(query)

print("Order totals:")
for row in cursor.fetchall():
    print(row)
 #Examople output:
print("Orders:", cursor.execute("SELECT COUNT(*) FROM orders").fetchone())  
print("Line items:", cursor.execute("SELECT COUNT(*) FROM line_items").fetchone())  
print("Products:", cursor.execute("SELECT COUNT(*) FROM products").fetchone()) 
 

#Task 2 
#For each customer , find the average price of their orders. 
#RETURN the total price using AS total_price and return the customer_id with AS customer_id_b.
#left JOIN the customers table with results of the subquery using ON customer_id = customer_id_b
#then after GROUP BY customer_id and get the average of the total price of customer orders in this case the line items
#Return customer name and average total price 

query2 = """
SELECT 
    customers.customer_name,
    AVG(order_totals.total_price) AS average_order_price
FROM customers
LEFT JOIN (
    SELECT 
    orders.customer_id AS customer_id_b,
    SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items 
    ON orders.order_id = line_items.order_id
    JOIN products 
    ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
    ) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id; 
       
"""   
cursor.execute(query2)
results2 = cursor.fetchall()
for row in results2:
    print(row)

#Task 3 
# Need to SELECT statement to retieve the customer _id 
#Anoth SELECT to retrieve the products_ids of the 5 least expensive products
#Another to retrieve the employee_id 
#Create order and 5 line_items records comprising the order
#SELECT with JOIN print out the list of line_item_ids for the order along with the quantity and product namefor each.
#FORGIEN KEYS in INSERT statements must be valid

        
#Get a customer_id
cursor.execute(
   "SELECT customer_id FROM customers WHERE customer_name = ?",
    ("Perez and Sons",)
)
customer_id = cursor.fetchone()[0]


#Get emplpyeee_id
cursor.execute(
    "SELECT employee_id FROM employees WHERE employee_name = ?",
    ("Miranda Harris",)
)
employee_id = cursor.fetchone()[0]

#Get 5 cheapest product_ids
cursor.execute(
    "SELECT product_id FROM products ORDER BY price ASC LIMIT 5"
)
product_ids = [row[0] for row in cursor.fetchall()]

try:
   
    #Insert new order and get order_id
    cursor.execute(
        """
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
        """,
        (customer_id, employee_id)
    )
    order_id = cursor.fetchone()[0]
    
    #Insert line_items
    for product_id in product_ids:
        cursor.execute(
            """
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?);
            """,
            (order_id, product_id, 1)  # quantity set to 1
        )
    conn.commit()
    
except Exception as e:
    conn.rollback()
    raise e

#Verify information was inserted correctly
cursor.execute(
    """
    SELECT line_items.line_item_id, line_items.quantity, products.product_name
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    WHERE line_items.order_id = ?
    """,
    (order_id,)
)
results = cursor.fetchall()

print("Line items for order_id", order_id)
for row in cursor.fetchall():
    print(row)  
    
        
#Task 4 
#Find employees wuth more than 5 orders... want the first_name, the last_name, and the count of orders. 
#JOIN on the employees and orders table then use   GROUP BY employee , COUNT count orders per employee, HAVING filter only those that has more than 5 orders.
#SELECT the employee_id , first_name, last_name, and order count


query3 = """      
SELECT
   e.employee_id,
   e.employee_name, 
   COUNT(o.order_id) AS order_count
   FROM employees e
   JOIN orders o ON e.employee_id = o.employee_id   
    GROUP BY e.employee_id, e.employee_name
    HAVING COUNT(o.order_id) > 5;
"""


cursor.execute(query3)
results3 = cursor.fetchall()
for row in results3:
    print(row) 
    
#Commit and close connection 
conn.commit()
conn.close()