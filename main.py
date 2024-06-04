import tkinter as tk
from tkinter import ttk
from functions import kirilldan_lotinga, lotindan_kirillga


def convert_to_kirill():
    input_text = input_textbox.get("1.0", tk.END).strip()
    output_text = lotindan_kirillga(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output_text)


def convert_to_lotin():
    input_text = input_textbox.get("1.0", tk.END).strip()
    output_text = kirilldan_lotinga(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output_text)

root = tk.Tk()
root.title("Lotin-Kirill konvertori")

# Kirish matni uchun yozuv maydoni
input_label = ttk.Label(root, text="Matnni kiriting:")
input_label.pack(pady=5)
input_textbox = tk.Text(root, height=10, width=50)
input_textbox.pack(pady=5)

# Kirillga o'tkazish tugmasi
to_kirill_button = ttk.Button(root, text="Kirillga o'tkazish", command=convert_to_kirill)
to_kirill_button.pack(pady=5)

# Lotinga o'tkazish tugmasi
to_lotin_button = ttk.Button(root, text="Lotinga o'tkazish", command=convert_to_lotin)
to_lotin_button.pack(pady=5)

# Natija matni uchun yozuv maydoni
output_label = ttk.Label(root, text="Natija:")
output_label.pack(pady=5)
output_textbox = tk.Text(root, height=10, width=50)
output_textbox.pack(pady=5)

# Tkinter oynasini ishga tushirish
root.mainloop()
