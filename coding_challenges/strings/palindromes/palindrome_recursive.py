def recursive_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False

    return recursive_palindrome(s[1:-1])


if __name__ == '__main__':
    print(recursive_palindrome("Ada da"))
