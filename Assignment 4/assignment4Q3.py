import tkinter as tk

# Function to handle button click
def on_button_click(value):
    current = display.get()
    display.delete(0, tk.END)  # Clear the display
    display.insert(tk.END, current + str(value))  # Append the clicked value

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(display.get())  # Use eval to evaluate the expression
        display.delete(0, tk.END)  # Clear the display
        display.insert(tk.END, result)  # Display the result
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to delete the last character in the display
def delete_last_char():
    current = display.get()
    display.delete(len(current)-1, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")  # Title of the window

# Set window size
root.geometry("1300x700")

# Display widget for showing input and results
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create the buttons and place them on the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Additional buttons for clear and delete operations
clear_button = tk.Button(root, text="C", width=10, height=3, font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0, padx=5, pady=5)

delete_button = tk.Button(root, text="DEL", width=10, height=3, font=("Arial", 18), command=delete_last_char)
delete_button.grid(row=5, column=1, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
