def calculator(num1: float, num2: float, *, operator: str):
    '''Give two operands, one arithmetic operator and return the result of matched operation.
    
        Positional arguments:
        num1 --the first operand (must be a float)
        num2 --the second operand (must be a float)
        Keyword argument:
        operator --arithmetic operator for num1 and num2 (operations and their signs are same as python operations)
        Valid operations: addition, subtraction, multiplication, division, remainder, exponentiation and floor division
        '''
    
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)
        case "%":
            print(num1 % num2)
        case "**":
            print(num1 ** num2)
        case "//":
            print(num1 // num2)
        case _:
            print("enter a valid operator.")

    return 0
        
print(calculator(1.0, 2.5, operator="-"))