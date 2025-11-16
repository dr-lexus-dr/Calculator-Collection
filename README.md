# Calculator-Collection

v1. Simple Console Calculator

Description: A basic command-line calculator that evaluates mathematical expressions using Python's eval() function. It provides quick calculations with minimal safety checks.

How to use:
Run the script
Enter mathematical expressions (e.g., "2 + 3 * 4")
Use operators: +, -, *, /
Type 'exit' to quit
Supports parentheses and decimal numbers

Example usage:

Enter expression: (5 + 3) * 2
Result: 16.0
Enter expression: 10 / 3
Result: 3.3333333333333335


v2. Safe Calculator with Parsing

Description: A secure console calculator that manually parses operations instead of using eval(). It's safer than the simple calculator and includes additional operations like exponentiation and modulus.

How to use:
Run the script
Enter first number when prompted
Choose operation: +, -, *, /, **, %
Enter second number
View result and choose to continue or exit
Press Ctrl+C to exit immediately

Example usage:
Enter first number: 8
Enter operation: **
Enter second number: 2
Result: 64.0
Continue? (y/n): n


v3. Basic Graphical Calculator (Tkinter)

Description: A desktop calculator with graphical user interface featuring standard calculator layout. Includes basic arithmetic operations, clear functions, and intuitive button interface.

How to use:

Run the script to open the calculator window

Click number buttons to input values

Click operation buttons (+, -, *, /)

Use 'C' to clear everything

Use '⌫' to delete last character

Click '=' to calculate result

Close window to exit

Features:

Number buttons 0-9

Basic operations: +, -, *, /

Decimal point support

Clear and backspace functions

Orange equals button for easy identification

4. Scientific Calculator (Console Version)
Description:
Advanced console calculator with scientific functions including trigonometry, logarithms, exponents, and special operations. Features a menu-driven interface.

How to use:

Run the script

Choose from menu options:

1: Basic operations

2: Trigonometric functions

3: Logarithms and exponents

5: Exit

Follow prompts for specific operations

For trigonometric functions, enter angles in radians

Example usage:

text
Select option (1-5): 2
Enter function: sin
Enter angle in radians: 1.57
sin(1.57) = 0.9999996829318346
5. Scientific Calculator with GUI
Description:
Comprehensive desktop scientific calculator with advanced mathematical functions organized in tabbed sections. Includes trigonometry, logarithms, exponents, and specialized operations.

How to use:

Basic Operations:

Click number buttons (0-9)

Use +, -, *, / for arithmetic

Parentheses for complex expressions

'=' to calculate

'C' to clear, '⌫' to backspace

Scientific Functions:

√ - Square root

x² - Square

x^y - Power (prompts for exponent)

π, e - Mathematical constants

log, ln - Logarithms

exp - Exponential

1/x - Reciprocal

% - Percentage

abs - Absolute value

floor, ceil, round - Rounding functions

! - Factorial

Trigonometric Functions:

sin, cos, tan - Basic trigonometric

asin, acos, atan - Inverse trigonometric

sinh, cosh, tanh - Hyperbolic functions

Select Degrees/Radians radio buttons for angle mode

Key Features:

Read-only display prevents direct typing

Organized sections for different function types

Error messages for invalid operations

Degree/radian mode for trigonometric functions

Professional interface with labeled sections

Installation Requirements:

Python 3.x

Tkinter (usually included with Python)

No additional packages required

All calculators handle common errors like division by zero and invalid inputs with helpful error messages. The GUI versions provide the most user-friendly experience while the console versions are useful for quick calculations or remote access.
