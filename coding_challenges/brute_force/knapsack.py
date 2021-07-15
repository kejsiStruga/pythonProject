"""
arr = [1, 2, 3]
power_set(arr) = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
2^n elements in the power set of a set of n elements
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





























