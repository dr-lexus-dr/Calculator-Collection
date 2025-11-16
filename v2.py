import operator

class SafeCalculator:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod
        }
    
    def calculate(self, num1, num2, operation):
        if operation in self.operations:
            try:
                if operation == '/' and num2 == 0:
                    return "Error: Division by zero!"
                return self.operations[operation](num1, num2)
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error: Unsupported operation"
    
    def run(self):
        print("Safe Calculator")
        print("Available operations: +, -, *, /, **, %")
        
        while True:
            try:
                print("\n" + "="*30)
                num1 = float(input("Enter first number: "))
                operation = input("Enter operation: ").strip()
                num2 = float(input("Enter second number: "))
                
                result = self.calculate(num1, num2, operation)
                print(f"Result: {result}")
                
                continue_calc = input("\nContinue? (y/n): ").lower()
                if continue_calc != 'y':
                    break
                    
            except ValueError:
                print("Error: Please enter valid numbers!")
            except KeyboardInterrupt:
                print("\nExiting calculator")
                break

if __name__ == "__main__":
    calculator = SafeCalculator()
    calculator.run()