import matplotlib.pyplot as plt
import main


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