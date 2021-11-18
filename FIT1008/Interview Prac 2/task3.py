# Ian Wong
# 30612616
# 17/09/2019
import task2


def read_text_file(name):
    """
    This function reads the lines of a file and appends to a ListADT, then returns a list of strings.

    :param name: name of the text file
    :pre: name of text file is a string and refers to an actual file in the folder location of the python file
    :post: none
    :return: returns a list of strings
    :complexity: best and worst case: O(n), reading every line of the file
    """
    with open(name) as f:
        my_list = task2.ListADT()
        for line in f:
            my_list.append(line.strip())
    f.close()
    return my_list


if __name__ == "__main__":
    text_file = read_text_file("small.txt")

