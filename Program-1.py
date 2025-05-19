#Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
# Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."
# Example usage
if __name__ == "__main__":
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (addition, subtraction, multiplication, division): ").lower()

    calculator = Calculator(a, b, operation)
    result = calculator.calculate()
    print(f"The result of {operation} between {a} and {b} is: {result}")