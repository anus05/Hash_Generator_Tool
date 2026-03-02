import hashlib
import tkinter as tk
from tkinter import messagebox

def generate_hash():
    text = entry.get()
    algo = algorithm.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text!")
        return

    if algo == "MD5":
        hash_obj = hashlib.md5(text.encode())
    elif algo == "SHA-1":
        hash_obj = hashlib.sha1(text.encode())
    elif algo == "SHA-256":
        hash_obj = hashlib.sha256(text.encode())
    elif algo == "SHA-512":
        hash_obj = hashlib.sha512(text.encode())
    else:
        messagebox.showerror("Error", "Select Algorithm!")
        return

    result.set(hash_obj.hexdigest())

# Main Window
root = tk.Tk()
root.title("Hash Generator Tool")
root.geometry("500x350")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Hash Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Input Field
tk.Label(root, text="Enter Text:").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Algorithm Selection
algorithm = tk.StringVar()
algorithm.set("SHA-256")

tk.Label(root, text="Select Algorithm:").pack(pady=5)

tk.Radiobutton(root, text="MD5", variable=algorithm, value="MD5").pack()
tk.Radiobutton(root, text="SHA-1", variable=algorithm, value="SHA-1").pack()
tk.Radiobutton(root, text="SHA-256", variable=algorithm, value="SHA-256").pack()
tk.Radiobutton(root, text="SHA-512", variable=algorithm, value="SHA-512").pack()

# Generate Button
tk.Button(root, text="Generate Hash", command=generate_hash, bg="black", fg="white").pack(pady=10)

# Output Field
result = tk.StringVar()
tk.Label(root, text="Generated Hash:").pack()
tk.Entry(root, textvariable=result, width=60).pack(pady=5)

root.mainloop()