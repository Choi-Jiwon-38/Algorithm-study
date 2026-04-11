drinkNum = int(input())

drinkList = list(map(int, input().split()))

drinkList.sort()
drinkList.reverse()

totalDrink = drinkList[0] / 2
for i in drinkList:
    totalDrink += i / 2

print(totalDrink)