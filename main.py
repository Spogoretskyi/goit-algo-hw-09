def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1]

    result = {}
    remaining_amount = amount

    for denomination in denominations:
        if remaining_amount >= denomination:
            num_coins = remaining_amount // denomination
            result[denomination] = num_coins
            remaining_amount %= denomination

    return result


def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 20, 50]

    dp_table = [float("inf")] * (amount + 1)
    dp_table[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in denominations:
        for i in range(coin, amount + 1):
            if dp_table[i - coin] + 1 < dp_table[i]:
                dp_table[i] = dp_table[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result
