# myList = []
# myList.append(3)
# myList.append(4)
# myList.append(None)

# print(myList)





l = [3,4,4,3]
n = len(l)
for i in range(n//2):
    print(l[i])
    print(l[n-i-1])
    if l[i] != l[n-1-i]:
        print("NOO")