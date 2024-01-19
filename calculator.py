import tkinter as tk
import math

def on_click(char):
    if char == '=':
        try:
            # Replace trigonometric function names with math module equivalents
            expression = display.get()
            expression = expression.replace('sin', 'math.sin(math.radians')
            expression = expression.replace('cos', 'math.cos(math.radians')
            expression = expression.replace('tan', 'math.tan(math.radians')
            expression = expression.replace('^', '**')

            # Evaluate the expression
            if expression.count('math.radians') > 0:
                expression += ')' * expression.count('math.radians')  # Close additional parentheses

            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif char == 'C':
        display.delete(0, tk.END)
    else:
        if char in ['sin', 'cos', 'tan']:
            char += '('  # Open parenthesis for the user
        display.insert(tk.END, char)

def create_button(root, text, row, col, command=None, colspan=1, bgcolor="#f0f0f0"):
    button = tk.Button(root, text=text, command=lambda: command(text), width=5, bg=bgcolor)
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
    return button

# Initialize main window
root = tk.Tk()
root.title("Scientific Calculator")

# Define size and layout to mimic a 9-inch phone screen
screen_width = 300  # Adjust as needed for your screen
screen_height = int(screen_width * 16 / 9)  # 16:9 aspect ratio
root.geometry(f"{screen_width}x{screen_height}")

# Color styling
button_color = "#e0e0e0"
special_button_color = "#c0c0c0"
root.configure(bg='black')

# Grid configuration
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

display = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define buttons
buttons = [
    # Standard buttons
    ('7', 1, 0, button_color), ('8', 1, 1, button_color), ('9', 1, 2, button_color),
    ('4', 2, 0, button_color), ('5', 2, 1, button_color), ('6', 2, 2, button_color),
    ('1', 3, 0, button_color), ('2', 3, 1, button_color), ('3', 3, 2, button_color),
    ('0', 4, 0, button_color), ('+', 1, 3, special_button_color), ('-', 2, 3, special_button_color),
    ('*', 3, 3, special_button_color), ('/', 4, 3, special_button_color), ('=', 4, 2, special_button_color),
    ('C', 4, 1, special_button_color),
    # Scientific buttons
    ('sin', 5, 0, special_button_color), ('cos', 5, 1, special_button_color), ('tan', 5, 2, special_button_color),
    ('√', 6, 0, special_button_color), ('x²', 6, 1, special_button_color), ('^', 6, 2, special_button_color),
    ('(', 5, 3, special_button_color), (')', 6, 3, special_button_color),
]

# Create buttons
for (text, row, col, color) in buttons:
    create_button(root, text, row, col, on_click, 1, color)

root.mainloop()
