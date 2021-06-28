"""
REQUIREMENT:
~~~~~~~~~~~~~

Have the function longest_pattern(str) take str which will be a string
and return the longest pattern within the string. A pattern for this challenge
will be defined as: if at least 2 or more adjacent characters within the string
repeat at least twice. i.e. "aabecaa" contains the pattern "aa".

On the other hand, "abbbaac" doesn't contain any pattern. Your program should
return yes/no pattern/null.

The string may either contain all characters (a through z only), integers, or both.
But the parameter will always be of type string. The max length will be 20 chars.
if a string is ie "aa2bbbaacbbb", the pattern is "bbb" not "aa".
So you must always return the longest pattern possible!!!!


SOLUTION:
~~~~~~~~~~
In CS, the __LONGEST_REPEATED_SUBSTRING_PROBLEM__ is the problem
of finding the longest substring of a string that occurs at least twice.

This problem can be solved in linear time and space O(n) by building a
suffix tree for the string (with a special end-of-string symbol like '$' append.


"""


def longest_repeated_substring(str_param):
    # return the longest pattern (at least 2 adjacent chars) within the string that's repeated at least twice

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


if __name__ == '__main__':
    str1 = "fdwaw4helloworldvcdv1c3xcv3xcz1sda21f2sd1ahelloworldgafgfa4564534321fadghelloworld"
    print(longest_pattern(str1))
