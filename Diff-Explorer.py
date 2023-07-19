import difflib
import tkinter as tk
from tkinter import filedialog, messagebox

def load_file(file_entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)

def compare_files():
    file_path1 = file_entry1.get()
    file_path2 = file_entry2.get()

    if not file_path1 or not file_path2:
        messagebox.showerror("Error", "Please select two files for comparison.")
        return

    with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2:
        diff = difflib.Differ().compare(file1.readlines(), file2.readlines())
        differences = '\n'.join(line for line in diff if line.startswith(('+', '-')) and not line.isspace())

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    for line in differences.splitlines():
        if line.startswith('-'):
            result_text.insert('end', line + '\n', 'deleted')
        elif line.startswith('+'):
            result_text.insert('end', line + '\n', 'added')

    result_text.tag_config('added', foreground='green')
    result_text.tag_config('deleted', foreground='red')

    result_text.config(state=tk.DISABLED)

def clear():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.config(state=tk.DISABLED)
    file_entry1.delete(0, tk.END)
    file_entry2.delete(0, tk.END)

root = tk.Tk()
root.title("File Comparison")

file_entry1 = tk.Entry(root, width=40)
file_entry1.pack(pady=10)

file_entry2 = tk.Entry(root, width=40)
file_entry2.pack(pady=5)

browse_button1 = tk.Button(root, text="Select Reference File", command=lambda: load_file(file_entry1))
browse_button1.pack()

browse_button2 = tk.Button(root, text="Select File to Compare", command=lambda: load_file(file_entry2))
browse_button2.pack()

compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=10)

result_text = tk.Text(root, wrap='word')
result_text.pack(expand=True, fill='both', padx=10, pady=5)

root.mainloop()
