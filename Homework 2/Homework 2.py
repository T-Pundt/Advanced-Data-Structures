class DynamicArray:
    def __init__(self, initial_capacity=10):
        self._capacity = initial_capacity
        self._size = 0
        self._array = [None] * self._capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, element):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = element
        self._size += 1

    def __getitem__(self, index):
        if not 0 <= index < self._capacity:
            raise IndexError('Index out of range')
        return self._array[index]

    def __setitem__(self, index, _value):
        if not 0 <= index < self._capacity:
            raise IndexError('Index out of range')
        self._array[index] = _value

    def __len__(self):
        return self._size

    def __delitem__(self, index):
        if not 0 <= index < self._capacity:
            raise IndexError('Index out of range')
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1


class HashTable:
    def __init__(self, initial_capacity=10, load_factor=0.75):
        self._capacity = initial_capacity
        self._size = 0
        self._load_factor = load_factor
        self._array = DynamicArray(initial_capacity)

    def _resize(self, new_capacity):
        old_array = self._array
        self._capacity = new_capacity
        self._array = DynamicArray(new_capacity)
        self._size = 0

        for bucket in old_array:
            if bucket is not None:
                # Check if the bucket contains a single key-value pair or multiple pairs
                if isinstance(bucket[0], tuple):
                    for key, value in bucket:
                        self[key] = value
                else:
                    key, value = bucket
                    self[key] = value

    def _hash1(self, key):
        return hash(key) % self._capacity

    def _hash2(self, key):
        return 1

    def _double_hash(self, key, attempt):
        return (self._hash1(key) + attempt * self._hash2(key)) % self._capacity

    def _probe(self, index, _key):
        initial_index = index
        while self._array[index] is not None and self._array[index][0] != _key:
            index = (index + 1) % self._capacity
            if index == initial_index:
                return None  # Full table
        return index

    def _should_resize(self):
        return self._size >= self._capacity * self._load_factor

    def __setitem__(self, _key, _value):
        if self._size >= self._load_factor * self._capacity:
            self._resize(2 * self._capacity)
        index = self._hash1(_key)
        initial_index = index
        attempt = 0
        while self._array[index] is not None and self._array[index][0] != _key:
            attempt += 1
            index = self._double_hash(_key, attempt)
            if index == initial_index:
                raise ValueError("Hash table is full")
        self._array[index] = (_key, _value)
        self._size += 1

        if self._should_resize():
            self._resize(self._capacity * 2)

    def __getitem__(self, _key):
        index = self._hash1(_key)
        initial_index = index
        attempt = 0
        while self._array[index] is not None:
            if self._array[index][0] == _key:
                return self._array[index][1]
            attempt += 1
            index = self._double_hash(_key, attempt)
            if index == initial_index:
                break
        raise KeyError(_key)

    def __delitem__(self, key):
        index = self._hash1(key)
        initial_index = index
        attempt = 0
        while self._array[index] is not None:
            if self._array[index][0] == key:
                self._array[index] = None
                self._size -= 1
                return
            attempt += 1
            index = self._double_hash(key, attempt)
            if index == initial_index:
                break
        raise KeyError(key)

    def __contains__(self, _key):
        try:
            _ = self[_key]
            return True
        except KeyError:
            return False

    def __len__(self):
        return self._size

    def __repr__(self):
        elements = []
        for _item in self._array:
            if _item is not None:
                elements.append(_item)
        return '{' + ', '.join(f'{k}: {v}' for k, v in elements) + '}'

    def items(self):
        for bucket in self._array:
            if bucket is not None:
                yield bucket


if __name__ == "__main__":
    hash_table = HashTable()

    import pandas as pd
    from pathlib import Path

    # This section of code creates the file pathway that is later used to open the csv file
    # Reference to reddit post was made here
    root_dir = Path(__file__).parent
    file = root_dir / 'us-contacts (2).csv'

    # reads in the data from the csv file, Header = None is to make sure the first line of data is read in
    dataframe = pd.read_csv(file, header=None)

    # converts the csv data stored in dataframe to a list of lists (Dynamic Array)
    contacts = dataframe.values.tolist()

    print(contacts[0][8])

    hash_table[contacts[0][8]] = contacts[0]
    hash_table[contacts[1][8]] = contacts[1]
    # Add key-value pairs
    hash_table['apple'] = 1
    hash_table['banana'] = 2
    hash_table['little'] = 1
    # hash_table['a'] = 4
    # hash_table['b'] = 5
    # hash_table['c'] = 6
    # hash_table['d'] = 7
    # hash_table['e'] = 8
    # hash_table['f'] = 9
    # hash_table['g'] = 10
    # hash_table['h'] = 11
    #
    # Retrieve values
    print(hash_table['apple'])  # Output: 1

    # Check if a key exists
    print('banana' in hash_table)  # Output: True

    # # Delete a key-value pair
    del hash_table['banana']
    del hash_table['apple']
    # print(hash_table)  # Output: {'apple': 1, 'cherry': 3}

    # # Get the number of key-value pairs
    print(len(hash_table))  # Output: 2
    #
    # # Iterate over key-value pairs
    for item in hash_table.items():
        print(item)
