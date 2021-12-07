import psycopg2
import matplotlib.pyplot as plt

query_1 = ''' 
CREATE VIEW AvaragePriceByCategory as 
SELECT DISTINCT(Category.FURNITURE_CATEGORY_NAME),
COUNT(Furniture.FURNITURE_NAME) 
FROM Furniture  
JOIN Category ON Furniture.FURNITURE_CATEGORY_ID = Category.FURNITURE_CATEGORY_ID   
GROUP BY Category.FURNITURE_CATEGORY_NAME
'''

query_2 = '''
CREATE VIEW ItemSameCost as
SELECT Furniture.FURNITURE_NAME, 
SUM(FURNITURE_PRICE) AS COST 
FROM Furniture
JOIN Furniture_Price ON Furniture.FURNITURE_ID = Furniture_Price.FURNITURE_ID
GROUP BY Furniture.FURNITURE_NAME
'''

query_3 = '''
CREATE VIEW CountCategory as 
SELECT Category.FURNITURE_CATEGORY_NAME,Furniture_Price.FURNITURE_PRICE
FROM Furniture
JOIN Category ON Furniture.FURNITURE_CATEGORY_ID = Category.FURNITURE_CATEGORY_ID 
JOIN Furniture_Price ON Furniture.FURNITURE_ID = Furniture_Price.FURNITURE_ID
'''

connection = psycopg2.connect(
                        database="Lab3", 
                        user="username", 
                        password="password", 
                        host="localhost", 
                        port=5432)
                        
with connection:

    cursor = connection.cursor()
    cursor.execute('DROP VIEW IF EXISTS CountCategory')
    cursor.execute(query_1)
    cursor.execute('SELECT * FROM CountCategory')
    countCategory  = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS ItemSameCost')
    cursor.execute(query_2)
    cursor.execute('SELECT * FROM ItemSameCost')
    itemSameCost = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS AvaragePriceByCategory')
    cursor.execute(query_3)
    cursor.execute('SELECT * FROM AvaragePriceByCategory')
    avaragePrice = cursor.fetchall()

    furnitureData = {
    'BILLY': main.itemSameCost[0][1],
    'KALLVIKEN': main.itemSameCost[1][1],
    'EKET': main.itemSameCost[2][1],
    'LYCKSELE MURBO': main.itemSameCost[3][1],
    'VALLENTUNA': main.itemSameCost[4][1],
    'KULLABERG': main.itemSameCost[5][1],
    'NORDVIKEN': main.itemSameCost[6][1]
}
fig, ax = plt.subplots()
ax.pie(furnitureData.values(), 
       labels=furnitureData.keys(), 
       autopct='%1.1f%%', 
       shadow=True,
       rotatelabels=True)
plt.show()

furnitureData = {}
for i in range(len(main.avaragePrice)):
    furnitureData[main.avaragePrice[i][0]] = main.avaragePrice[i][1]

fig, ax = plt.subplots()
ax.plot(furnitureData.keys(), furnitureData.values(), )
plt.xlabel('Category')
plt.ylabel('Avarage category')
plt.show()

furnitureData = {}
for i in range(len(main.countCategory)):
    furnitureData[main.countCategory[i][0]] = main.countCategory[i][1]

plt.bar(furnitureData.keys(), furnitureData.values(), width=0.5)
plt.xlabel('Category')
plt.ylabel('Count category')
plt.show()