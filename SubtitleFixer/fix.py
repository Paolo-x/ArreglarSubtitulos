import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def arreglar_subtitulo():
    ruta = filedialog.askopenfilename(filetypes=[("Subtítulos", "*.srt")])
    
    if not ruta:
        return

    try:
        with open(ruta, "rb") as f:
            data = f.read()

       
        try:
            texto = data.decode("utf-8")
            usada = "utf-8 (ya estaba bien)"
        except:
            try:
                texto = data.decode("cp1252")
                usada = "cp1252"
            except:
                texto = data.decode("latin-1")
                usada = "latin-1"

        nueva_ruta = ruta.replace(".srt", "_FIXED.srt")

        with open(nueva_ruta, "w", encoding="utf-8") as f:
            f.write(texto)

        messagebox.showinfo("Listo", f"Codificación: {usada}\n\nGuardado en:\n{nueva_ruta}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def procesar_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Subtítulos", "*.srt")])
    
    if not ruta:
        return

    try:
        
        with open(ruta, "rb") as f:
            data = f.read()

        
        reemplazos = {
            b'\xe1': b'a',  # á
            b'\xe9': b'e',  # é
            b'\xed': b'i',  # í
            b'\xf3': b'o',  # ó
            b'\xfa': b'u',  # ú
            b'\xf1': b'n',  # ñ
            b'\xc1': b'A',
            b'\xc9': b'E',
            b'\xcd': b'I',
            b'\xd3': b'O',
            b'\xda': b'U',
            b'\xd1': b'N'
        }

        for original, reemplazo in reemplazos.items():
            data = data.replace(original, reemplazo)

        nueva_ruta = ruta.replace(".srt", "_SIN_TILDES.srt")

        
        with open(nueva_ruta, "wb") as f:
            f.write(data)

        messagebox.showinfo("Listo", f"Archivo guardado en:\n{nueva_ruta}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Subtitle Fixer PRO")
ventana.geometry("420x260")
ventana.update_idletasks()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto // 2)
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
ventana.resizable(False, False)
ventana.configure(bg="#121212")

style = ttk.Style(ventana)
style.theme_use("clam")

style.configure("TFrame", background="#121212")
style.configure("TLabel", background="#121212", foreground="#E0E0E0", font=("Segoe UI", 12))
style.configure("TButton",
                background="#1F1F1F",
                foreground="#FFFFFF",
                font=("Segoe UI", 11, "bold"),
                padding=10,
                borderwidth=0)
style.map("TButton",
          background=[("active", "#2A2A2A")],
          foreground=[("active", "#FFFFFF")])

contenedor = ttk.Frame(ventana, padding=20)
contenedor.pack(fill="both", expand=True)

titulo = ttk.Label(contenedor, text="Subtitle Fixer PRO", font=("Segoe UI", 16, "bold"))
titulo.pack(pady=(0, 16))

boton = ttk.Button(contenedor, text="Arreglar SRT corrompido", command=arreglar_subtitulo)
boton.pack(fill="x", pady=6)

boton2 = ttk.Button(contenedor, text="Solo borrar tildes", command=procesar_archivo)
boton2.pack(fill="x", pady=6)

nota = ttk.Label(contenedor, text="Compatible con archivos .srt", font=("Segoe UI", 9))
nota.pack(pady=(12, 0))

ventana.mainloop()