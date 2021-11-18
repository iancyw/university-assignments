import random
import time
import math


# Task 1
def radix_sort(num_list, b):
    """
    This function sorts a list using radix sort algorithm.
    :param num_list: array of numbers to be sorted
    :param b: base
    :return: sorted list in ascending order
    :pre: None
    :post: numbers are sorted in ascending order
    :complexity: O((n+b)M), while loops runs until 1st digit of largest number is reached (M), counting sort runs in
    O(n+b) time.
    """
    if not num_list:
        return num_list

    copy_list = num_list[:]

    def counting_sort(array, base, digit):
        """
        Function sorts an array using counting sort algorithm, given by lecture slides.
        :param array: array of numbers to be sorted
        :param base: base to be sorted by
        :param digit: which digit place is it sorting at
        :return: None
        :pre: array of numbers
        :post: numbers are sorted in ascending order according to which digit place it is being sorted at
        :complexity: O(n+b), where n is the number of elements in array, and b is range of input
        """
        size = len(array)
        output = [0] * size
        count = [0] * base
        position = [0] * base

        # constructs count array
        for i in range(0, size):
            num = (array[i] // base ** digit) % base
            count[num] += 1

        # constructs position array
        position[0] = 0
        for i in range(1, base):
            position[i] = position[i - 1] + count[i - 1]

        # constructs output array
        for i in range(0, size):
            num = (array[i] // base ** digit) % base
            output[position[num]] += array[i]
            position[num] += 1

        for i in range(0, size):
            array[i] = output[i]

    # finds the largest number in array, while loop runs until 1st digit of largest number is reached
    max_num = max(copy_list)
    max_digits = int(math.floor(math.log(max_num, b)+1))    # taken from lecture slides; need logbM count sorts
    digit = 0
    while max_digits >= digit:
        counting_sort(copy_list, b, digit)
        digit += 1

    return copy_list


# Task 2
def time_radix_sort():
    """
    This function creates a random test array and times how long radix sort takes to sort the list using different bases
    :return: returns a list of tuples representing the base used in radix sort and how long it took in seconds.
    """
    test_data = [random.randint(1, (2**64)-1) for _ in range(100000)]
    bases = [2, 4, 8, 16, 32, 64, 128]
    output = []

    for base in bases:
        start = time.time()
        radix_sort(test_data, base)
        end = time.time()

        total_time = (end - start)
        output.append((base, total_time))

    return output


# Task 3
def find_rotations(string_list, p):
    """
    This function will return a list of all strings in string_list whose p-rotations also exist in strings list
    :param string_list: a list of strings; each string in this list is unique
    :param p: number of left rotations; a negative p corresponds to right rotations
    :return: a list of all strings in string list whose p-rotations also exist in string_list
    :complexity: O(MN), hopefully
    """
    def string_rotation(string, p):
        """
        This function takes a string and returns the string after a number of p left rotations.
        :param string:  string to be rotated
        :param p:       number of left rotations; if negative, number of right rotations
        :return:        string after number of p left rotations have been applied
        :pre:           string must be of type str
        :complexity:    len(string) = O(1), % operation = O(1), string slicing = O(m), for str of len m,str.join = O(m);
                        overall complexity = O(m)
        """
        slices = [string[(p % len(string)):], string[:(p % len(string))]]
        return ''.join(slices)

    def equalise_word_len(array, max_len):
        """
        This function finds takes an array of strings and if the len(string) != to the max_len, it adds on ` characters
        to the string until len(string) == max_len
        :param array: array of strings
        :param max_len: max length of largest word
        :return: returns a list of tuples, (string, id). strings are all of the same length equal to max_len. id is to
                 keep track of the unique string.
        :complexity: iterates through N elements in list, adds ` to the end of any element that != max_len.
        overall complexity: O(n)
        """
        size = len(array)
        equalised_words_lst = []
        for i in range(0, size):                        # goes through N elements in list
            arr1 = ['`'] * (max_len - len(array[i]))    # adds number of ` depending on len
            part = ''.join(arr1)
            word_parts = [array[i], part]               # joins the word and ` characters together
            equalised_words_lst.append((''.join(word_parts), i))    # adds them to the list as a tuple

        return equalised_words_lst

    def radix_sort_string(array):
        """
        This function implements the radix sort algorithm in order to sort strings.
        :param array: array of tuples, of the form (string, id). Strings must be all of equal length, with ` denoting
                      empty space. ID is to keep track of the unique strings even after being rotated or sorted.
        :return: returns a sorted list of tuples, sorted alphabetically according to the first element of the tuple,
                 string.
        :complexity: The complexity of radix sort is O((n+b)m). As counting sort complexity is O(n), as b= 27;
                     overall complexity = O(MN)
        """
        def counting_sort_strings(array, place):
            """
            This is an implementation of LSD counting sort that is used to sort strings. It goes through from the last
            place of the string and uses the ord() function to form a count list. Unicode characters ` through to z were
            used.
            :param array: an array of tuples, of the form (string, id)
            :param place: the character place, 1 means that it is character str[-(1)]
            :return: returns a list of tuples, where the first element of the tuples are sorted in alphabetical order
            :complexity: As complexity of counting sort is O(n+b), where in this case b= 27, overall complexity is O(N)
            """
            size = len(array)
            output = [0] * size
            count = [0] * 27
            position = [0] * 27

            # constructs count array
            for i in range(0, size):
                num = ord(array[i][0][-place])  # accesses tuple, the tuples string, the place is the char it is sorting
                count[num % 96] += 1            # as the unicode number for ` starts at 96, everything is modulo 96

            # constructs position array
            position[0] = 0
            for i in range(1, 27):
                position[i] = position[i - 1] + count[i - 1]

            # constructs output array
            for i in range(0, size):
                num = ord(array[i][0][-place])  # accesses tuple, the tuples string, the place is the char it is sorting
                output[position[num % 96]] = array[i]
                position[num % 96] += 1

            for i in range(0, size):
                array[i] = output[i]

        length = len(array[0][0])               # finds the max length for string
        place = 1                               # starts strings from the least significant place
        while length >= place:                  # runs until it sorts all columns of chars
            counting_sort_strings(array, place)
            place += 1                          # increments sorting column by one

        return array

    if len(string_list) < 1:
        return []
    copy_list = string_list[:]                  # creates a copy of array of strings
    rotated_strings = []
    output = []
    max_len = 0

    for word in copy_list:                      # iterates through list to find the largest string length
        if len(word) > max_len:
            max_len = len(word)

    equalised_og_list = equalise_word_len(copy_list, max_len)   # equalised list of non-rotated strings; O(n)
    radix_sort_string(equalised_og_list)                        # equalised sorted list of non-rotated strings; O(mn)

    # overall complexity for this block is still O(MN)
    for string in copy_list:                                    # iterates through elements in copy_list: O(n)
        rotated_strings.append(string_rotation(string, p))      # rotates current string and appends it to list, O(m)

    equalised_rotated_list = equalise_word_len(rotated_strings, max_len)    # equalised list of rotated strings; O(n)
    radix_sort_string(equalised_rotated_list)                        # equalised sorted list of rotated strings; O(mn)

    # this compares the elements between two lists, if the strings of their tuples match, we check the ID of the
    # rotated string to see what was the original string it was rotated from and append that to the output list.
    for i in range(0, len(copy_list)):                                      # for loop to len(list); O(n)
        if equalised_og_list[i][0] == equalised_rotated_list[i][0]:         # direct comparison; O(1)
            output.append(copy_list[equalised_rotated_list[i][1]])          # appends to output list.

    return output


if __name__ == "__main__":

    num_list = [18446744073709551615,
                18446744073709551614,
                9,
                11111111111111111111,
                2111111111111111111,
                311111111111111111]

    string_list = ["aaa",
                   "abc",
                   "cab",
                   "acb",
                   "wxyz",
                   "yzwx"]

    print(radix_sort(num_list, 10))
    print(find_rotations(string_list, 2))

    

