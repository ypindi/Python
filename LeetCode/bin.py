# rows = [""]*5
# rows[2] += "Anu"

# print(rows[2])

# visited = set()
# print(visited)

# visited.add(3)
# print(visited)

# strs = ["eat", "tea"]
# strs.pop()

# print(strs)


myDict1 = {"a": 1, "b": 2}
myDict2 = {"b": 2, "a": 1}
# if myDict1 == myDict2:
#     print("Equal")
# else:
#     print("Not Equal")

myListOfDicts = []
myListOfDicts.append(myDict1)
print(myListOfDicts)
if myDict2 in myListOfDicts:
    print("Found")
else:
    print("Not Found")