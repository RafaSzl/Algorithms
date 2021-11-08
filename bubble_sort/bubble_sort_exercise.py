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

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test7 = {'input_list': [in_list],
         'output_list': [out_list]}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]


def bubble_sort(g_list: list) -> list:
    while True:
        for x, y in enumerate(g_list):
            if x+1 == len(g_list):
                continue
            if g_list[x] > g_list[x+1]:
                comp_val = g_list[x]
                g_list[x] = g_list[x+1]
                g_list[x+1] = comp_val
                print(g_list)

        print(g_list)
        if g_list == sorted(g_list):
            return g_list


bubble_sort(test0['input_list'])


