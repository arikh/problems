# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(square):
    # Your code here
    if not all(len(square) == len(row) for row in square): return False
    rows = [item for item in square]
    columns = []
    x = 0
    while x < len(square):
        temp = []
        y = 0
        while y < len(square[x]):
            temp.append(square[y][x])
            y = y + 1
        columns.append(temp)
        x = x + 1
    return match_list(rows, columns)



def match_list(list_one,list_two):
    for i, n in enumerate(list_one):
        if list_one[i] != list_two[i]:
            return False
    return True







print(symmetric([[1, 2, 3],
               [2, 3, 4],
               [3, 4, 1]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]]))
# #>>> True
#
print(symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "dog"],
               ["fish","fish","cat"]]))
# #>>> False
#
print(symmetric([[1, 2],
               [2, 1]]))
# #>>> True
#
print(symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 6]]))
# #>>> False
#
print(symmetric([[1,2,3],
                [2,3,1]]))
#>>> False
