import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        self.current_input = ""
        self.create_widgets()
    
    def create_widgets(self):
        # Input field
        self.display = tk.Entry(self.window, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('⌫', 5, 1)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self.window, text=text, font=('Arial', 16),
                              command=self.calculate, bg='orange')
            elif text in ['C', '⌫']:
                btn = tk.Button(self.window, text=text, font=('Arial', 16),
                              command=self.clear if text == 'C' else self.backspace)
            else:
                btn = tk.Button(self.window, text=text, font=('Arial', 16),
                              command=lambda t=text: self.add_to_display(t))
            
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
        # Configure row and column weights
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
    
    def add_to_display(self, char):
        self.current_input += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)
    
    def clear(self):
        self.current_input = ""
        self.display.delete(0, tk.END)
    
    def backspace(self):
        self.current_input = self.current_input[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)
    
    def calculate(self):
        try:
            if self.current_input:
                # Safe evaluation
                allowed_chars = set('0123456789+-*/.() ')
                if not all(c in allowed_chars for c in self.current_input):
                    messagebox.showerror("Error", "Invalid characters in expression")
                    return
                
                result = eval(self.current_input)
                self.current_input = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_input)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")
            self.clear()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = CalculatorGUI()
    calc.run()