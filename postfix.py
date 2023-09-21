def is_operand(val):
    # Check if val is an operand (a number or a single character)
    return val.isdigit() or (len(val) == 1 and val.isalpha())


def is_operator(val):
    # Check if val is an operator (+, -, *, /, ^)
    return val in ['+', '-', '*', '/', '^']

def operate(operand1, operand2, operator):
    # Perform the operation based on the operator
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero is not allowed")
        return operand1 / operand2
    if operator == '^':
        return operand1 ** operand2

def eval_post(expression):
    stack = []
    for val in expression:
        if is_operand(val):
            stack.append(int(val))
        elif is_operator(val):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operate(operand1, operand2, val)
            stack.append(result)
    return stack.pop()

e2 = ['2', '4', '^', '3', '4', '*', '5', '/', '-']
result = eval_post(e2)
print("Result:", result)

e2 = ['12', '13', '+', '10', '20', '*','-']
result = eval_post(e2)
print("Result:", result)

