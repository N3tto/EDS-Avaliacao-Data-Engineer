import requests
import pandas as pd
import pyodbc

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=your_server;'
    r'DATABASE=your_database;'
    r'UID=your_username;'
    r'PWD=your_password'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

response = requests.get('https://your_api_endpoint.com/data')
data = response.json()

df = pd.DataFrame(data)

data = df.values.tolist()

sql = 'INSERT INTO your_table_name (column1, column2, column3, ...) VALUES (?, ?, ?, ...)'

for row in data:
    cursor.execute(sql, row)
conn.commit()

cursor.close()
conn.close()
