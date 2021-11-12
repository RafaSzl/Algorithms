# Write a function to merge two sorted arrays

def merge(list1: list, list2: list) -> list:
    list1 = list(list1)
    list2 = list(list2)
    new_list = []

    while True:
        x = 0

        if len(list1) == 0:
            new_list.extend(list2)
            list2 = []
        elif len(list2) == 0:
            new_list.extend(list1)
            list1 = []

        if len(list1) == 0 and len(list2) == 0:
            print(new_list)
            return new_list

        if list1[x] > list2[x]:
            new_list.append(list2[x])
            list2.pop(x)
        elif list1[x] < list2[x]:
            new_list.append(list1[x])
            list1.pop(x)
        elif list1[x] == list2[x]:
            new_list.append(list1[x])
            new_list.append(list2[x])
            list1.pop(x)
            list2.pop(x)


some_list = [0, 4, 6, 12]
some_list2 = [4, 12, 13]

merge(some_list, some_list2)

