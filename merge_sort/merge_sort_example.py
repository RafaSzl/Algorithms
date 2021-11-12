import random

# If the input list is empty or contains just one element, it is already sorted. Return it.
# If not, divide the list of numbers into two roughly equal parts.
# Sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
# Merge the two sorted lists to get a single sorted list

test0 = {'input_list': [0, 2, 3, 6, -5, 8],
         'output_list': [-5, 0, 2, 3, 6, 8]}
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


def merge_sort(nums):
    # if list is 0 or 1 element long
    if len(nums) > 1:
        # get the midpoint
        mid = len(nums) // 2

        # split the list into two halves
        left_nums = nums[:mid]
        right_nums = nums[mid:]
        print(left_nums)
        print(right_nums)
        # solve the problem for each half recursively
        # after these 2 lines left and right nums are sorted
        left_sorted = merge_sort(left_nums)
        right_sorted = merge_sort(right_nums)


        # merge step
        i = 0  # keep track of leftmost element in left array
        j = 0  # keep track of leftmost element in right array
        k = 0  # keeps track of the index in merge array

        # copy data to temp arrays right_nums and left_nums
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
                k += 1
            else:
                nums[k] = right_nums[j]
                j += 1
                k += 1
        # checking if any element is left
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1
        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1
    print(nums)

merge_sort(test0['input_list'])