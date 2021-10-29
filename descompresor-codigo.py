import os
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox, filedialog

def crearWidgets():

    copy = Label(ventana, text = "Programa por Doble R", fg = "white", bg = "black").place(x= 500, y = 380)

    #Descomprimir
    unzipArchLabel = Label(ventana, text = "Objeto que descomprimes: ",fg = "white", bg = "black", font=("Arial 12"))
    unzipArchLabel.grid(row = 0, column = 0, padx = 5, pady = 5)

    ventana.unzipEntry = Text(ventana, height = 2, width = 45, font = ("Arial",10))
    ventana.unzipEntry.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

    #Boton para navegar
    botonnavegar = Button(ventana, text = "Navergar", fg = "white",bg = "black", width = 5, height = 2, command = unzipnavegar)
    botonnavegar.grid(row = 0, column = 3, padx = 5, pady = 5)
    #Boton para navegar

    #Nombre del archico a descomprimir
    nombredelarchivo = Label(ventana, text = "Nombre de la carpeta: ", bg = "black", fg = "white", font=("Arial 12"))
    nombredelarchivo.grid(row = 1, column = 0, padx = 5, pady = 5)
    #Nombre del archivo a descomprimir

    #Entrada del nombre del archivo
    ventana.unzipNombreEntrada = Entry(ventana, width = 35, font=("Arial 12"))
    ventana.unzipNombreEntrada.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)
    #Entrada del nombre del archivo

    #Boton de descomprimir
    descomprimir = Button(ventana, text = "Descomprimir", fg ="white", bg = "black", width = 9, height = 2, command = unzipArchivos)
    descomprimir.grid(row = 1, column = 3, padx = 5, pady = 5)

    #Boton cerar
    cerrar = Button(ventana, text = "Cerrar", bg = "black", fg = "white", width = 5, height = 2, command = closed)
    cerrar.place(x=5, y = 350)

def unzipnavegar():
    ventana.unzipArchivoLista = filedialog.askopenfilename(initialdir = "/home/marck/Downloads/Compressed")
    ventana.unzipEntry.insert("1.0", "Los siguientes objetos serán descomprimidos \n")
    ventana.archivos = os.path.basename(ventana.unzipArchivoLista)
    ventana.unzipEntry.insert("2.0", ventana.archivos+"\n")
    ventana.unzipEntry.config(state=DISABLED)

def closed():
    ventana.destroy()

def unzipArchivos():
    #creando la carpeta con el nombre asignado
    os.makedirs(ventana.unzipNombreEntrada.get())

    #Abrir el archivo
    with ZipFile(ventana.unzipArchivoLista, "r") as UNzip1:
        #Extraer archivo
        UNzip1.extractall(ventana.unzipNombreEntrada.get())

    #MOstrar el aviso xd
    messagebox.showinfo("¡GENIAL!", "Objetos descomprimidos de forma exitosa")


ventana = tk.Tk()
ventana.title("Descompresor v1.0")
ventana.configure(background = "black")
ventana.minsize(width = 640, height = 400)
ventana.maxsize(width = 640, height = 400)
crearWidgets()







ventana.mainloop()
