import tkinter as tk

root = tk.Tk()
root.title("My first GUI")
root.geometry("400x400")

label = tk.Label(root, text="Hello", font=("arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()

root.mainloop()