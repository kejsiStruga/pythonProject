
def longest_pattern(str_param):
    # return the longest pattern within the string

    n = len(str_param)
    LCSR = [[0 for k in range(n + 1)]
            for l in range(n + 1)]

    result = ""
    result_length = 0

    idx = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (str_param[i - 1] == str_param[j - 1] and
                    LCSR[i - 1][j - 1] < (j - 1)):
                LCSR[i][j] = LCSR[i - 1][j - 1] + 1

                if LCSR[i][j] > result_length:
                    result_length = LCSR[i][j]
                    idx = max(i, idx)

            else:
                LCSR[i][j] = 0

    if result_length > 1:
        for i in range(idx - result_length + 1, idx + 1):
            result = result + str_param[i - 1]
        result = "yes " + result
    else:
        result = "no " + result

    return result
