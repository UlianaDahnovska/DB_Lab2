import csv
import psycopg2

OUTPUT_FILE = 'data.csv'

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
        fields = [x[0] for x in cursor.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outFile:
            data = csv.data(outFile)
            data.writerow(fields)
            for row in cursor:
                data.writerow([str(x) for x in row])

 
