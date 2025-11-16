# Calculator Collection - Complete Descriptions and Usage Guides

## 1. Simple Console Calculator

**Description:**
A basic command-line calculator that evaluates mathematical expressions using Python's eval() function. It provides quick calculations with minimal safety checks. Suitable for simple arithmetic operations and quick calculations.

**How to use:**
1. Run the Python script
2. The calculator will start and show available operations
3. Enter mathematical expressions directly:
   - Basic arithmetic: "5 + 3"
   - With parentheses: "(2 + 3) * 4"
   - Decimal numbers: "10.5 / 2"
4. Supported operators: + (addition), - (subtraction), * (multiplication), / (division)
5. Type 'exit' to quit the calculator
6. The calculator handles basic error checking for division by zero and invalid expressions

**Example usage:**
Enter expression: 15 + 7
Result: 22
Enter expression: (10 - 3) * 2
Result: 14
Enter expression: 8 / 2
Result: 4.0
Enter expression: exit
Exiting calculator




## 2. Safe Calculator with Parsing

**Description:**
A secure console calculator that manually parses operations instead of using eval(). This approach is safer as it doesn't execute arbitrary code. Includes additional operations like exponentiation and modulus. Ideal for users who need more security and extended functionality.

**How to use:**
1. Run the Python script
2. Calculator displays available operations: +, -, *, /, ** (power), % (modulus)
3. Follow the prompts step by step:
   - Enter first number
   - Enter operation symbol
   - Enter second number
4. View the calculated result
5. Choose whether to continue with another calculation or exit
6. Press Ctrl+C at any time to exit immediately

**Example usage:**
Enter first number: 15
Enter operation: +
Enter second number: 7
Result: 22.0
Continue? (y/n): y

Enter first number: 8
Enter operation: **
Enter second number: 2
Result: 64.0
Continue? (y/n): n




## 3. Basic Graphical Calculator (Tkinter)

**Description:**
A desktop calculator with graphical user interface featuring standard calculator layout. Built with Tkinter, it provides an intuitive button-based interface similar to physical calculators. Perfect for users who prefer visual interaction.

**How to use:**
1. Run the script to open the calculator window
2. Interface elements:
   - Display screen at the top shows input and results
   - Number buttons (0-9) for input
   - Operation buttons: +, -, *, /
   - Additional buttons:
     - '.' for decimal points
     - 'C' to clear everything
     - '⌫' to delete last character
     - '=' to calculate result
     - '(' and ')' for parentheses
3. Click buttons to build your expression
4. Click '=' to see the result
5. Close the window or use system close button to exit

**Features:**
- Standard calculator layout familiar to most users
- Orange equals button for easy identification
- Real-time display of input
- Error handling for invalid operations
- Support for complex expressions with parentheses

## 4. Scientific Calculator (Console Version)

**Description:**
Advanced console calculator with scientific functions including trigonometry, logarithms, exponents, and special operations. Features a menu-driven interface that organizes functions into categories. Excellent for students and professionals needing scientific calculations.

**How to use:**
1. Run the Python script
2. Main menu appears with options:
   - 1: Basic operations (+, -, *, /, **)
   - 2: Trigonometric functions (sin, cos, tan)
   - 3: Logarithms and exponents (log, ln, exp)
   - 4: Other mathematical functions (under development)
   - 5: Exit calculator
3. Select option by entering the corresponding number
4. Follow sub-menus and prompts for specific operations
5. For trigonometric functions, angles are entered in radians

**Example usage:**
Select option (1-5): 1
Enter first number: 5
Enter operation: *
Enter second number: 4
Result: 20.0

Select option (1-5): 2
Enter function: sin
Enter angle in radians: 1.57
sin(1.57) = 0.9999996829318346




## 5. Scientific Calculator with GUI

**Description:**
Comprehensive desktop scientific calculator with advanced mathematical functions organized in labeled sections. Includes three main functional areas: basic operations, scientific functions, and trigonometric functions. The most feature-rich calculator in the collection.

**How to use:**

**Basic Operations Section:**
- Click number buttons (0-9) to input values
- Use operation buttons: + (addition), - (subtraction), * (multiplication), / (division)
- Use '(' and ')' buttons for complex expressions
- '.' button for decimal numbers
- 'C' button clears the entire display
- '⌫' button deletes the last character
- '=' button calculates and displays the result

**Scientific Functions Section:**
- **√** - Square root of current value
- **x²** - Squares the current value
- **x^y** - Raises to power (opens dialog for exponent input)
- **π** - Inserts mathematical constant Pi (3.14159...)
- **e** - Inserts mathematical constant e (2.71828...)
- **log** - Base-10 logarithm
- **ln** - Natural logarithm (base e)
- **exp** - Exponential function (e raised to power)
- **1/x** - Reciprocal (1 divided by current value)
- **%** - Percentage (divides current value by 100)
- **abs** - Absolute value
- **floor** - Round down to nearest integer
- **ceil** - Round up to nearest integer
- **round** - Round to nearest integer
- **!** - Factorial (for non-negative integers)

**Trigonometric Functions Section:**
- **sin** - Sine function
- **cos** - Cosine function
- **tan** - Tangent function
- **asin** - Inverse sine (arcsine)
- **acos** - Inverse cosine (arccosine)
- **atan** - Inverse tangent (arctangent)
- **sinh** - Hyperbolic sine
- **cosh** - Hyperbolic cosine
- **tanh** - Hyperbolic tangent
- **Degrees/Radians** - Radio buttons to switch angle modes

**Workflow:**
1. Run the script to open the calculator window
2. Build your calculation using number and function buttons
3. For scientific functions: enter a number first, then click the function button
4. For power (x^y): enter base number, click x^y, enter exponent in dialog
5. Use parentheses to control calculation order
6. Click '=' to compute the final result
7. Toggle between degrees and radians for trigonometric functions as needed

**Key Features:**
- Read-only display prevents accidental typing
- Organized tabbed interface for different function types
- Comprehensive error handling with descriptive messages
- Degree/radian mode selection for trigonometric functions
- Professional appearance with labeled sections
- Support for complex mathematical expressions

**Installation Requirements:**
- Python 3.x installed on your system
- Tkinter library (usually included with standard Python installation)
- No additional packages or dependencies required

**Error Handling:**
All calculators include comprehensive error handling for:
- Division by zero
- Invalid mathematical operations
- Syntax errors in expressions
- Out-of-range values
- Invalid inputs

The GUI versions provide visual error messages while console versions show text-based warnings. Choose the calculator that best fits your needs - console versions for quick calculations or remote access, and GUI versions for enhanced usability and advanced features.






**Requirements for all calculators:**
- Python 3.x
- Tkinter (usually included with Python)
