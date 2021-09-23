class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_length = len(digits)
        plus_one = []
        index = digits_length - 1

        digit_sum = digits[index] + 1
        result = digit_sum % 10
        carry = 1 if digit_sum >= 10 else 0
        plus_one.append(result)
        index -= 1

        while index > -1:
            if carry:
                digit_sum = digits[index] + 1
                result = digit_sum % 10
                carry = 1 if digit_sum >= 10 else 0
                plus_one.append(result)
            else:
                plus_one.append(digits[index])
                carry = 0
            index -= 1

        if carry:
            plus_one.append(carry)

        return plus_one[::-1]