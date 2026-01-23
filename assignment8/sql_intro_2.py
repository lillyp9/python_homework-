import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")  

#Task 2: SQL query with JOIN 
query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products 
On line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
# Task 3: print the first 5 rows of the dataframe
print(df.head(5))

#Task 4 - add column "total" to the dataframe
df['total'] = df['quantity'] * df['price']
print(df.head(5))

#Task 5: 
df = df.groupby('product_id').agg({
    'line_item_id': 'count', 
    'total': 'sum',
    'product_name': 'first'}).reset_index()
print(df.head(5))

#Task 6 Sort the DataFrame by product_name
df = df.sort_values(by='product_name')

#Add the dataframe to a file named order_summary.csv
df.to_csv("order_summary.csv")