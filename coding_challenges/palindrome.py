import string


def is_palindrome(s):
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")

    """
    The easiest way to do it in Python, would be 
    to reverse the string and check if its equal to the unreversed string.
    The way we reverse a string in Python is by using the slice
    function* that steps backwards (-1).
    
    *The slice function in Python. returns a range of characters.
    Specify the start and end index, separated by a colon,
    to return a part of the string.
    
    Syntax: 
    string[start:end:direction]
    start -> inclusive
    end -> exclusive
    direction -> optional
    """
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome("madam I'm Adam"))
