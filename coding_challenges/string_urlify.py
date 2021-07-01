def URLify(input_str, input_len):
    url = ""

    for i in range(input_len):
        if input_str[i] == " ":
            url += "%20"
        else:
            url += input_str[i]
    return url


if __name__ == '__main__':
    input_s = "Msc. Management "
    print(URLify(input_s, len(input_s)))