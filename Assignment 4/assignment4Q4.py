import tkinter as tk
from time import strftime

# Function to get the current time and update the clock display
def time():
    # Get the current time in the format HH:MM:SS AM/PM
    current_time = strftime('%I:%M:%S %p')
    # Update the clock label with the new time
    label.config(text=current_time)
    # Call this function again after 1000 ms (1 second) to update the time
    label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")  # Set the window title
root.geometry("700x300")  # Set the window size

# Create a label widget to display the time
label = tk.Label(root, font=("calibri", 50, "bold"), background="dark blue", foreground="white")
label.pack(anchor="center")  # Place the label in the center

# Call the time function to start the clock
time()

# Run the Tkinter event loop
root.mainloop()


