import tkinter as tk
from tkinter import ttk, messagebox

# Setup awal
root = tk.Tk()
root.title("Form Identitas Mahasiswa")
root.geometry("450x470")

# Tema warna (Tugas 2)
bg_color = "#e6f2ff"  # Biru muda
fg_color = "#1a1a1a"  # Hitam keabu-abuan
root.configure(bg=bg_color)
root.columnconfigure(0, weight=1)  # Biar konten ke tengah

# Header
tk.Label(
    root, text="FORM IDENTITAS MAHASISWA",
    font=("Arial", 14, "bold"), bg=bg_color, fg=fg_color
).grid(row=0, column=0, pady=15)

form = tk.Frame(root, bg=bg_color)
form.grid(row=1, column=0, pady=5)

# Input Nama
tk.Label(form, text="Nama", bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
nama = tk.Entry(form, width=30)
nama.grid(row=0, column=1, pady=5, padx=5)

# Input NIM
tk.Label(form, text="NIM", bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="w", pady=5)
nim = tk.Entry(form, width=30)
nim.grid(row=1, column=1, pady=5, padx=5)

# Input Prodi
tk.Label(form, text="Program Studi", bg=bg_color, fg=fg_color).grid(row=2, column=0, sticky="w", pady=5)
prodi = ttk.Combobox(
    form, values=["Informatika", "Manajemen", "Akuntansi"],
    state="readonly", width=27
)
prodi.grid(row=2, column=1, pady=5, padx=5)

# Input Alamat pakai widget Text (Tugas 1)
tk.Label(form, text="Alamat", bg=bg_color, fg=fg_color).grid(row=3, column=0, sticky="nw", pady=5)
alamat = tk.Text(form, width=30, height=4)
alamat.grid(row=3, column=1, pady=5, padx=5)

# Label Hasil
hasil = tk.Label(root, text="", bg=bg_color, fg=fg_color, justify="left")
hasil.grid(row=2, column=0, pady=10)


# Fungsi Simpan dengan Validasi (Tugas 3)
def simpan():
    # Cek input kosong (termasuk kalau cuma diisi spasi)
    if not nama.get().strip() or not nim.get().strip():
        messagebox.showwarning("Peringatan", "Nama dan NIM tidak boleh kosong!")
        return

    alamat_text = alamat.get("1.0", tk.END).strip()

    hasil.config(
        text=f"Nama: {nama.get()}\n"
             f"NIM: {nim.get()}\n"
             f"Program Studi: {prodi.get()}\n"
             f"Alamat: {alamat_text}"
    )


# Fungsi Reset
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="")


# Frame Tombol (Tugas 4)
tombol = tk.Frame(root, bg=bg_color)
tombol.grid(row=3, column=0, pady=10)

# Tombol pakai grid
tk.Button(tombol, text="Simpan", command=simpan, width=8, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(tombol, text="Reset", command=reset, width=8, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)

# Tombol Keluar (Tugas 5)
tk.Button(tombol, text="Keluar", command=root.destroy, width=8, bg="#555555", fg="white").grid(row=0, column=2, padx=5)

root.mainloop()