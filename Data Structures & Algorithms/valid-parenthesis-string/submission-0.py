class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == '*':
                star_stack.append(i)
            elif c == '(':
                parenthesis_stack.append(i)
            else:
                # try to pop left parenthesis; if cant, try to pop star
                if parenthesis_stack:
                    parenthesis_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        # might have left parentheses and stars left, storing the indices:
        # stars = [2, 3]
        # left = [0]
        # then, try to pop left with stars, but only if stars[-1] > left[-1]
        while parenthesis_stack and star_stack:
            if parenthesis_stack[-1] > star_stack[-1]:
                return False
            parenthesis_stack.pop()
            star_stack.pop()


        return len(parenthesis_stack) == 0
        