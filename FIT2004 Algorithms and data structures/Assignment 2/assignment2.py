# Task 1
def longest_oscillation(L):
    """
    This function finds the longest oscillation in a given list. Function has been implemented optimally
    :param L: list of integers
    :return: tuple containing the length of the longest oscillation and the indices in L at which it occurs
    :complexity: time complexity = O(N), space complexity = O(N).
    """
    n = len(L)
    if n < 1:               # returns (0, []) if an empty list
        return 0, []

    memo_up = [0] * n       # memo for longest osc in L[0..i], where L[i] > L[i - 1]; time = O(n), space = O(n)
    memo_down = [0] * n     # memo for longest osc in L[0..i], where L[i] < L[i - 1]; time = O(n), space = O(n)
    memo_up[0] = memo_down[0] = 1   # base cases, where osc L[0..0] is length 1

    for i in range(1, n):   # iterates through list; time = O(n), space = O(1)
        j = i - 1
        if L[j] < L[i]:     # if L[i] > L[j], then longest osc up with small element until i is memo_down[i - 1]. add 1
            memo_up[i] = memo_down[i - 1] + 1
            memo_down[i] = memo_down[i - 1]
        elif L[j] > L[i]:   # if L[i] < L[j], then longest osc up with large element until i is memo_up[i - 1]. add 1
            memo_down[i] = memo_up[i - 1] + 1
            memo_up[i] = memo_up[i - 1]
        else:               # if L[i] == L[j], then do nothing
            memo_down[i] = memo_down[i - 1]
            memo_up[i] = memo_up[i - 1]

    lst = []
    up = 1                              # initialises first up as len of 1, as L[0..1] is always len 1
    down = 1                            # initialises first down as len of 1, as L[0..1] is always len 1
    s1 = 0                              # initialises saved value 1 to be 0, as 0 index is always part of soln
    s2 = 0                              # initialises saved value 2 to be 0.
    for i in range(1, n):               # checks memo lists to see where they have changed; time = O(n), space = O(n)
        # if current length does not match with saved length up, that means a larger element was found.
        if memo_up[i] != up:
            up = memo_up[i]             # new longest osc len that ends with large element
            lst.append(s2)              # appends the previous element that is smaller
            s1 = s2 = i                 # saves the current element
        # if current length does not match with saved length down, that means a smaller element was found.
        elif memo_down[i] != down:
            down = memo_down[i]         # new longest osc len that ends with small element
            lst.append(s2)              # appends the previous element that is larger
            s1 = s2 = i                 # saves the current element
        # if there has been no change, the element was either larger when we were looking for a smaller element, or it
        # was smaller when we were looking for a larger element. we take the smallest/largest element.
        else:
            s2 += 1
    lst.append(s1)                      # if there had been no change after the loop, appends the saved element
    return max(memo_down[n - 1], memo_up[n - 1]), lst   # returns the longest oscillation length and the indices


# Task 2
def valid_position(M, i, j):
    """
    This function determines if a given position is valid on the matrix given.
    :param M: matrix of numbers
    :param i: row number
    :param j: column number
    :return: returns True, if position is valid; returns False, if position is invalid
    :complexity: time complexity = O(1)
    """
    if (i >= len(M) or i < 0) or (j >= len(M[0]) or j < 0):
        return False
    return True


def longest_walk(M):
    """
    This function returns the longest increasing walk in a matrix
    :param M: matrix of numbers
    :return: returns a tuple containing the longest walk length and the row-column coordinates of the element of M that
             make up the longest increasing walk
    :complexity: space complexity: O(nm); time complexity: O(nm log(nm)), Sub-optimal implementation.
    """
    def longest_path_index(M, i, j):
        """
        This function returns the longest path at M[i][j]
        :param M: matrix of numbers
        :param i: row number
        :param j: column number
        :return: returns the max walk length for that index
        :complexity: time complexity = O(log(nm)), as it saves solved solns into dp table, finds solved solns in O(1)
        """
        if memo[i][j] != -1:            # checks if solution has been found
            return memo[i][j]
        else:                           # else finds the longest path for that index
            max_length = 1              # initialise max length of path to 1
            for direct in directions:   # iterates through number of directions; O(1) constant time
                row = i + direct[0]
                column = j + direct[1]

                if valid_position(M, row, column) and M[row][column] > M[i][j]:  # if valid_position and increasing
                    path_len = 1 + longest_path_index(M, row, column)     # finds longest path; saves time with dp table
                    max_length = max(path_len, max_length)
            memo[i][j] = max_length     # saves the longest path length for this index into memo
            return max_length           # returns path length

    n = len(M)
    if n < 1:               # if empty list, return (0, [])
        return 0, []
    elif n == 1:            # if matrix of size 1, return (1, [(0,0)])
        return 1, [(0, 0)]
    else:
        max_walk_len = 0
        memo = [[-1 for _ in range(n)] for _ in range(len(M[0]))]       # creates a matrix of size nm
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]     # 8 directions

        for i in range(n):                              # iterates through rows
            for j in range(n):                          # iterates through columns
                walk_len = longest_path_index(M, i, j)  # finds the longest increasing walk
                if walk_len > max_walk_len:
                    max_walk_len = walk_len
                    coords = i, j                       # finds the index that correspond to longest increasing walk

        res = max_walk_len
        path = [(coords[0], coords[1])]                 # initialises path
        while res != 1:                                 # while it has not reached the end of the path loop continues
            current_max = 0
            for direct in directions:
                row = coords[0] + direct[0]
                column = coords[1] + direct[1]

                if valid_position(M, row, column) and memo[row][column] < memo[coords[0]][coords[1]]:
                    if memo[row][column] > current_max:     # chooses the longest path that is smaller than current
                        current_max = memo[row][column]     # sets current_max to longest path that is smaller
                        current_coords = row, column        # remembers the coords for current_max

            path.append((current_coords[0], current_coords[1]))     # appends the coords for current_max
            res = current_max                                       # sets current_max to res
            coords = current_coords                                 # set coords to saved coords of current_max

    return max_walk_len, path


if __name__ == "__main__":
    L = [1, 5, 7, 4, 6, 8, 6, 7, 1]
    L1 = [1, 2, 3]
    L2 = [1, 1, 1, 1]
    L3 = [1, 2]
    L4 = [1, 5, 7, 6]
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    M1 = [[4, 6],
          [7, 2]]
    M2 = [[1, 2, 3],
          [1, 2, 1],
          [2, 1, 3]]
    print(longest_oscillation(L))
    print(longest_walk(M))