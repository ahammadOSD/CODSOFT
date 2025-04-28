import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())  # Get the first number
        num2 = float(entry2.get())  # Get the second number
        operation = operation_var.get()  # Get the selected operation

        # Perform calculation based on operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return
        
        result_label.config(text=f"Result: {result}")  # Display the result

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")  # Handle invalid input

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Entry field for the first number
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root, font=("Helvetica", 14))
entry1.pack(pady=5)

# Entry field for the second number
tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root, font=("Helvetica", 14))
entry2.pack(pady=5)

# Dropdown menu for operation selection
operation_var = tk.StringVar()
operation_var.set("Add")  # Default operation

tk.Label(root, text="Select Operation:").pack(pady=5)
operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.pack(pady=5)

# Button to trigger calculation
calc_button = tk.Button(root, text="Calculate", font=("Helvetica", 14), command=calculate)
calc_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:", font=("Helvetica", 16, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()
