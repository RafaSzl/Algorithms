
import random
import timeit
import random
# sort the given list
# first of all create test samples
test0 = {'input_list': [0, 2, 3, -5, 23, -42],
         'output_list': [-42, -5, 0, 2, 3, 23]}

test1 = {'input_list': [3, 5, 6, 8, 9, 10, 99],
         'output_list': [3, 5, 6, 8, 9, 10, 99]}

test2 = {'input_list': [99, 10, 9, 8, 6, 5, 3],
         'output_list': [3, 5, 6, 8, 9, 10, 99]}

test3 = {'input_list': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0],
         'output_list': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]}

test4 = {'input_list': [],
         'output_list': []}

test5 = {'input_list': [14],
         'output_list': [14]}

test6 = {'input_list': [[42, 42, 42, 42, 42, 42, 42]],
         'output_list': [[42, 42, 42, 42, 42, 42, 42]]}

in_list = list(range(100))
out_list = list(range(100))
random.shuffle(in_list)

test7 = {'input_list': in_list,
         'output_list': out_list}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]


def bubble_sort(g_list: list) -> list:
    # copy of the list to avoid changing it!!!
    g_list_copy = g_list
    while True:
        for x in range(len(g_list_copy) - 1):
            if x+1 == len(g_list_copy):
                continue
            if g_list_copy[x] > g_list_copy[x+1]:
                g_list_copy[x], g_list_copy[x+1] = g_list_copy[x+1], g_list_copy[x]
                # print(g_list)

        # print(g_list_copy)
        if g_list_copy == sorted(g_list_copy):
            return g_list_copy


bubble_sort(test2['input_list'])

print(bubble_sort(test2['input_list']) == test2['output_list'])


def bubble_sort2(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    # print('bubble_sort', nums)
    # 4. Repeat the process n-1 times
    for j in range(len(nums) - 1):
        # print('iteration', j)
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            # print('i', i, nums[i], nums[i+1])
            # 2. Compare the number with
            if nums[i] > nums[i + 1]:
                # 3. Swap the two elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # print(nums)
    # Return the sorted list
    return nums


bubble_sort2(test3['input_list'])
print(bubble_sort2(test3['input_list']) == test3['output_list'])
