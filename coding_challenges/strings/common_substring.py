"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

s1 = "and"
s2 = "abc"

They share a common substring "a"

s1 = "be"
s2 = "cat"

They don't share any common substrings

For each pair of strings return "YES" or "NO"

"""


def haveCommonSubstring(s1, s2):
    if s1 == s2:
        return "YES"
    elif len(s1) == 0 or len(s2) == 0:
        return "NO"
    else:
        for i in s1:
            if i in s2:
                return "YES"
        return "NO"































