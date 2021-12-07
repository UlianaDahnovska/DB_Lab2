import csv
import psycopg2

INPUT_CSV_FILE = 'furniture.csv'

createQuery = '''
CREATE TABLE Furniture (
    FURNITURE_ID SERIAL PRIMARY KEY  ,
	FURNITURE_NAME VARCHAR(80),
	FURNITURE_SHORT_DESCRIPTION INT,
	FURNITURE_CATEGORY_ID INT REFERENCES Category(FURNITURE_CATEGORY_ID)
);
'''
deleteQuery = '''
DROP TABLE Furniture CASCADE 
'''
insertQuery = '''
INSERT INTO Furniture (FURNITURE_NAME, FURNITURE_SHORT_DESCRIPTION) VALUES (%s, %s)
'''

connection = psycopg2.connect(
                        database="Lab3", 
                        user="username", 
                        password="password", 
                        host="localhost", 
                        port=5432)
                        
with connection:
    cursor = connection.cursor()
    cursor.execute(deleteQuery)
    cursor.execute(createQuery)
    with open(INPUT_CSV_FILE, 'r') as inputFile:
        data = csv.DictReader(inputFile)
        for idx, row in enumerate(data):
                row['furniture'] = row['furniture'][:-1]
                if(row['furniture'][-1] == 'm'):
                    row['furniture'] = row['furniture'][:-1]
                values = (row['furnitureItem'], row['furniture'])
                cursor.execute(insertQuery, values)

    connection.commit()
