def calculate(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "Invalid operator"

def main():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        

        result = calculate(num1, num2, op)
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid number entered.")
        

if __name__=="__main__":
    main() 
