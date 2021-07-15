"""
arr = [1, 2, 3]
power_set(arr) = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
2^n elements in the power set of a set of n elements


KnapSack -> You have a knapsack to carry products for selling. It holds up to a
certain weight, not enough to carry all your products - you must choose which one
to carry. Knowing the weight and value of each product, which choice of
products gives you the highest value?

We facilitate the idea of power sets because in that way we get all possible pairs.
A brute force approach simply checks these selections in a for loop. Making sure
we don't surpass the max_weight capacity and maximize the value by choosing the
set which has highest value.

"""


def power_set(arr):
    result = [[]]
    for el in arr:
        newsubsets = [subset + [el] for subset in result]
        result.extend(newsubsets)
    return result


def total_weight(cand):
    sum = 0
    for el in cand:
        sum += el.get("weight")
    return sum


def sales_value(cand):
    value = 0
    for el in cand:
        value += el.get("value")
    return value


def knapsack(items, max_weight):
    best_value = 0

    for candidate in power_set(items):
        if total_weight(candidate) <= max_weight:
            if sales_value(candidate) > best_value:
                best_value = sales_value(candidate)
                best_candidate = candidate

    return best_candidate


if __name__ == '__main__':
    items = [
        {"weight": 10,
         "value": 20},

        {"weight": 20,
         "value": 30},

        {"weight": 30,
         "value": 40}
    ]

    print(knapsack(items, 50))





























