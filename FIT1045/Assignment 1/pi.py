from math import pi
from math import sqrt


# basel
def basel(precision):
    basel_n = 0  # number of terms processed
    basel_x = 0  # sum of the sequence of 1/n**2
    basel_approximation = 0  # isolating the pi by itself
    while abs(pi - basel_approximation) > precision:  # this loop runs until pi - basel_approximation < precision
        basel_n += 1
        basel_x += 1 / basel_n ** 2
        basel_approximation = sqrt(6 * basel_x)
    return basel_approximation, basel_n  # returns basel approximation of pi and the number of terms


# taylor
def taylor(precision):
    taylor_count = 1  # counts the number of terms needed
    taylor_x = 1  # represents 1/x, every time a term is added x is increased by 2
    taylor_sum = 1  # sum of the 1/x chain
    taylor_approximation = 0  # isolating the pi by itself by moving around terms
    while abs(pi - taylor_approximation) > precision:
        # loops runs until taylor - pi < precision (as pi - taylor is negative) and it is not a negative term
        taylor_count += 1  # increases the number of terms
        taylor_x += 2  # increases the x in 1/x
        if taylor_count % 2 == 0:  # if it's an odd term, it subtracts 1/x from the sum
            taylor_sum -= 1 / taylor_x
            taylor_approximation = 4 * taylor_sum  # updates the taylor_approximation to check if the loop should cont.
        else:
            taylor_sum += 1 / taylor_x  # otherwise if the term is odd, it adds 1/x to the sum
            taylor_approximation = 4 * taylor_sum  # updates the taylor_approximation
    return taylor_approximation, taylor_count  # once loop breaks, returns the taylor approximation and number of terms


# wallis
def wallis(precision):
    wallis_count = 1  # counts the number of terms needed
    wallis_sum = 4 / 3  # represents the sum of the series
    wallis_approximation = 0  # isolating pi by itself by moving around terms
    while abs(pi - wallis_approximation) > precision:  # loop runs until this condition is false
        wallis_count += 1  # increase the number of terms by 1
        wallis_sum = wallis_sum * (((2 * wallis_count) ** 2) / ((2 * wallis_count - 1) * (2 * wallis_count + 1)))
        wallis_approximation = 2 * wallis_sum  # updates the approximation
    return wallis_approximation, wallis_count


# spigot
def spigot(precision):
    spigot_count = 1  # number of terms needed
    numerator = 1  # separate counter for numerator
    denominator = 3  # separate counter for denominator
    previous_term = 1  # previous term(s) that we then multiply with current term
    spigot_sum = 1  # the sum of the series
    spigot_approximation = 0  # isolating pi by itself
    while abs(pi - spigot_approximation) > precision:  # loop runs until this is false
        spigot_count += 1  # increases the number of terms
        spigot_sum += previous_term * (numerator / denominator)  # previous term multiplied by current num and denom
        previous_term *= (numerator / denominator)  # updating the new previous terms
        numerator += 1  # increasing numerator counter by 1
        denominator += 2  # increasing denominator counter by 2
        spigot_approximation = 2 * spigot_sum  # updates the approximation
    return spigot_approximation, spigot_count


# second function to be used in race function (takes second element of tuple when used as the key for sorted())
def second(x):
    return x[1]


# race
def race(precision, algorithms):
    race_list = []  # empty list for the algorithm steps and n
    count = 1  # counter for the term number
    for i in algorithms:  # iterates through all the terms in algorithms
        if i == basel:
            race_list.append((count, basel(precision)[1]))  # appends current count and algorithm steps
            count += 1  # increase count by 1
        if i == taylor:
            race_list.append((count, taylor(precision)[1]))  # appends current count and algorithm steps
            count += 1  # increase count by 1
        if i == wallis:
            race_list.append((count, wallis(precision)[1]))  # appends current count and algorithm steps
            count += 1  # increase count by 1
        if i == spigot:
            race_list.append((count, spigot(precision)[1]))  # appends current count and algorithm steps
            count += 1  # increase count by 1
    sorted_race_list = sorted(race_list, key=second)  # sorts the list of tuples by the second element in the tuple
    return sorted_race_list  # return the sorted race list


# print_results
def print_results(sorted_race_list):
    algorithm_numbers = [i[0] for i in sorted_race_list]  # records the first element of the tuples, which is the order
    algorithm_steps = [i[1] for i in sorted_race_list]  # records the second element of the tuples, which is steps
    for i in range(len(sorted_race_list)):
        print("Algorithm " + str(algorithm_numbers[i]) + " finished in " + str(algorithm_steps[i]) + " steps.")

