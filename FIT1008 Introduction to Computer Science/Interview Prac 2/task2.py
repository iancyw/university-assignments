# Ian Wong
# 30612616
# 17/09/2019
# !/usr/bin/python3
import math


class ListADT:
    def __init__(self, size=40):
        """
        Creates an empty array of a certain size. If no size is given, creates a array of size 40.

        :param size: size of the array
        :return: none
        :complexity: best and worst case: O(1)
        :pre: none
        :post: array of size is created. size must be at least 40
        """
        if size < 40:   # if size < 40, sets size to 40
            print("Size must be at least 40. Setting to 40 now.")
            size = 40
        self.the_array = [None] * size
        self.length = 0

    def __str__(self):
        """
        This method prints the list as a string, with an item on a new line. If list is empty, prints an empty string

        :return: returns a list as a string with each item on a new line. if the list is empty, returns empty string
        :pre: none
        :post: none
        :complexity: best case: O(1) (empty list, prints out empty string), worst case: O(n), (n = size of list)
        """
        my_str = ""
        if self.is_empty():
            return my_str
        for i in range(0, self.length):
            my_str += str(self.the_array[i]) + "\n"
        return my_str

    def __len__(self):
        """
        This method returns the length of the list

        :return: returns the length of the list
        :pre: none
        :post: none
        :complexity: best and worst case: O(1)
        """
        return self.length

    def __getitem__(self, index):
        """
        This method returns the item at the index in the list.

        :param index: index of the item in the list
        :return: returns the item at the index in the list; raises an index error if the index is out of bounds
        :pre: not an empty list
        :post: none
        :complexity: worst and best case: O(1)
        """
        if self.is_empty():
            raise IndexError("Attempted to get item from empty list.")
        elif index not in range(-self.length, self.length):
            raise IndexError("Index out of bound.")
        else:
            if index < 0:
                return self.the_array[index + self.length]
            else:
                return self.the_array[index]

    def __setitem__(self, index, item):
        """
        Sets the value at index in the list to be item

        :param index: index where item will be set
        :param item: item to be set at index
        :return: none
        :pre: not an empty list; index is is within bounds
        :post: item at index has changed to item
        :complexity: best and worst case: O(1)
        """
        if self.is_empty():
            raise IndexError("Attempted to set value in empty list.")
        elif index not in range(-self.length, self.length):
            raise IndexError("Index out of bound.")
        else:
            if index < 0:
                self.the_array[index + self.length] = item
            else:
                self.the_array[index] = item

    def __eq__(self, other):
        """
        Checks if the ListADT self is equal to the ListADT other, regardless of the underlying array length

        :param other: a ListADT to compare self against
        :return: returns True if self == other; returns False otherwise
        :pre: other must be a ListADT, otherwise returns AttributeError
        :post: self and other are equal ListADTS
        :complexity: best and worst case: O(n)
        """
        try:
            if self.length == other.length:
                for i in range(0, self.length):
                    if not self.the_array[i] == other.the_array[i]:
                        return False
                return True
            return False
        except AttributeError:
            return False

    def insert(self, index, item):
        """
        Inserts an item into an index in the list, shifting other items aside. If the index is eq to last index,
        then append to end of list

        :param index: index where item is to be inserted
        :param item: item to be inserted into the list
        :return: none
        :pre: index must be in range
        :post: a ListADT with an extra item, inserted at the index given. if index is -1 or self.length, append at end
        :complexity: best case: O(1), appending to the end of list; worst case: O(n), shifting everything to one side
        """
        if index == -1:
            self.append(item)
            return
        if index not in range(-(self.length + 1), self.length + 1):
            raise IndexError("Index out of bounds.")
        elif index < 0:
            previous = self.the_array[index + (self.length + 1)]      # copies the item at the given index to previous
            self.the_array[index + (self.length + 1)] = item          # sets the item at the given index to item
            self.length += 1                                    # increases the length of the list by 1
            for i in range(index + (self.length + 1), self.length):
                current = self.the_array[i]                     # copies the current item
                self.the_array[i] = previous                    # sets the current item to be the previous item
                previous = current                              # sets the previous item to current item
        else:
            previous = self.the_array[index]                    # copies the item at the given index to previous item
            self.the_array[index] = item                        # sets the item at the given index to item
            self.length += 1                                    # increases the length of the list by 1
            for i in range(index + 1, self.length):
                current = self.the_array[i]                     # copies the current item
                self.the_array[i] = previous                    # sets the current item to be the previous item
                previous = current                              # sets the previous item to current item
        if self.is_full():
            self.the_array += [None] * math.ceil((len(self.the_array) * 0.9))   # increases the size of array by 1.9

    def delete(self, index):
        """
        This method deletes the item at a certain index and shifts everything to the left one index.

        :param index: the index of the item you wish to delete
        :return: none
        :pre: the list is not empty, index is not > self.length and not < -self.length
        :post: the list has one item removed, with a decreased length of 1. if the len(list) is 1/4 the size of the
               the array after deletion, halve the size of the array (size of the array cannot be < 40)
        :complexity: best case: O(1), deleting the last index; worst case: O(n), deleting the first index
        """
        if self.is_empty():                         # checks if list is empty, can't delete from empty list
            raise IndexError("Attempted to delete from empty list.")
        if index not in range(-self.length, self.length):
            raise IndexError("Index out of bounds.")
        if index < 0:                               # if the index is negative, adds the length to make it positive
            for i in range(index + self.length, self.length):
                self.the_array[i] = self.the_array[i + 1]
            self.length -= 1
        else:
            for i in range(index, self.length - 1):
                self.the_array[i] = self.the_array[i + 1]
            self.length -= 1
        if self.length < (len(self.the_array)/4):   # checks if the length of the list < len(the_array)/4
            if (len(self.the_array)/2) >= 40:       # checks if you were to halve the array, would it still be >= 40
                tmp = ListADT(math.ceil(len(self.the_array)*0.5))
                for i in range(0, self.length):
                    tmp.append(self.the_array[i])                   # copies all the items in the list to the tmp array
                self.the_array = tmp.the_array                      # sets the original array to the tmp array

    def is_empty(self):
        """
        This method checks if the list is empty.

        :return: returns True if length of list is 0; returns False otherwise
        :pre: none
        :post: none
        :complexity: best and worst case: O(1)
        """
        return self.length == 0

    def is_full(self):
        """
        This method checks if the list is full.

        :return: returns True if the size of the list is equal to the size of the array; returns False otherwise
        :pre: none
        :post: none
        :complexity: best and worst case: O(1)
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
        This method checks if the list contains an item.

        :param item: the item that is checked if its in the list
        :return: returns True if the item is in the list; returns False otherwise
        :complexity: best case: O(1) (item is at the first index),worst case: O(n), (n = size of list, item not in list)
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def append(self, item):
        """
        This method adds an item onto the end of the list and increases the size of the list by 1.

        :param item: the item to be appended
        :return: none
        :pre: array is not full
        :post: item has been added to end of the list and length of list has been increased by 1. if list is full after
               append, increase the size of the array by 1.9 (rounding up)
        :complexity: best and worst case: O(1)
        """
        if not self.is_full():
            self.the_array[self.length] = item
            self.length += 1
            if self.is_full():
                self.the_array += [None] * math.ceil(len(self.the_array)*0.9)  # if the array is full, increases by 1.9
        else:
            raise Exception('List is full')

    def unsafe_set_array(self, array, length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')

        self.the_array = array
        self.length = length


if __name__ == "__main__":
    x = ListADT(40)
    lines = ListADT(40)
    lines.append(1)
    lines.append(2)
    lines.append(3)
    lines.append(4)
    lines.append(5)
    for item in range(lines.length, 0, -1):
        x.insert(0, item)
    print(x.the_array)
    x.insert(5, 0)
    print(x.the_array)
