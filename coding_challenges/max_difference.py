
def max_diff(a):
    min_el = a[0]
    max_el = 0
    for i in range(len(a)):
        if a[i] < min_el:
            min_el = a[i]
        elif a[i] - min_el > max_el:
            max_el = a[i] - min_el
    return max_el
