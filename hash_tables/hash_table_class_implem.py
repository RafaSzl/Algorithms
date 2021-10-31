class HashTable:

    def __init__(self, max_size= 4096):
        self.data_list = [(None, None)] * max_size

    def insert(self, key, value):
        indx = get_index(self.data_list, key)
        self.data_list[indx] = key, value

    def find(self, key):
        """Find the value associated with a key"""
        indx = get_index(self.data_list, key)
        if key is None:
            return None
        key, value = self.data_list[indx]
        return value

    def update(self, key, value):
        """Change the value associated with a key"""
        indx = get_index(self.data_list, key)
        self.data_list[indx] = key, value

    def list_all(self):
        """List all the keys"""
        return [kv[0] for kv in self.data_list if kv is not None]


# if the statement is true do nothin, if it is not gives error
# for item in data_list:
#     assert item == None


def get_index(data_l, a_string):

    result = 0

    for character in a_string:
        # converts char into number by using func ord
        a_number = ord(character)

        result += a_number
    # len data, not max hash fun lenght due to making func generic, not taking any variable from somewhere else
    print('summary of all numbers from ord(): {}'.format(result))
    print('length of data: {}'.format(len(data_l)))
    list_index = result % len(data_l)
    print('List index: {}'.format(list_index))
    return list_index


# tests for get_index fund
# print(get_index(data_list, '') == 0)
# data_list2 = [None] * 48
# print()
# get_index(data_list2, 'Aakash')
# print()
# print(ord('A') + ord('a') + ord('k') + ord('a') + ord('s') + ord('h'))
# print(585 % 48)
# print(get_index(data_list2, 'Aakash'))


first_table = HashTable(max_size=1024)
first_table.insert('Aakash', '999898')
first_table.insert('Hemanth', '1238562')
print()
first_table.find('Aakash')
print()
print(first_table.list_all())


"""
As you can see above, the value for the key listen was overwritten by the value for the key silent. Our hash table 
implementation is incomplete because it does not handle collisions correctly.

To handle collisions we'll use a technique called linear probing. Here's how it works:

While inserting a new key-value pair if the target index for a key is occupied by another key, then we try the next 
index, followed by the next and so on till we the closest empty location.

While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for
 a location which contains a key-value pair with the matching key.

While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for
 a location which contains a key-value pair with the matching key, and update its value.

We'll define a function called get_valid_index, which starts searching the data list from the index determined by
 the hashing function get_index and returns the first index which is either empty or contains 
 a key-value pair matching the given key.

"""


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    indx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at indx
        kv = data_list[indx]

        # If it is None, return the index
        if key is None:
            return indx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return indx

        # Move to the next index
        indx += 1

        # Go back to the start if you have reached the end of the array
        if indx == len(data_list):
            indx = 0
