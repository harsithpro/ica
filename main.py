import tkinter as tk
from tkinter import ttk
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        interest = (principal * rate * time) / 100
        result_label["text"] = f"Simple Interest: {interest:.2f}"
    except ValueError:
        result_label["text"] = "Invalid Input! Please enter numbers only."
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("500x500")
root.resizable(True, True)
tk.Label(root, text="Principal Amount (P):", font=("Arial", 12)).pack(pady=5)
principal_entry = ttk.Entry(root, font=("Arial", 12))
principal_entry.pack(pady=5)
tk.Label(root, text="Annual Interest Rate (%):", font=("Arial", 12)).pack(pady=5)
rate_entry = ttk.Entry(root, font=("Arial", 12))
rate_entry.pack(pady=5)
tk.Label(root, text="Time (Years):", font=("Arial", 12)).pack(pady=5)
time_entry = ttk.Entry(root, font=("Arial", 12))
time_entry.pack(pady=5)
calculate_button = ttk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)
root.mainloop()