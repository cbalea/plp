'''
Write a script that gets some numbers from the user and creates a function that create an ordered list from these numbers.
Hint: Use variable-length arguments.
'''

def sort_numbers(*numbers):
    return sorted(list(numbers))
    
print sort_numbers(3, 5, 6, 3)