class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        for char in expression:
            if char == ',':
                continue
            elif char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char == '!':
                stack.append('!')
            elif char == '&':
                stack.append('&')
            elif char == '|':
                stack.append('|')
            elif char == ')':
                operands = []
                while stack and isinstance(stack[-1], bool):
                    operands.append(stack.pop())
                operator = stack.pop()
                
                if operator == '!':
                    stack.append(not operands[0])
                elif operator == '&':
                    stack.append(all(operands))
                elif operator == '|':
                    stack.append(any(operands))
            elif char == '(':
                continue
        
        return stack[0]


