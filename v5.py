import tkinter as tk
from tkinter import ttk, messagebox
import math

class ScientificCalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("500x600")
        self.window.resizable(False, False)
        
        self.current_input = ""
        self.setup_styles()
        self.create_widgets()
    
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('Scientific.TButton', font=('Arial', 10))
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(main_frame, textvariable=self.display_var, 
                               font=('Arial', 18), justify='right', state='readonly')
        self.display.grid(row=0, column=0, columnspan=5, sticky='ew', padx=5, pady=10)
        
        self.create_basic_buttons(main_frame)
        self.create_scientific_buttons(main_frame)
        self.create_trig_buttons(main_frame)
        
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
    
    def create_basic_buttons(self, parent):
        basic_frame = ttk.LabelFrame(parent, text="Basic Operations", padding="5")
        basic_frame.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
        
        basic_buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('C', 0, 4),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3), ('⌫', 1, 4),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('(', 2, 4),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3), (')', 3, 4)
        ]
        
        for (text, row, col) in basic_buttons:
            if text == '=':
                btn = ttk.Button(basic_frame, text=text, command=self.calculate)
                btn.grid(row=row, column=col, sticky='ew', padx=2, pady=2)
            elif text in ['C', '⌫']:
                btn = ttk.Button(basic_frame, text=text,
                               command=self.clear if text == 'C' else self.backspace)
                btn.grid(row=row, column=col, sticky='ew', padx=2, pady=2)
            else:
                btn = ttk.Button(basic_frame, text=text,
                               command=lambda t=text: self.add_to_display(t))
                btn.grid(row=row, column=col, sticky='ew', padx=2, pady=2)
        
        for i in range(5):
            basic_frame.columnconfigure(i, weight=1)
        for i in range(4):
            basic_frame.rowconfigure(i, weight=1)
    
    def create_scientific_buttons(self, parent):
        sci_frame = ttk.LabelFrame(parent, text="Scientific Functions", padding="5")
        sci_frame.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
        
        sci_buttons = [
            ('√', 0, 0), ('x²', 0, 1), ('x^y', 0, 2), ('π', 0, 3), ('e', 0, 4),
            ('log', 1, 0), ('ln', 1, 1), ('exp', 1, 2), ('1/x', 1, 3), ('%', 1, 4),
            ('abs', 2, 0), ('floor', 2, 1), ('ceil', 2, 2), ('round', 2, 3), ('!', 2, 4)
        ]
        
        for (text, row, col) in sci_buttons:
            btn = ttk.Button(sci_frame, text=text, style='Scientific.TButton',
                           command=lambda t=text: self.scientific_function(t))
            btn.grid(row=row, column=col, sticky='ew', padx=2, pady=2)
        
        for i in range(5):
            sci_frame.columnconfigure(i, weight=1)
        for i in range(3):
            sci_frame.rowconfigure(i, weight=1)
    
    def create_trig_buttons(self, parent):
        trig_frame = ttk.LabelFrame(parent, text="Trigonometric Functions", padding="5")
        trig_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
        
        trig_buttons = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), 
            ('asin', 1, 0), ('acos', 1, 1), ('atan', 1, 2),
            ('sinh', 2, 0), ('cosh', 2, 1), ('tanh', 2, 2)
        ]
        
        for (text, row, col) in trig_buttons:
            btn = ttk.Button(trig_frame, text=text, style='Scientific.TButton',
                           command=lambda t=text: self.trig_function(t))
            btn.grid(row=row, column=col, sticky='ew', padx=2, pady=2)
        
        self.angle_mode = tk.StringVar(value="rad")
        deg_btn = ttk.Radiobutton(trig_frame, text="Degrees", variable=self.angle_mode, value="deg")
        rad_btn = ttk.Radiobutton(trig_frame, text="Radians", variable=self.angle_mode, value="rad")
        
        deg_btn.grid(row=0, column=3, columnspan=2, sticky='w', padx=5)
        rad_btn.grid(row=1, column=3, columnspan=2, sticky='w', padx=5)
        
        for i in range(5):
            trig_frame.columnconfigure(i, weight=1)
        for i in range(3):
            trig_frame.rowconfigure(i, weight=1)
    
    def add_to_display(self, char):
        self.current_input += str(char)
        self.display_var.set(self.current_input)
    
    def clear(self):
        self.current_input = ""
        self.display_var.set("")
    
    def backspace(self):
        self.current_input = self.current_input[:-1]
        self.display_var.set(self.current_input)
    
    def degrees_to_radians(self, degrees):
        return degrees * math.pi / 180
    
    def radians_to_degrees(self, radians):
        return radians * 180 / math.pi
    
    def scientific_function(self, func):
        try:
            if self.current_input:
                current_value = float(eval(self.current_input))
                result = None
                
                if func == '√':
                    if current_value < 0:
                        raise ValueError("Cannot calculate square root of negative number")
                    result = math.sqrt(current_value)
                elif func == 'x²':
                    result = current_value ** 2
                elif func == 'x^y':
                    exponent = tk.simpledialog.askfloat("Power", "Enter exponent:")
                    if exponent is not None:
                        result = current_value ** exponent
                    else:
                        return
                elif func == 'π':
                    result = math.pi
                elif func == 'e':
                    result = math.e
                elif func == 'log':
                    if current_value <= 0:
                        raise ValueError("Logarithm undefined for non-positive numbers")
                    result = math.log10(current_value)
                elif func == 'ln':
                    if current_value <= 0:
                        raise ValueError("Natural log undefined for non-positive numbers")
                    result = math.log(current_value)
                elif func == 'exp':
                    result = math.exp(current_value)
                elif func == '1/x':
                    if current_value == 0:
                        raise ValueError("Division by zero")
                    result = 1 / current_value
                elif func == '%':
                    result = current_value / 100
                elif func == 'abs':
                    result = abs(current_value)
                elif func == 'floor':
                    result = math.floor(current_value)
                elif func == 'ceil':
                    result = math.ceil(current_value)
                elif func == 'round':
                    result = round(current_value)
                elif func == '!':
                    if current_value < 0 or current_value != int(current_value):
                        raise ValueError("Factorial defined only for non-negative integers")
                    result = math.factorial(int(current_value))
                
                if result is not None:
                    self.current_input = str(result)
                    self.display_var.set(self.current_input)
                    
        except ValueError as e:
            messagebox.showerror("Math Error", str(e))
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {e}")
            self.clear()
    
    def trig_function(self, func):
        try:
            if self.current_input:
                current_value = float(eval(self.current_input))
                result = None
                
                if self.angle_mode.get() == "deg" and func in ['sin', 'cos', 'tan']:
                    angle = self.degrees_to_radians(current_value)
                elif self.angle_mode.get() == "deg" and func in ['asin', 'acos', 'atan']:
                    angle = current_value
                else:
                    angle = current_value
                
                if func == 'sin':
                    result = math.sin(angle)
                elif func == 'cos':
                    result = math.cos(angle)
                elif func == 'tan':
                    result = math.tan(angle)
                elif func == 'asin':
                    if current_value < -1 or current_value > 1:
                        raise ValueError("Arcsin input must be between -1 and 1")
                    result = math.asin(angle)
                    if self.angle_mode.get() == "deg":
                        result = self.radians_to_degrees(result)
                elif func == 'acos':
                    if current_value < -1 or current_value > 1:
                        raise ValueError("Arccos input must be between -1 and 1")
                    result = math.acos(angle)
                    if self.angle_mode.get() == "deg":
                        result = self.radians_to_degrees(result)
                elif func == 'atan':
                    result = math.atan(angle)
                    if self.angle_mode.get() == "deg":
                        result = self.radians_to_degrees(result)
                elif func == 'sinh':
                    result = math.sinh(angle)
                elif func == 'cosh':
                    result = math.cosh(angle)
                elif func == 'tanh':
                    result = math.tanh(angle)
                
                if result is not None:
                    self.current_input = str(result)
                    self.display_var.set(self.current_input)
                    
        except ValueError as e:
            messagebox.showerror("Math Error", str(e))
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Trigonometric calculation error: {e}")
            self.clear()
    
    def calculate(self):
        try:
            if self.current_input:
                allowed_chars = set('0123456789+-*/.() ')
                if not all(c in allowed_chars for c in self.current_input):
                    messagebox.showerror("Error", "Invalid characters in expression")
                    return
                
                result = eval(self.current_input)
                self.current_input = str(result)
                self.display_var.set(self.current_input)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")
            self.clear()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    try:
        import tkinter.simpledialog
    except ImportError:
        pass
    
    calculator = ScientificCalculatorGUI()
    calculator.run()