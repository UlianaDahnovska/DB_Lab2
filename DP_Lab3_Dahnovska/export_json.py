import json
import psycopg2

OUTPUT_FILE = 'data.json'

TABLES = [
    'Furniture',
    'Category',
    'Furniture_Price',
]

connection = psycopg2.connect(
                        database="Lab3", 
                        user="username", 
                        password="password", 
                        host="localhost", 
                        port=5432)
                        
data = {}

with connection:
    cursor = connection.cursor()
    for table in TABLES:
        cursor.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cursor.description]
        for row in cursor:
            rows.append(dict(zip(fields, row)))
        data[table] = rows

with open(OUTPUT_FILE_T.format(table_name), 'w') as outFile:
    json.dump(data, outFile, default = str)
    