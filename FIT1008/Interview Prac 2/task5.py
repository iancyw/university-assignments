# Ian Wong
# 30612616
# 25/09/2019
import task2
import task3


class Editor:
    def __init__(self):
        """
        Creates an empty ListADT as a instance variable called text_lines

        :return: none
        :pre: none
        :post: creates an empty ListADT, with no elements inside of size 40
        :complexity: best and worst case: O(1)
        """
        self.text_lines = task2.ListADT()

    def menu(self):
        """
        Creates an interface that takes commands from the users and calls the appropriate methods.

        :return: none
        :pre: none
        :post: appropriate method has been called according to the command, and self.text_lines has changed accordingly
        :complexity: best case: O(1), worst case: O(n), some methods from ListADT class are O(n) (such as .insert)
        """
        cmd = input()                               # reads the command line from the user
        if cmd.startswith("quit"):
            ed.quit()
        elif cmd.startswith("insert"):
            if len(cmd) == 6:                       # if len(cmd) == 6, there was no specified line number for insert
                print("?")
                return
            num = cmd.partition(" ")[2]             # partitions the cmd into a tuple, using space as the separator
            lines = task2.ListADT()                 # creates an empty ListADT for the strings being inputted

            complete = False                        # initialises complete to False at first
            while not complete:                     # runs until complete = True
                line = input()                      # takes line input from user
                if line == ".":                     # if line is "." by itself, complete set to true; nothing appended
                    complete = True
                else:
                    lines.append(line)              # any other line is appended to lines

            try:
                ed.insert_num_strings(num, lines)   # inserts strings into text_lines at specified line number
            except IndexError:
                print("?")                          # prints out ?, if there is an error

        elif cmd.startswith("print"):
            if len(cmd) == 5:                       # if len(cmd) == 5, no specified line number, prints all strings
                ed.print_num("")
            else:
                num = cmd.partition(" ")[2]         # num is 2nd position in partitioned tuple
                ed.print_num(num)                   # prints out the string at specified line number

        elif cmd.startswith("read"):
            file_name = cmd.partition(" ")[2]       # file_name is at 2nd position in partitioned tuple
            try:
                ed.read_filename(file_name)         # try reading the file into text_lines
            except FileNotFoundError:
                print("?")                          # if filename is not valid or its not found, prints ?

        elif cmd.startswith("delete"):
            if len(cmd) == 6:                       # if no specified line number, deletes everything
                try:
                    ed.delete_num("")
                except IndexError:
                    print("?")                      # if IndexError is raised, prints out ?
            else:
                num = cmd.partition(" ")[2]
                try:
                    ed.delete_num(num)
                except IndexError:
                    print("?")

        elif cmd.startswith("search"):
            if len(cmd) == 6:                       # if no specified line number, prints out ?
                print("?")
                return
            string = cmd.partition(" ")[2]
            for index in ed.search_string(string):
                print(index)                        # for index in the returned list, prints out the index

        else:
            print("?")                              # if the command is not recognized, prints out ?

    def insert_num_strings(self, num, string):
        """
        This method inserts a string at a specified line number

        :param num: number of the line where you wish to insert the string
        :param string: the string that is to be inserted into the text_lines
        :return: none
        :pre: num must be within bounds, num must not be 0, string must be a ListADT
        :post: string has been inserted into the ListADT, at the appropriate position indicated by num
        :complexity: best case: O(1), raises an IndexError; worst case: O(n), inserts an item at the beginning
        """
        if int(num) == 0:
            raise IndexError("Invalid index.")
        elif int(num) not in range(-(self.text_lines.length + 1), self.text_lines.length + 2):
            raise IndexError("Attempted to insert out of bounds.")

        elif int(num) > 0:
            i = 1
            for item in range(0, string.length):                    # for each item in the ListADT string, insert item
                self.text_lines.insert(int(num) - i, string[item])  # inserts at line_num - i
                i -= 1                                              # decreases i, moving the pointer one space up
        else:
            i = 1
            for item in range(0, string.length):
                self.text_lines.insert(int(num) + (self.text_lines.length + 1) - i, string[item])
                i -= 1

    def print_num(self, rest_string):
        """
        Prints out the specified strings in the list. if not specified, prints out all the strings

        :param rest_string: the line number of the string that is to be printed out
        :return: none
        :pre: rest_string must be within the bounds (the line number must exist and contain a string)
        :post: Raises an IndexError if the index was out of bounds
        :complexity: best and worst case: O(1)
        """
        if rest_string == "":
            print(self.text_lines)
        elif int(rest_string) not in range(self.text_lines.length):
            raise IndexError("Attempted to print out of bounds.")
        else:
            print(self.text_lines[int(rest_string) - 1])

    def read_filename(self, filename):
        """
        This method calls the function from Task3 and reads a file, putting the lines of the file self.text_lines

        :param filename: the name of text file that is being read
        :return: none
        :pre: file must exist in the same directory
        :post: text_lines is now a list consisting of strings from text file, raises a FileNotFoundError if no txt file
               file found with filename
        :complexity: best and worst case: O(n)
        """
        self.text_lines = task3.read_text_file(filename)

    def delete_num(self, rest_string):
        """
        This method deletes a string at a specified line number given by rest_string. del all strings if not specified

        :param rest_string: line number of the string that is to be deleted
        :return: none
        :pre: text_lines must have something in it, the line number specified is not 0, the line number is within range
        :post: deletes the item at the specified line number, raises an IndexError if pre conditions are not met
        :complexity: best case: O(1); worst case: O(n), deleting the first index, causing everything to shift down
        """
        if self.text_lines.is_empty():
            raise IndexError("Attempted to delete from empty list.")
        if rest_string == "":
            self.text_lines = task2.ListADT()

        elif int(rest_string) == 0:
            raise IndexError("Invalid Index")
        elif int(rest_string) not in range(-self.text_lines.length, self.text_lines.length + 1):
            raise IndexError("Attempted to delete outside of bounds.")
        else:
            self.text_lines.delete(int(rest_string) - 1)

    def search_string(self, string):
        """
        This method searches all strings in the list for a substring, and returns the indexes of those strings that
        contains the substring

        :param string: the substring that is being searched for
        :return: returns a list of indexes of the strings that contain the substring
        :pre: none
        :post: none
        :complexity: best case: O(1), no strings in list; worst case: O(n^2) searches through all the items and iterates
                     through all the letters of the items
        """
        line_lst = task2.ListADT()
        lines = self.text_lines

        for line in range(0, lines.length):                 # for each string in the text_lines
            j = 0
            k = 0
            i = 0
            check = True

            while check:                                    # keeps running while check is True
                if lines[line][j + i] == string[k]:         # if letter of string is equal to letter line
                    if k == len(string) - 1:                # checks if it's the last letter of string
                        line_lst.append(line + 1)           # if it's the last letter that means the substring is there
                        check = False                       # don't need to check the rest of the string; check = False
                    elif (j + i) == len(lines[line]) - 1:   # current letter is the last letter of line; check = False
                        check = False
                    i += 1                                  # increases displacement of j
                    k += 1                                  # increases k counter (letter of string)
                else:
                    if j == len(lines[line]) - 1:           # checks if it's the last letter of line
                        check = False                       # check = False
                    k = 0                                   # resets k, starts comparing from first letter of string
                    i = 0                                   # resets i, displacement has been reset
                    j += 1                                  # check if there is a substring from the next letter of line

        return line_lst                                     # returns the list of indexes that contain substring

    def quit(self):
        """
        This method quits out of the program

        :return: none
        :pre: none
        :post: the program has been quit out of
        :complexity: best and worst case: O(1)
        """
        quit()


def test_insert_num_strings():
    """Testing function for insert_num_strings method of Editor class"""
    ed = Editor()
    val = task2.ListADT()
    val.append("This is a line.")
    ed.insert_num_strings("1", val)     # Testing append in front
    assert ed.text_lines == val
    ed.insert_num_strings("-1", val)
    val.append("This is a line.")       # Testing append using negative index
    assert ed.text_lines == val

    ed = Editor()
    val = task2.ListADT()
    val.append("This is a line 1.")
    val.append("This is a line 2.")
    val.append("This is a line 3.")
    ed.insert_num_strings("1", val)
    assert ed.text_lines.the_array == val.the_array


def test_delete_num():
    """Testing function for delete_num method of Editor class"""
    ed = Editor()
    val = task2.ListADT()
    val.append("This is a line 1.")
    val.append("This is a line 2.")
    val.append("This is a line 3.")
    ed.insert_num_strings("1", val)
    assert ed.text_lines.the_array == val.the_array     # checks if the values have been added correctly

    ed.delete_num("-1")
    assert ed.text_lines.length == 2


if __name__ == "__main__":
    test_insert_num_strings()
    test_delete_num()
    ed = Editor()
    while True:
        ed.menu()