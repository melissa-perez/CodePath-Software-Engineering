class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
            }
        # our stack
        parser = []
        # corner case: true cases are even lengths
        if len(s) % 2 != 0:
            return False

        for bracket in s:
            if bracket in brackets:
                if len(parser) > 0 and brackets[bracket] == parser[-1]:
                    parser.pop(-1)
                else:
                    return False
            else:
                parser.append(bracket)
        # corner case: if stack has len then not valid
        if len(parser) > 0:
            return False
        # if we make it here then it is valid    
        return True
