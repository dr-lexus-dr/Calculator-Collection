def simple_calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    print("Enter 'exit' to quit")
    
    while True:
        try:
            expression = input("\nEnter expression: ").strip()
            
            if expression.lower() == 'exit':
                print("Exiting calculator")
                break
                
            # Check expression safety
            allowed_chars = set('0123456789+-*/. ()')
            if not all(c in allowed_chars for c in expression):
                print("Error: Invalid characters in expression")
                continue
                
            result = eval(expression)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Division by zero!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_calculator()