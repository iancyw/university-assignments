from math import inf


def bottom_up_coin_change(c, V):
    min_coins = [inf] * (V + 1)
    min_coins[0] = 0
    for value in range(1, V + 1):
        options = []
        for coin in c:
            if value >= coin:
                options.append(min_coins[value - coin])
        min_coins[value] = min(options) + 1
    return min_coins[V]

def top_down_coin_change(c, V, min_coins):
    if V = 0:
        return 0
    else:
        if min_coins[V] == -1:
            min_val = inf
            for coin in c:
                if coin <= V:
                    min_val = min(min_coins, 1 + top_down_coin_change(V - coin))
            min_coins[V] = min_val
        return min_coins[V]

if __name__ == "__main__":
    min_coins
    print(bottom_up_coin_change([9, 5, 6, 1], 12))