def insurance_series_germany():
    annual_income_list = [
        64350,
        62550,
        60750,
        59400,
        57600,
        56250,
        54900,
        53550,
        52200,
        50850,
        49500,
        49950,
        48600,
        48150,
        47700,
        47250,
        46800,
        46350,
        45900
    ]

    diff_dict = {}

    idx = 0
    for i in range(2, len(annual_income_list)):
        diff_dict[idx] = annual_income_list[i] - annual_income_list[i-1]
        idx += 1

    for k, v in diff_dict.items():
        print(k, '-->', v)


if __name__ == '__main__':
    insurance_series_germany()


























