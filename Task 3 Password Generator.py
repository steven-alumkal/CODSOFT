import tkinter as tk
import random

# Define the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x150")

# Create the label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window, width=10)

length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Define the function to generate and display the password
def generate_password():
    password_length = int(length_entry.get())

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(characters) for i in range(password_length))

    password_label.config(text=password)

# Create the generate button and password label
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
password_label = tk.Label(window, text="")

generate_button.grid(row=1, column=0, padx=5, pady=5)
password_label.grid(row=1, column=1, padx=5, pady=5)

# Run the main loop
window.mainloop()
