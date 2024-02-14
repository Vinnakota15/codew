import tkinter as tk
import random
import string

def generate_password(strength, length):
    if strength == "weak":
        characters = string.ascii_letters + string.digits
    elif strength == "medium":
        characters = string.ascii_letters + string.digits + "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation + "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    length_entry.config(state=tk.DISABLED)
    strength_menu.config(state=tk.DISABLED)
    generate_button.config(state=tk.DISABLED)
    
    strength = strength_var.get()
    length = int(length_entry.get())
    password = generate_password(strength, length)
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state=tk.DISABLED)
    
    ok_button.config(state=tk.NORMAL)
    regenerate_button.config(state=tk.NORMAL)

def regenerate():
    length_entry.config(state=tk.DISABLED)
    strength_menu.config(state=tk.DISABLED)
    generate_button.config(state=tk.DISABLED)
    
    strength = strength_var.get()
    length = int(length_entry.get())
    password = generate_password(strength, length)
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state=tk.DISABLED)
    
    ok_button.config(state=tk.NORMAL)

def edit_length():
    length_entry.config(state=tk.NORMAL)
    strength_menu.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)
    password_entry.config(state=tk.NORMAL)
    ok_button.config(state=tk.DISABLED)
    regenerate_button.config(state=tk.DISABLED)

def clear_screen():
    length_entry.config(state=tk.NORMAL)
    strength_menu.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)
    password_entry.config(state=tk.NORMAL)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    ok_button.config(state=tk.DISABLED)
    regenerate_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create entry to display generated password
password_entry = tk.Entry(root, width=50, state=tk.DISABLED)
password_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10))

# Create label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=5)

# Create label and entry for password strength
strength_label = tk.Label(root, text="Password Strength:")
strength_label.grid(row=2, column=0, padx=10, pady=5)

strength_var = tk.StringVar()
strength_var.set("weak")

strength_options = ["weak", "medium", "strong"]
strength_menu = tk.OptionMenu(root, strength_var, *strength_options)
strength_menu.grid(row=2, column=1, padx=10, pady=5)

# Create button to generate password
generate_button = tk.Button(root, text="Generate", command=generate, width=10)
generate_button.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="e")

# Create buttons for edit length, regenerate, and clear screen
edit_button = tk.Button(root, text="Edit", command=edit_length, width=10)
edit_button.grid(row=3, column=1, padx=(5, 20), pady=5, sticky="w")

regenerate_button = tk.Button(root, text="Regenerate", command=regenerate, width=10)
regenerate_button.grid(row=4, column=0, padx=(20, 5), pady=5, sticky="e")

ok_button = tk.Button(root, text="OK", command=clear_screen, state=tk.DISABLED, width=10)
ok_button.grid(row=4, column=1, padx=(5, 20), pady=5, sticky="w")

# Configure row weights
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()