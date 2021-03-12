'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the 
expression would always evaluate to a result, and there will not be any division by zero operation.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i[-1].isdigit():
                stack.append(int(i))
            else:
                o2 = stack.pop() 
                o1 = stack.pop()
                if i == '+': 
                    stack.append(o1 + o2)
                elif i == '-': 
                    stack.append(o1 - o2)
                elif i == '*': 
                    stack.append(o1 * o2)
                else: 
                    stack.append(int(float(o1) / o2))
        return stack.pop()
