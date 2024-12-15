import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest
def calculate_si():
    try:
        # Get the values from the entry fields
        principal = float(principal_entry.get())
        rate_of_interest = float(rate_entry.get())
        time = float(time_entry.get())

        # Calculate Simple Interest
        simple_interest = (principal * rate_of_interest * time) / 100
        total_amount = principal + simple_interest

        # Display the result
        si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        total_label.config(text=f"Total Amount: {total_amount:.2f}")
    
    except ValueError:
        # If the user enters invalid data, show an error message
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields")

# Function to clear all the fields
def clear_fields():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    si_label.config(text="Simple Interest: ")
    total_label.config(text="Total Amount: ")

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("600x450")

# Create labels and entry fields for user inputs
tk.Label(root, text="Principal Amount (P):", font=("Arial", 12)).pack(pady=10)
principal_entry = tk.Entry(root, font=("Arial", 14))
principal_entry.pack(pady=5)

tk.Label(root, text="Rate of Interest (R) [%]:", font=("Arial", 12)).pack(pady=10)
rate_entry = tk.Entry(root, font=("Arial", 14))
rate_entry.pack(pady=5)

tk.Label(root, text="Time Period (T) [in years]:", font=("Arial", 12)).pack(pady=10)
time_entry = tk.Entry(root, font=("Arial", 14))
time_entry.pack(pady=5)

# Button to calculate Simple Interest
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14), bg="blue", fg="white", command=calculate_si)
calculate_button.pack(pady=20)

# Button to clear all fields
clear_button = tk.Button(root, text="Clear", font=("Arial", 14), bg="brown", fg="white", command=clear_fields)
clear_button.pack(pady=10)

# Labels to display the results
si_label = tk.Label(root, text="Simple Interest: ", font=("Arial", 12))
si_label.pack(pady=10)

total_label = tk.Label(root, text="Total Amount: ", font=("Arial", 12))
total_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
