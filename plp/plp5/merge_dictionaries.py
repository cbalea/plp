'''
Write a program that will merge 2 dictionaries with any depth (including contained dictionaries, lists, sets, strings, integers,
floats). Type mismatches should yield a tuple with the two elements.

Examples:
a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

Expected result:
{'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3,2]}, 'm': ([1], "wer")}
'''
from pprint import pprint

a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2], 'b': {'c': 1}}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2], 'b': {'c':2}}, 'm': "wer"}

c = dict()

for key in a.keys():
    try:
        if type(a[key]) == set:
            c[key] = a[key].union(b[key])
        elif type(a[key]) == dict:
            c[key] = dict()
#            stillHaveDict = False
#            while stillHaveDict:
            for deepKey in a[key].keys():
                c[key][deepKey] = a[key][deepKey] + b[key][deepKey]
#                    if type(a[key][deepKey]) == dict:
#                        stillHaveDict = True
        else:
            c[key] = a[key] + b[key]
    except TypeError:
        c[key] = (a[key], b[key], )
    

pprint(c)
