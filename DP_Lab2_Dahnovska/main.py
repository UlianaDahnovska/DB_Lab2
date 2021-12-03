import psycopg2

query1 = ''' 
SELECT Category.FURNITURE_CATEGORY_NAME,Furniture_Price.FURNITURE_PRICE 
FROM Furniture 
JOIN Category ON Furniture.FURNITURE_CATEGORY_ID = Category.FURNITURE_CATEGORY_ID 
JOIN Furniture_Price ON Furniture.FURNITURE_ID = Furniture_Pricefood_id  
'''

query2 = '''
SELECT Furniture.FURNITURE_NAME, 
SUM(FURNITURE_PRICE) AS COST 
FROM Furniture
JOIN Furniture_Price ON Furniture.FURNITURE_ID = Furniture_Price.FURNITURE_ID
GROUP BY Furniture.FURNITURE_NAME
'''

query3 = '''
SELECT DISTINCT(Category.FURNITURE_CATEGORY_NAME),
COUNT(Furniture.FURNITURE_NAME) 
FROM Furniture  
JOIN Category ON Furniture.FURNITURE_CATEGORY_ID = Category.FURNITURE_CATEGORY_ID   
GROUP BY Category.FURNITURE_CATEGORY_NAME
'''

connection = psycopg2.connect(
                        database="Lab2", 
                        user="username", 
                        password="password", 
                        host="localhost", 
                        port=5432)

cursor = connection.cursor()
cursor.execute(query1)
avaragePrice = cursor.fetchall()
print("First query:- ", avaragePrice)

cursor.execute(query2)
itemSameCost = cursor.fetchall()
print("Second query:- ", itemSameCost)

cursor.execute(query3)
countCategory = cursor.fetchall()
print("Third query:- ", countCategory) 
