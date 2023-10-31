import pandas as pd
import pyodbc

conn_str = (
    r'DRIVER= {ODBC Driver 17 for SQL Server};'
    r'SERVER= server_placeholder;'
    r'DATABASE= database_placeholder;'
    r'UID= username_placeholder;'
    r'PWD= password_placeholder'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

df = pd.read_csv("procedimentos.csv")
data = df.values.tolist()

sql = 'INSERT INTO table_name_placeholder (column1, column2, column3, ...) VALUES (?, ?, ?, ...)'

for row in data:
    cursor.execute(sql, row)
conn.commit()

cursor.close()
conn.close()
