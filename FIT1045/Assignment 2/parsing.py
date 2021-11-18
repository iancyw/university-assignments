from math import pow


# tokenization
def tokenization(expr):
    i = 0
    n = len(expr)
    operators = ['(', ')', '+', '-', '/', '*', '^']
    lst = []
    while i < n:
        if expr[i] in operators:
            lst.append(expr[i])
            i += 1
        elif expr[i].isdigit():
            num = expr[i]
            i += 1
            num_flag = 1
            while num_flag == 1:
                try:
                    if expr[i] == '.':
                        num += expr[i]
                        i += 1
                    elif expr[i].isdigit():
                        num += expr[i]
                        i += 1
                    elif expr[i] in operators or expr[i] == ' ':
                        lst.append(float(num))
                        num_flag = 0
                except IndexError:
                    lst.append(float(num))
                    num_flag = 0
        elif expr[i] == ' ':
            i += 1
    return lst


# has_precedence
def has_precedence(op1, op2):
    operators = ['+', '-', '*', '/', '^']
    operator_val = [1, 1, 2, 2, 3]
    i_1 = operators.index(op1)
    i_2 = operators.index(op2)
    if operator_val[i_1] > operator_val[i_2]:
        return True
    return False


# simple_evaluation
def simple_evaluation(tokens):
    if len(tokens) == 1:
        return tokens[0]
    else:
        operators = ['+', '-', '*', '/', '^']
        op_pos = []
        op = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                op_pos.append(i)
                op.append(tokens[i])

        def does_something_have_precedence(lst):
            for a in lst:
                for b in lst:
                    if has_precedence(a, b) is True:
                        return True
                    else:
                        continue
            return False

        while len(op_pos) != 1 and does_something_have_precedence(op) is True:
            for p in op_pos:
                for q in op_pos:
                    if has_precedence(tokens[p], tokens[q]) is True:
                        op_pos.remove(q)
                        op.remove(tokens[q])
        op = tokens[op_pos[0]]
        if op == '^':
            result = pow(tokens[op_pos[0] - 1], tokens[op_pos[0] + 1])
        if op == '*':
            result = tokens[op_pos[0] - 1] * tokens[op_pos[0] + 1]
        if op == '/':
            try:
                result = tokens[op_pos[0] - 1] / tokens[op_pos[0] + 1]
            except ZeroDivisionError:
                print('Division by zero. Error.')
                quit()
        if op == '+':
            result = tokens[op_pos[0] - 1] + tokens[op_pos[0] + 1]
        if op == '-':
            result = tokens[op_pos[0] - 1] - tokens[op_pos[0] + 1]
        del tokens[op_pos[0] - 1: op_pos[0] + 2]
        tokens.insert(op_pos[0] - 1, result)
        return simple_evaluation(tokens)


# complex_evaluation
def complex_evaluation(tokens):
    brackets = ['(', ')']
    br_pos = []
    br = []
    for i in range(len(tokens)):
        if tokens[i] in brackets:
            br_pos.append(i)
            br.append(tokens[i])
    if br == []:
        return simple_evaluation(tokens)
    else:
        i = 0
        flag = 1
        while flag == 1:
            if br[i] == '(':
                if br[i+1] == ')':
                    result = simple_evaluation(tokens[br_pos[i] + 1: br_pos[i + 1]])
                    del tokens[br_pos[i]: br_pos[i+1] + 1]
                    tokens.insert(br_pos[i], result)
                    return complex_evaluation(tokens)
            i += 1


# evaluation
def evaluation(string):
    tokened_string = tokenization(string)
    complex_flag = 0
    for token in tokened_string:
        if token == '(' or token == ')':
            complex_flag = 1
    if complex_flag == 1:
        return complex_evaluation(tokened_string)
    return simple_evaluation(tokened_string)
