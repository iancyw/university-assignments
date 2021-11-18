class HashTable:
    def __init__(self, table_capacity=101, hash_base=31):
        """
        This method initialises a HashTable of table_capacity and a given hash_base. If no table_capacity or hash_base
        is given, they are given default values of 101 and 31 respectively

        :param table_capacity: the size of the table
        :param hash_base: the base to be used to calculate the hash value of a key
        :pre: none
        :post: created an array of size table_capacity
        :complexity: best and worst case: O(n), with n being table_capacity
        """
        self.table = [None] * table_capacity
        self.table_size = table_capacity
        self.base = hash_base
        self.count = 0

    def __getitem__(self, key):
        """
        This method returns the value corresponding to the key in the hash_table. If the key does not exist in the table,
        raises a KeyError

        :param key: string key used to access value in hash table
        :return: return a value corresponding to the key
        :pre: key exists in the hash_table
        :post: none
        :complexity: best and worst case: O(1)
        """
        position = self.hash(key)
        if self.table[position] is not None:
            if self.table[position][0] == key:
                return self.table[position][1]
            else:
                orig_pos = position
                while self.table[position][0] != key:
                    position = (position + 1) % self.table_size
                    if self.table[position] is None:    # if probing finds None, key does not exist
                        raise KeyError("Key does not exist in the hash table")
                    if position == orig_pos:            # if after probing the whole array, and returns back to orig
                        raise KeyError("Key does not exist in the hash table")
                return self.table[position][1]
        raise KeyError("Key does not exists in the hash table.")

    def __setitem__(self, key, item):
        """
        This method sets the value corresponding to the key in the hash table to be item. If the hash_table is full,
        This method sets the value corresponding to the key in the hash table to be item. If the hash_table is full,
        the rehash method is called.

        :param key: string key used to set item in hash_table
        :param item: item ot be set in hash_table
        :return: none
        :pre: none
        :post: the value at the hash_table corresponding to the key is now changed to item. if it was the first time,
               the key was used, count has gone up by one, otherwise it remains the same
        :complexity: best case: O(1), setting a value in the hash_table; worst case: O(n), having to rehash
        """
        position = self.hash(key)
        for _ in range(self.table_size):
            if self.table[position] is None:                    # found empty slot
                self.table[position] = (key, item)
                self.count += 1
                return
            elif self.table[position][0] == key:                # found key
                self.table[position] = (key, item)
                return
            else:                                               # not found, try next position
                position = (position + 1) % self.table_size
        self.rehash()
        self.__setitem__(key, item)

    def __contains__(self, key):
        """
        This methods checks if the key is in the hash_table and returns False if not; True otherwise

        :param key: key to be checked if its in the hash_table
        :return: returns True if key is in the table; returns False otherwise
        :pre: none
        :post: none
        :complexity: best and worst case: O(1)
        """
        for position in range(self.table_size):
            if self.table[position] is not None:
                if self.table[position][0] == key:
                    return True
        return False

    def hash(self, key):
        """
        This method calculates the hash_value from a string key

        :param key: the key that is to be converted into a hash_value
        :return: returns the hash_value of the string key
        :pre: none
        :post: none
        :complexity: best and worst case: O(n), where n is the length of the key
        """
        value = 0
        for i in range(len(key)):
            value = (value * self.base + ord(key[i])) % self.table_size
        return value

    def rehash(self):
        """
        This method creates a new array with a size that is the smallest prime number that is larger than twice the
        current size of the table.

        :return: none
        :pre: none
        :post: a new array has been created that is the smallest prime number that is twice the size of the previous
               hash_table. all elements that were in the previous hash_table are inserted back into the new array as
               key, value pairs
        :complexity: best and worst case: O(n), where n is the size of the previous table
        """
        primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                  919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                  17519, 21023, 25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437,
                  187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                  1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]

        i = 0
        old_array = self.table
        while primes[i] < (2*self.table_size):
            i += 1
        self.table = [None] * primes[i]
        self.table_size = primes[i]
        self.count = 0
        for entry in old_array:
            if entry is not None:
                key, item = entry[0], entry[1]
                self.__setitem__(key, item)


if __name__ == "__main__":
    table = HashTable()
