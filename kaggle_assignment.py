"""
Instructions
Download a dataset from Kaggle and load it into a database of your choice! Options: SQLite, MySQL, or PostgreSQL

Must have at least 100 rows.

https://www.kaggle.com/datasets
"""
import pandas as pd
import sqlite3

df = pd.read_csv("diamonds.csv")
print(df.head())
print(df.tail())

connection = sqlite3.connect("diamond_rating.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS diamonds")
# create table
df.to_sql("diamonds", connection)
connection.close()

# load data into the table