from tkinter import *
import os
from PIL import Image, ImageTk

def obtener_imagen(nombre, ancho, alto):
    RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(RUTA_BASE, nombre)
    if os.path.exists(ruta_imagen):
        img = Image.open(ruta_imagen)
        img = img.resize((ancho, alto))
        return ImageTk.PhotoImage(img)

class header(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#F82A3E", height=230)
        self.__titulo = Label(self, text="Plantilla", font=("Arial", 32), bg="#F82A3E", fg="white")
        self.logo_img = obtener_imagen("images/logo.png", 230, 230)
        lbl_logo = Label(self, image=self.logo_img, compound="top", height=230, bg="#F82A3E")
        lbl_logo.grid(row=0, column=0)
        self.home_img = obtener_imagen("images/home.png", 140, 140)
        lbl_home = Button(self, image=self.home_img, height=230, bg="#F82A3E", relief="flat"
                          ,activebackground="#F82A3E")
        lbl_home.grid(row=0, column=1)
        self.__titulo.grid(row=0, column=2, padx=350)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo):
        self.__titulo.config(text=nuevo)

class mainVentas(Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.controlador = controlador
        head = header(self)
        head.titulo = "Ventas"
        head.pack(fill="x")

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventas")
        self.state('zoomed')
        self.geometry("1024x720")
        self.pantallas = {}
        self.pantallas["Ventas_Main"] = mainVentas(self, self)
        self.mostrar_pantalla("Ventas_Main")

    def mostrar_pantalla(self, nombre):
        for pantalla in self.pantallas.values():
            pantalla.pack_forget()
        self.pantallas[nombre].pack(expand=True, fill="both")


if __name__ == "__main__":
    app = App()
    app.mainloop()
