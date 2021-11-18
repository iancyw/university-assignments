class TrieNode:
    def __init__(self, item=None):
        self.item = item
        self.children = []
        self.wordcount = 0
        self.word = ""

class Trie:
    def __init__(self, text):
        """
        This method initialises a Trie object using a list of strings
        :param text: a list of strings which will be composed only of lowercase English alphabet characters
        :complexity: O(T), with T being the total number of characters over all strings in the list
        """
        self.root = TrieNode()                      # creates an empty root node
        if not text:
            exit()
        for string in text:                         # inserts strings from text
            current = self.root                     # starts inserting a string from the root node of the Trie
            for char in string:                     # for each char, check for char in children of current node
                found = False
                for child in current.children:      # iterates through children in current node
                    if child.item == char:          # if char matches the item in child node
                        current = child             # set child as the current node
                        current.wordcount += 1      # indicates how many times this prefix has been gone through
                        found = True                # found set to True, as we found a match
                        break                       # break out of loop so we don't check other children
                if not found:                       # if no child matches char, create a new node and append to children
                    new = TrieNode(char)            # create new node for current char
                    new.wordcount += 1              # increase wordcount by 1 for this prefix
                    new.word = ''.join((current.word, char))
                    current.children.append(new)    # append to current node's children
                    current = new                   # set pointer to new node

            finished = False
            for child in current.children:          # for children in the last character of the string
                if child.item == "$":               # if one of the children is $, increase wordcount by 1
                    current = child                 # set current to child
                    current.wordcount += 1          # increase wordcount by 1
                    finished = True                 # set finished to True
                    break                           # break out of the loop
            if finished is False:                   # if finished == False, then first instance of word, create new node
                finish_node = TrieNode("$")         # create new node
                finish_node.wordcount += 1          # sets wordcount to 1
                finish_node.word = ''.join((current.word, ''))
                current.children.append(finish_node)    # appends to children

    def string_freq(self, query_str):
        """
        This method returns the number of elements in the text which are exactly query_string.
        :param query_str: non_empty string consisting only of lowercase letters
        :return: returns the number of elements in the Trie which are exactly query_string
        :complexity: O(q), where q is the length of query_str
        """
        current = self.root                 # sets current node to the root
        for char in query_str:              # for each char in query_str, see if there is a node that matches
            found = False
            for child in current.children:  # for child in the current node
                if child.item == char:      # if child == char
                    current = child         # set current node to child
                    found = True            # we have found a match set to true
                    break                   # break out of loop so we don't iterate over other children
            if not found:                   # if there has been no child found that matches char, return 0
                return 0

        for child in current.children:      # searches children of the last char
            if child.item == "$":           # if end of word found
                return child.wordcount      # return the number of exact words that match query_str
        return 0                            # else, word is not in Trie, return 0

    def prefix_freq(self, query_str):
        """
        This method returns the number of words in the Trie that have query_str as a prefix
        :param query_str: possibly empty string, wi
        :return: returns the number of words that have a prefix that matchs query_str
        :complexity: O(q), where q is the length of query_str
        """
        current = self.root                 # sets current node to the root
        for char in query_str:              # for each char in query_str, see if there is a node that matches
            found = False
            for child in current.children:  # for child in the current node
                if child.item == char:      # if child == char
                    current = child         # set current node to child
                    found = True            # we have found a match set to true
                    break                   # break out of loop so we don't iterate over other children
            if not found:
                return 0                    # prefix was not in the Trie
        return current.wordcount            # return the wordcount of prefix

    def __prefix_search__(self, prefix):
        """
        This method is used to return all the strings that have matching prefixes
        :param prefix: a string consisting only of lowercase letters
        :return: returns a list of strings that have matching prefixes to the param prefix
        :complexity: O(s), where S is the total number of characters in the strings that have matching prefixes
        """
        current = self.root
        # this block is used to get to the end of the prefix. e.g. where we start searching for the strings
        for char in prefix:                             # for character in the prefix, traverse the trie
            found = False
            for child in current.children:              # for each child in the current node
                if child.item == char:                  # if node == char
                    current = child                     # set current node to child
                    found = True                        # found set to true
                    break                               # break out of loop so we don't iterate over other children
            if not found:
                return []

        res_list = []
        stack = [current]                               # initialises the stack with the end of the prefix
        while stack:                                    # while loop continues until stack is empty
            current = stack.pop()                       # pop() is O(1) time; pops off a child from the stack

            if current.item == "$":                     # if node is $, we have reach the end of the word
                for i in range(current.wordcount):      # appends how many times this word has appeared in this text
                    res_list.append(current.word)       # appends the whole word to res_lst

            for child in current.children:              # if node is not $; haven't reached end of word, keep going
                stack.append(child)                     # appends all the children
        return res_list                                 # returns res_lst

    def wildcard_prefix_freq(self, query_str):
        """
        This method returns all the strings in the text given a prefix with a single wildcard.
        :param query_str: a non-empty string consisting of lowercase letters and exactly one '?' character, anywhere
        :return: returns a list containing all the strings which have a prefix which matches query_str
        :complexity: O(q + S), where q is the length of query_str, and s is the total number of characters with matching
                     prefixes
        """
        current = self.root                                 # sets current as the root node
        res_lst = []
        prefix_lst = []                                     # list of prefixes; prefixes that don't exist return nothing
        wildcard = False                                    # wildcard flag; after wildcard has been used
        res = ''                                            # used to store the result before wildcard has been met

        for char in query_str:                              # for char in initial query_str; O(q)
            if char == "?":                                 # if char is "?"; joins res to all children of current
                for c in current.children:                  # for each child in current: worst case O(1)
                    if c.item != "$":                       # if the item is not "$"; not end of word
                        pref = ''.join((res, c.item))       # joins existing prefix to new char
                        prefix_lst.append(pref)             # appends to prefix list
                        wildcard = True                     # wildcard set to True
            else:
                if wildcard:                                # if wildcard has been encountered; only need to add char
                    for i in range(len(prefix_lst)):
                        prefix_lst[i] = ''.join((prefix_lst[i], char))
                else:                                       # if wildcard has not been encountered; add char to res
                    for c in current.children:              # for child in current
                        if c.item == char:                  # if the node == char
                            current = c                     # set current node to child
                            res = ''.join((res, c.item))    # appends the char to res
                            break                           # breaks out of the loop so we don't iterate over the rest

        for p in prefix_lst:                                # for each prefix in the prefix_lst; worst-case O(1)
            lst = self.__prefix_search__(p)                 # list of all the strings that have matching prefixes; O(S)
            for i in lst:                                   # for each string, append it to the res_lst
                res_lst.append(i)

        return res_lst


if __name__ == "__main__":
    empty = []
    text = ["example_string", "another_example", "exam"]
    text1 = ["aa", "aab", "aaab", "abaa", "aa", "abba", "aaba", "aaa", "aa", "aaab", "abbb", "baaa", "baa", "bba"]
    student_trie = Trie(text1)
    print(student_trie.string_freq("aa"))
    print(student_trie.prefix_freq("aa"))
    print(student_trie.wildcard_prefix_freq("aa?"))
