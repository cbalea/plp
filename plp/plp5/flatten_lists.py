'''
Write a program that will flatten a list up to a maximum given depth. The user will input the list and the depth.

Ex: 
initial list: L = [1, [2, 3], ["a", ["b","c"]], 9]
max_depth = 2
Expected result: 
[1, 2, 3, "a", ["b", "c"], 9]
'''

originalList = [1, [2, 3], ["a", ["b","c"]], 9]
targetDepth = 2


for i in range(targetDepth-1):
    flattedList = []
    for elem in originalList:
        if type(elem) is list:
            flattedList.extend(elem)
        else:
            flattedList.append(elem)
    originalList = flattedList

print flattedList
