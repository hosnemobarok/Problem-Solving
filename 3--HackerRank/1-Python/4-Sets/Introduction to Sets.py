def average(arr):
    set_digit = set(arr)
    digit_len = len(set_digit)
    result = (sum(set_digit) / digit_len)
    return result


