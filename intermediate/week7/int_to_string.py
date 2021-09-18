def int_to_string(num):

    shift = ord('0')
    result = []
    sign = 1

    # the magic number is 48, to shift the int correct
    if num < 0:
        sign = -1
        num *= -1

    while num > 0:
        digit = num % 10
        res = chr(digit + shift)
        result.append(res)
        num //= 10

    if sign < 0:
        result.append("-")

    return "".join(result[::-1])


if __name__ == "__main__":
    print(int_to_string(123))
    print(int_to_string(-67154))
