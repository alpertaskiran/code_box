'''
It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of
length n, where costs[i] is the price of the ith ice cream bar in coins.
The boy initially has coins coins to spend, and he wants to buy as many ice cream
bars as possible.Note: The boy can buy the ice cream bars in any order.
Return the maximum number of ice cream bars the boy can buy with coins coins.
You must solve the problem by counting sort.
'''


def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    for i, cost in enumerate(costs):
        coins -= cost
        if coins < 0:
            return i
    return len(costs)
