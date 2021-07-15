"""Amanda has a string of lowercase letters that she wants to copy to a new string. She can perform the following
operations with the given costs. She can perform them any number of times to construct a new string p:

Append a character to the end of string p at a cost of  dollar.
Choose any substring of s and append it to the end of p at no charge.

"""


def stringConstruction(s):
    p = ""
    cost = 0
    print(len(s) % 2 == 0)
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            p += s[i]
            cost += 1
        if p == s[len(s)//2:len(s)]:
            p += s[len(s)//2:len(s)]
        else:
            for i in range((len(s) // 2), len(s)):
                p += s[i]
                cost += 1
    else:
        for i in range(len(s) // 2):
            p += s[i]
            cost += 1
        if p == s[len(s)//2+1:len(s)]:
            p += s[len(s)//2:len(s)]
        else:
            for i in range((len(s) // 2), len(s)):
                p += s[i]
                cost += 1


    return cost


if __name__ == '__main__':
    print(stringConstruction("abcd"))

































