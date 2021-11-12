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
    # loop for outer (unsorted) items. index 0 is in 'sorted' part
    for i in range(1, len(nums)):
        # index j that starts at index of outer loop and iterates the list to the left and checks if we need to do swaps
        # and stops if we dont need to swap anymore - if the right place for current number is found
        j = i
        # inner loop, check if left neighbour is bigger than the current element
        # and we check if j is bigger than 0, due to not point to -1 index in a list
        while nums[j-1] > nums[j] and j > 0:
            # it looks for the entry at index j and puts it entry at index j-1, and from j-1 to j
            nums[j-1], nums[j] = nums[j], nums[j-1]
            # we need to go further to the left
            j -= 1
    return nums


insertion_sort(test3['input_list'])