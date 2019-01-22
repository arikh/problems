# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(square):
    # Your code here
    if not all(len(square) == len(row) for row in square): return False
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
    return asymmetric_match(square, columns)


def asymmetric_match(list_one, list_two):
    x = 0
    while x < len(list_one):
        y = 0
        while y < len(list_one[x]):
            if list_one[x][y] != - list_two[x][y]:
                return False
            y = y + 1

        x = x + 1
    return True


# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
