import random

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


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums


insertion_sort(test3['input_list'])