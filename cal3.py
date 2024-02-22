import tkinter as tk

def button_click(number):
    current = entry_screen.get()
    entry_screen.delete(0, tk.END)
    entry_screen.insert(tk.END, str(current) + str(number))

def clear_screen():
    entry_screen.delete(0, tk.END)

def backspace():
    current = entry_screen.get()
    entry_screen.delete(len(current)-1)

def calculate():
    expression = entry_screen.get()
    try:
        result = eval(expression)
        if isinstance(result, int):  # Check if result is an integer
            entry_screen.delete(0, tk.END)
            entry_screen.insert(tk.END, result)
        elif isinstance(result, float):  # Check if result is a float
            quotient = result // 1  # Get the integer part of the quotient
            if result % 1 == 0:  # If remainder is zero
                entry_screen.delete(0, tk.END)
                entry_screen.insert(tk.END, int(quotient))  # Display quotient as integer
            else:
                entry_screen.delete(0, tk.END)
                entry_screen.insert(tk.END, "{:.2f}".format(result))  # Display quotient as float with 2 decimal points
    except:
        entry_screen.delete(0, tk.END)
        entry_screen.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

outer_frame = tk.Frame(root, bg="#a6a6a6", padx=10, pady=10)
outer_frame.pack(expand=True, fill="both")

entry_screen = tk.Entry(outer_frame, font=("Arial", 20), bd=5, relief=tk.FLAT, justify="right")
entry_screen.pack(side=tk.TOP, expand=True, fill="both")

button_frame = tk.Frame(outer_frame)
button_frame.pack(expand=True, fill="both", padx=10, pady=10)  # Adjusted padding

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("*", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("%", 3, 2), ("/", 3, 3)
]

for (text, row, col) in buttons:
    btn = tk.Button(button_frame, text=text, font=("Arial", 16), bd=5, relief=tk.RAISED, command=lambda num=text: button_click(num))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button_frame.grid_columnconfigure(col, weight=1, uniform="equal")
    button_frame.grid_rowconfigure(row, weight=1)

clear_button = tk.Button(button_frame, text="C", font=("Arial", 16), bd=5, relief=tk.RAISED, command=clear_screen)
clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

backspace_button = tk.Button(button_frame, text="⌫", font=("Arial", 16), bd=5, relief=tk.RAISED, command=backspace)  # Added backspace button
backspace_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

calculate_button = tk.Button(button_frame, text="=", font=("Arial", 16), bd=5, relief=tk.RAISED, command=calculate)
calculate_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")  # Adjusted position of calculate button

root.mainloop()