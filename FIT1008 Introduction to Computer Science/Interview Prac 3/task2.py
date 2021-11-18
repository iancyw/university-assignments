import csv
import task1
import time


def load_dictionary(hash_table, filename, time_limit=300):
    """
    This function loads words from a dictionary into a HashTable.

    :param hash_table: class HashTable
    :param filename: name of file to read from
    :param time_limit: optional argument, time_limit for loading dictionary
    :return: none
    :pre: file must exist within same directory as file
    :post: HashTable has been filled with key and value pairs
    :complexity: best case: O(n); worst case: O(n), having to rehash after insertion
    """
    with open(filename) as f:
        start = time.time()
        for line in f:
            line = line[:-1]
            hash_table[line] = 1
            if (time.time() - start) > time_limit:
                raise Exception("Loading dictionary has exceeded time limit.")
    f.close()


def load_dictionary_time(hash_base, table_size, filename, max_time):
    """
    This method creates a HashTable, with hash_base and table_size

    :param hash_base: the base to be used to calculate the hash_value from keys
    :param table_size: the size of the HashTable
    :param filename: the name of the file to be read from; the dictionary
    :param max_time: max time the program is allowed to run for
    :return: returns a tuple consisting of unique_words loaded and the time taken to load. If time taken exceeds
             max_time, time_taken is returned as none
    :pre: file should exist in the same directory as program
    :post: hashtable has been created with key and value pairs
    :complexity: best case and worst case: O(n)
    """
    hash_table = task1.HashTable(table_size, hash_base)

    try:
        start = time.time()
        load_dictionary(hash_table, filename, max_time)
        end = time.time()
        time_taken = end - start
    except Exception:
        time_taken = None
    return hash_table.count, time_taken


def table_load_dictionary_time(max_time):
    """
    This method loads the time taken, base used, and table_size used for each dictionary and write its to a csv file.

    :param max_time: max time allowed for loading the dictionary,
    :return: none
    :pre: none
    :post: csv file has been written into, with 4 columns consisting of the base used, the table_size, the dictionary
           and the time taken to load the dictionary
    :complexity: best and worst case: O(n^3), going through 3 for loops for the bases, sizes, and dictionaries
    """
    hash_bases = [1, 27183, 250726]
    table_sizes = [250727, 402221, 1000081]
    dictionaries = ["english_small.txt", "english_large.txt", "french.txt"]

    with open("output_task2.csv", "w") as f:
        dict_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for base in hash_bases:
            for size in table_sizes:
                for diction in dictionaries:
                    temp = load_dictionary_time(base, size, diction, max_time)
                    words_added = temp[0]
                    time_taken = temp[1]
                    if time_taken is None:
                        time_taken = "TIMEOUT"
                    dict_writer.writerow([diction, size, base, time_taken, words_added])
    f.close()


if __name__ == "__main__":
    table_load_dictionary_time(120)