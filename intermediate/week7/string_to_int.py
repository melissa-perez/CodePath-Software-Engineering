
def string_to_int(s):
    shift = ord('0')
    result = 0
    sign = 1

    # the magic number is 48, to shift the int correct
    for digit in s:
        if digit == '-':
            sign = -1
        else:
            res = ord(digit) - shift
            result = result * 10 + res
    return result * sign


if __name__ == "__main__":
    print(string_to_int("123"))
    print(string_to_int("-67154"))