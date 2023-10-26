import tkinter as tk

# Define the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x300")

# Create the entry field for displaying the input and result
entry = tk.Entry(window, width=25, borderwidth=5)
entry.grid(row=0, columnspan=4, padx=10, pady=10)

# Define functions for each operation
def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create buttons for numbers and operations
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

row = 1
for button_row in buttons:
    column = 0
    for button_text in button_row:
        button = tk.Button(window, text=button_text, width=5, command=lambda char=button_text: button_click(char))
        button.grid(row=row, column=column, padx=5, pady=5)
        column += 1
    row += 1

# Create the clear and equal buttons
clear_button = tk.Button(window, text="Clear", width=5, command=button_clear)
equal_button = tk.Button(window, text="=", width=5, command=button_equal)

clear_button.grid(row=5, column=0, padx=5, pady=5)
equal_button.grid(row=5, column=1, padx=5, pady=5)

# Run the main loop
window.mainloop()
