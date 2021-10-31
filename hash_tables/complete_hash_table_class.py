class ProbingHashTable:
    def __init__(self, max_size=4096):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [(None, None)] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]

    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not (None, None)]


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


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    indx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at indx

        kv = data_list[indx]

        # If it is None, return the index
        if kv == (None, None):
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


probing_table = ProbingHashTable()
probing_table.insert('listen', 99)
print()
print(probing_table.find('listen') == 99)

probing_table.insert('silent', 200)
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)

probing_table.insert('listen', 101)
print(probing_table.find('listen') == 101)

print(probing_table.list_all() == ['listen', 'silent'])
