import sys

input = sys.stdin.readline

treeDict = dict()
totalTreeNum = 0

while True:
    treeName = input().rstrip()
    if treeName == "":
        break
    elif treeName in treeDict:
        treeDict[treeName] += 1
        totalTreeNum += 1
    else:
        treeDict[treeName] = 1
        totalTreeNum += 1

sortedTreeList = sorted(treeDict)

for i in sortedTreeList:
    print("%s %.4f" %(i, treeDict[i]/totalTreeNum*100))