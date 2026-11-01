import tkinter as tk

root = tk.Tk()
root.title("KASIR")
root.geometry("500x500")

label = tk.Label(root, text="KASIR TOKO")
label.grid(row=0, column=0, columnspan=3)

tk.Label(root, text="username").grid(row=0, column=0)
tk.Label(root, text="full name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(root, text="Male", variable=var1).grid(row=10, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=11, sticky=tk.W)

v = tk.IntVar()

tk.Radiobutton(root, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).pack(anchor=tk.W)


button = tk.Button(root, text="LOGIN", width=25, command=root.destroy)
button.grid(row=2, column=0, columnspan=3)

root.mainloop()