n, continuedDay = map(int, input().split())
visitorList = list(map(int, input().split()))

maxVisitor = 0
dayCount = 0

continuedVisitor = sum(visitorList[0:continuedDay])

for i in range(n-continuedDay+1):
    if maxVisitor < continuedVisitor:
        maxVisitor = continuedVisitor
        dayCount = 1
    elif maxVisitor == continuedVisitor:
        dayCount += 1
    
    if i != n-continuedDay:
        continuedVisitor = continuedVisitor - visitorList[i] + visitorList[i + continuedDay]

if maxVisitor == 0:
    print("SAD")
else:
    print(maxVisitor)
    print(dayCount)