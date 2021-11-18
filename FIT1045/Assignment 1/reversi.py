import copy


# new_board (0 = EMPTY, 1 = BLACK, 2 = WHITE)
def new_board():
    return [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]


# score (counts each square in the matrix and increases counters. returns number of blacks and number of whites)
def score(board):
    black_count = 0
    white_count = 0
    for i in board:
        for j in i:
            if j == 2:
                white_count += 1
            if j == 1:
                black_count += 1
    return black_count, white_count


# print_board (prints out the current board in text format)
def print_board(board):
    row_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    h_line = ' +───+───+───+───+───+───+───+───+ '
    print('\n')
    print(h_line)
    for i in range(len(board)):
        print(str(row_numbers[i]) + '| ' + str(board[i][0]) + ' | ' + str(board[i][1]) + ' | ' + str(board[i][2]) +
              ' | ' + str(board[i][3]) + ' | ' + str(board[i][4]) + ' | ' + str(board[i][5]) + ' | ' + str(board[i][6])
              + ' | ' + str(board[i][7]) + ' | ')
        print(h_line)
    print('   a   b   c   d   e   f   g   h')


# enclosing
def enclosing(board, player, pos, direct):
    n = len(board)
    pos_i = pos[0]
    pos_j = pos[1]
    pos_lst = [0, 1, 2, 3, 4, 5, 6, 7]
    count_1 = 0
    count_2 = 0
    if player == 1:
        for i in range(n):
            pos_i += direct[0]
            pos_j += direct[1]
            if pos_i not in pos_lst or pos_j not in pos_lst:
                return False
            if board[pos_i][pos_j] == 2:
                count_2 += 1
            if board[pos_i][pos_j] == 1 and count_2 == 0:
                return False
            if board[pos_i][pos_j] == 1 and count_2 > 0:
                return True
            elif board[pos_i][pos_j] == 0:
                return False
    if player == 2:
        for i in range(n):
            pos_i += direct[0]
            pos_j += direct[1]
            if pos_i not in pos_lst or pos_j not in pos_lst:
                return False
            if board[pos_i][pos_j] == 1:
                count_1 += 1
            if board[pos_i][pos_j] == 2 and count_1 == 0:
                return False
            if board[pos_i][pos_j] == 2 and count_1 > 0:
                return True
            elif board[pos_i][pos_j] == 0:
                return False


# valid_moves (for the current player, checks all squares in the matrix and uses enclosing() for a list of directions to
# decide whether or not the square is a valid move, returns a list of valid moves)
def valid_moves(board, player):
    n = len(board)
    lst = []
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    if player == 1:
        for d in directions:
            for i in range(n):
                for j in range(n):
                    if enclosing(board, player, (i, j), d) and board[i][j] == 0 and (i, j) not in lst:
                        lst.append((i, j))
    if player == 2:
        for d in directions:
            for i in range(n):
                for j in range(n):
                    if enclosing(board, player, (i, j), d) and board[i][j] == 0 and (i, j) not in lst:
                        lst.append((i, j))
    return lst


# flip1 (flips pieces for player 1)
def flip1(board, pos, direct):
    n = len(board)
    pos_i = pos[0]
    pos_j = pos[1]
    flipped_tiles = 0
    for i in range(n):
        pos_i += direct[0]
        pos_j += direct[1]
        if pos_i > 7 or pos_i < 0:
            return False
        if pos_j > 7 or pos_j < 0:
            return False
        if board[pos_i][pos_j] == 2:
            flipped_tiles += 1
            board[pos_i][pos_j] = 1
        elif board[pos_i][pos_j] == 1:
            return board, flipped_tiles


# flip2 (flips pieces for player 2)
def flip2(board, pos, direct, flip=0):
    n = len(board)
    pos_i = pos[0]
    pos_j = pos[1]
    flipped_tiles = 0
    for i in range(n):
        pos_i += direct[0]
        pos_j += direct[1]
        if pos_i > 7 or pos_i < 0:
            return False
        if pos_j > 7 or pos_j < 0:
            return False
        if board[pos_i][pos_j] == 1:
            flipped_tiles += 1
            if flip == 1:
                continue
            else:
                board[pos_i][pos_j] = 2
        elif board[pos_i][pos_j] == 2:
            return board, flipped_tiles


# next_state (for the current player, checks the pos using enclosing() for all directions to check if it's a valid move.
# if it is a valid move, flip1 or flip2 will flip the corresponding pieces inbetween the pos and the current player's
# other piece)
def next_state(board, player, pos):
    current_board = copy.copy(board)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    if player == 1:
        current_board[pos[0]][pos[1]] = 1
        for d in directions:
            if enclosing(current_board, player, pos, d):
                current_board = flip1(current_board, pos, d)[0]
        return current_board, 2
    if player == 2:
        current_board[pos[0]][pos[1]] = 2
        for d in directions:
            if enclosing(current_board, player, pos, d):
                current_board = flip2(current_board, pos, d)[0]
        return current_board, 1


# position (turns strings into positions on the board)
def position(string):
    split_string = list(string)
    rows = ['1', '2', '3', '4', '5', '6', '7', '8']
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = 0
    col = 0
    for i in rows:
        if split_string[1] == i:
            row = rows.index(i)
        elif split_string[1] not in rows:
            return None
    for j in columns:
        if split_string[0] == j:
            col = columns.index(j)
        elif split_string[0] not in columns:
            return None
    return row, col


# run_two_players() (runs a two player game of reversi)
def run_two_players():
    board = new_board()
    print_board(board)
    print("Player 1 tile = 1 | Player 2 tile = 2")
    flag = 1
    player = 1
    while flag == 1:
        pos_flag = 1
        while pos_flag == 1:
            user_input = input("Player " + str(player) + ", enter a position: ")
            if user_input == "q":
                print("Player " + str(player) + " has quit! The score is " + str(score(board)))
                return
            elif len(user_input) != 2:
                print("Invalid move")
                continue
            pos = position(user_input)
            if pos in valid_moves(board, player):
                pos_flag = 0
            elif pos not in valid_moves(board, player):
                print("Invalid move")
        board = next_state(board, player, pos)[0]
        player = next_state(board, player, pos)[1]
        print_board(board)
        if valid_moves(board, player) == []:
            print("Player " + str(player) + "has no valid moves.")
            if player == 1:
                player = 2
            if player == 2:
                player = 1
        if valid_moves(board, 1) == [] and valid_moves(board, 2) == []:
            print("The game is finished! The score is", score(board))
            break


# run_single_player() (runs a one player game of reversi)
def run_single_player():
    board = new_board()
    print_board(board)
    print("Player 1 tile = 1 | Player 2 tile = 2")
    flag = 1
    player = 1
    while flag == 1:
        if player == 1:
            pos_flag = 1
            while pos_flag == 1:
                user_input = input("Player " + str(player) + ", enter a position: ")
                if user_input == "q":
                    print("Player " + str(player) + " has quit! The score is " + str(score(board)))
                    return
                elif len(user_input) != 2:
                    print("Invalid move")
                    continue
                pos = position(user_input)
                if pos in valid_moves(board, player):
                    pos_flag = 0
                elif pos not in valid_moves(board, player):
                    print("Invalid move")
            board = next_state(board, player, pos)[0]
            player = next_state(board, player, pos)[1]
            print_board(board)
            if valid_moves(board, 2) == []:
                print("Player 2 has no valid moves.")
                player = 1
            if valid_moves(board, 1) == [] and valid_moves(board, 2) == []:
                print("The game is finished! The score is", score(board))
                break
        if player == 2:
            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
            max_flipped = 0
            max_pos = 0
            for i in valid_moves(board, 2):
                pos = i
                flipped = 0
                for j in directions:
                    if enclosing(board, 2, pos, j):
                        flipped += flip2(board, pos, j, 1)[1]
                if flipped > max_flipped:
                    max_flipped = flipped
                    max_pos = pos
            board = next_state(board, 2, max_pos)[0]
            player = next_state(board, 2, max_pos)[1]
            print("The computer is making it's move...")
            print_board(board)
            print("The computer has made it's move.")
            if valid_moves(board, 1) == []:
                print("Player 1 has no valid moves.")
                player = 2
            if valid_moves(board, 1) == [] and valid_moves(board, 2) == []:
                print("The game is finished! The score is", score(board))
                break

run_two_players()