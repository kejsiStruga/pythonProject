"""
Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.

A palindrome - a string that reads same backwards as forwards
So the reverse of the string is equal to the org string

madam
mmaad

mma d amm

odd length
    1 character will not be paired

even length
    each character must be paired

We'll go over the string and keep a dict where keys are the characters;
Then we traverse the dict and check if each character has an even frequency

in the case of odd length, there should be only one character with odd frequency

"""


def isPalindrome(s):
    len_s = len(s)

    s_dict = {}

    for c in s:
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1

    if len_s % 2 == 0: # even
        for i in s_dict:
            if s_dict[i] % 2 != 0:
                return "NO"
        return "YES"
    else:
        counter = 0
        for i in s_dict:
            if s_dict[i] % 2 != 0:
                counter += 1
        if counter == 1:
            return "YES"
        else:
            return "NO"





























