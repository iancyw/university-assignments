def bubble_sort(the_list):
    """
    This program sorts a list using the bubble sorting algorithm
    :param the_list: a list of elements in any order
    :return: returns a sorted list in increasing order
    :complexity: O(n^2), where n is the length of the list
    """
    n = len(the_list)
    for a in range(n-1):  # n - 1, as one element does not need to be sorted
        for i in range(n-1):  # iterates through each number, ensuring the last number is always the largest
            item = the_list[i]  # sets item as current i
            item_to_right = the_list[i+1]  # sets item_to_right, as the value one index over from item
            if item > item_to_right:  # executes only if item > item_to_right, otherwise the pointer moves to the next number and compares
                the_list[i] = item_to_right  # the number that was on the right swaps pos with the item
                the_list [i+1] = item  # the item moves over one space to the right
