# """
# implemented binary search algorithm
#
# Here's a systematic strategy we'll apply for solving problems:
#
# 1 State the problem clearly. Identify the input & output formats.
# 2 Come up with some example inputs & outputs. Try to cover all edge cases.
# 3 Come up with a correct solution for the problem. State it in plain English.
# 4 Implement the solution and test it using example inputs. Fix bugs, if any.
# 5 Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6 Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
#
#
# Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
#
# The number query occurs somewhere in the middle of the list cards.
# query is the first element in cards.
# query is the last element in cards.
# The list cards contains just one element, which is query.
# The list cards does not contain number query.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number query occurs at more than one position in cards.
# """
#
# test_dict = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
#              {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
#              {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
#              {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
#              {'input': {'cards': [6], 'query': 6}, 'output': 0},
#              {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
#              {'input': {'cards': [], 'query': 7}, 'output': -1},
#              {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
#               'output': 7},
#              {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#                         'query': 6},
#               'output': 2}]
#
#
# def binary_search(cards, number):
#     low, high = 0, len(cards) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         mid_number = cards[mid]
#
#         print('low: ' + str(low) + ', high: ' + str(high) + ', mid: ' + str(mid) + ', mid number: ' + str(mid_number))
#
#         if mid_number == number:
#             return print('searched index is ' + str(mid) + ' and value is ' + str(cards[mid]))
#         elif mid_number < number:
#             high = mid -1
#         elif mid_number > number:
#             low = mid + 1
#
#     return print('-1')
#
#
# for i in range(0, len(test_dict)):
#
#     binary_search(test_dict[i]['input']['cards'], test_dict[i]['input']['query'])
#     print(test_dict[i])
#     print(test_dict[i]['input']['cards'])
#     print(test_dict[i]['input']['query'])
#
#
#######################################################################
#
# def duplicate(somelist):
#     """
#     biore binary search na srodku listy
#     sprawdzam
#
#     :param somelist:
#     :return:
#     """
#     emptylist = []
#     for i in somelist:
#         if len(emptylist) == 0:
#             emptylist.append(i)
#         else:
#             if i in emptylist:
#                 return i
#             emptylist.append(i)
#
#
# nums = [3, 1, 3, 4, 2]
#
# x = duplicate(nums)
#
# print(x)
#
#
###################################################
# from random import randrange
#
#
# def guessNumber(n: int) -> int:
#     picked_number = randrange(n)
#     print("Picked number is {}".format(picked_number))
#
#     low, high = 0, n
#
#     while True:
#         guess = (high + low) // 2
#         print('My guess is {}'.format(guess))
#
#         if picked_number > int(guess):
#             print(1)
#             low = guess + 1
#
#         elif picked_number < int(guess):
#             print(-1)
#             high = guess - 1
#
#         else:
#             return 0
#
#
# guessNumber(10)
#
#
############################################

test1 = {'input': [8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 'output': 3}
test2 = {'input': [3, 4, 5, 6, 7, 0, 1, 2], 'output': 5}
test3 = {'input': [1, 2, 3, 4, 5, 6, 7], 'output': 0}
test4 = {'input': [6, 1, 2, 3, 4, 5], 'output': 1}
test5 = {'input': [4, 5, 6, 7, 8, 9, 10, 11, 1], 'output': 8}
test6 = {'input': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'output': 0}
test7 = {'input': [4], 'output': 0}


def rotatedlist_linear(nums):
    """
    Given a roteted sorted list that was rotated some inknown number of times,
    we need to find the number of times it was rotated
    :param nums: a sorted, rotated list e.g. [7, 9, 3, 5, 6]
    :return: rotations: the number of times the sorted list was rotated  e.g. 4 (int)

    Example of inputs:
    A list of size 10 rotated 3 times.
    A list of size 8 rotated 5 times.
    A list that wasn't rotated at all.
    A list that was rotated just once.
    A list that was rotated n-1 times, where n is the size of the list.
    A list that was rotated n times (do you get back the original list here?)
    An empty list.
    A list containing just one element.

    """
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
    position += 1

    return 0


def rotatedlist_binary(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"low:{low}, high:{high}, mid:{mid}")
        if len(nums) > 1 and nums[mid] > nums[mid + 1]:
            return print(mid + 1)
        elif nums[mid] < nums[high]:
            high = mid - 1
        else:
            low = mid + 1
    return print(0)


rotatedlist_binary(test7['input'])
