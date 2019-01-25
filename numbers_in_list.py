# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    # YOUR CODE
    initial_list = [int(string[0])]
    sublist = []
    i = 0
    while i < len(string):
        if i > 0:
            if int(string[i]) <= int(string[i-1]) or (len(sublist) > 0 and int(string[i]) <= max(sublist)):
                sublist.append(int(string[i]))
            else:
                sublist = []
                initial_list.append(int(string[i]))
            if len(sublist) > 0 and sublist not in initial_list:
                initial_list.append(sublist)
        i = i + 1
    return initial_list


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print(numbers_in_lists(string))
print(repr(string), numbers_in_lists(string) == result)
string= '987654321'
print(numbers_in_lists(string))
result = [9,[8,7,6,5,4,3,2,1]]
print(repr(string), numbers_in_lists(string) == result)
string = '455532123266'
print(numbers_in_lists(string))
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(repr(string), numbers_in_lists(string) == result)
string = '123456789'
print(numbers_in_lists(string))
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(repr(string), numbers_in_lists(string) == result)
# print(max([1,2,3]))
