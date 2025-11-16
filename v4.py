import math

class ScientificCalculator:
    def __init__(self):
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'exp': math.exp
        }
    
    def show_menu(self):
        print("\n" + "="*40)
        print("SCIENTIFIC CALCULATOR")
        print("="*40)
        print("1. Basic operations (+, -, *, /)")
        print("2. Trigonometric functions")
        print("3. Logarithms and exponents")
        print("4. Other mathematical functions")
        print("5. Exit")
        print("="*40)
    
    def basic_operations(self):
        print("\n--- Basic Operations ---")
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /, **): ")
            b = float(input("Enter second number: "))
            
            if op == '+': result = a + b
            elif op == '-': result = a - b
            elif op == '*': result = a * b
            elif op == '/': 
                if b == 0: 
                    print("Error: Division by zero!")
                    return
                result = a / b
            elif op == '**': result = a ** b
            else:
                print("Unknown operation!")
                return
            
            print(f"Result: {result}")
            
        except ValueError:
            print("Error: Please enter valid numbers!")
    
    def trigonometric(self):
        print("\n--- Trigonometric Functions ---")
        print("Available: sin, cos, tan")
        func = input("Enter function: ").lower()
        
        if func in ['sin', 'cos', 'tan']:
            try:
                angle = float(input("Enter angle in radians: "))
                result = self.functions[func](angle)
                print(f"{func}({angle}) = {result}")
            except ValueError:
                print("Error: Please enter a valid number!")
        else:
            print("Unknown function!")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Select option (1-5): ")
            
            if choice == '1':
                self.basic_operations()
            elif choice == '2':
                self.trigonometric()
            elif choice == '5':
                print("Exiting calculator")
                break
            else:
                print("Function under development!")

if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.run()