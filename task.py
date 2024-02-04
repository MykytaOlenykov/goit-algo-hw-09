def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        result[coin_used[amount]] = result.get(coin_used[amount], 0) + 1
        amount -= coin_used[amount]

    return result


if __name__ == "__main__":
    amount = 113
    print("Greedy Algorithm:", find_coins_greedy(amount))
    print("Dynamic Programming Algorithm:", find_min_coins(amount))
