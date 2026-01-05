import tkinter as tk
def check_strength():
    password = entry.get()
    score = 0
    special_chars = "!@#$%^&*"

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in special_chars for c in password):
        score += 1

    if score == 5:
        result_label.config(text="STRONG ", fg="green")
        root.configure(bg="#1b5e20")   # dark green
    elif score >= 3:
        result_label.config(text="MEDIUM ", fg="orange")
        root.configure(bg="#ff9800")   # orange
    else:
        result_label.config(text="LOW ", fg="red")
        root.configure(bg="#b71c1c")   # red


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        eye_btn.config(text="🙈")
    else:
        entry.config(show="*")
        eye_btn.config(text="👁️")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x260")
root.configure(bg="#1e1e2f")


title = tk.Label(
    root,
    text="🔐 Password Strength Checker",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)


entry_frame = tk.Frame(root, bg="#1e1e2f")
entry_frame.pack(pady=10)


entry = tk.Entry(entry_frame, show="*", font=("Arial", 12), width=22)
entry.pack(side="left")

eye_btn = tk.Button(
    entry_frame,
    text="👁️",
    font=("Arial", 12),
    command=toggle_password
)
eye_btn.pack(side="left", padx=5)


check_btn = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=check_strength
)
check_btn.pack(pady=10)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    bg=root["bg"]
)
result_label.pack(pady=10)

root.mainloop()
