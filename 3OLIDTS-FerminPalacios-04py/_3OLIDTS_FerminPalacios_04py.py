import tkinter as tk
from tkinter import messagebox
import re

def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

def guardar_valores():
    #obtener valores desde los entrys
    nombres= tbNombre.get()
    apellidos=tbApellidos.get()
    edad=tbEdad.get()
    estatura=tbEstatura.get()
    telefono=tbTelefono.get()
    ###obtener el genero de los radoobuttoms
    genero =""
    if var_genero.get()==1:
        genero="hombre"
    elif var_genero.get()==2:
        genero="mujer"
    
        ###validar que los campos tengan el formato correcto
    if (es_entero_valido(edad) and es_decimal_valido(estatura)and es_entero_valido_de_10_digitos(telefono)
        and es_texto_valido(nombres) and es_texto_valido(apellidos)):


        ###genera la cadena de caracteres
        datos= ("Nombres: "+ nombres + "\n" + "apellidos: " + apellidos + "\n"+"edad"+ edad + "anos\n" + "Estarura: " 
                + estatura +"\n"+"Telefonos: "+telefono+"\n")
        ###guarda los datos en un archivo txt
        with open ("3O2025.txt","a") as archivo:
            archivo.write(datos +"\n\n")
        ##mostra mensaje de confimarcion
        messagebox.showinfo("informacion", "datos guardados con exito: \n\n"+ datos )
        limpiar_campos()
    else:
        messagebox.showinfo("informacion", "por favor, ingrese datos válidos en los campos.")
        limpiar_campos()

def es_entero_valido(valor):
    try:
        int (valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) ==10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$",valor))


#creacion ventana
ventana = tk.Tk()
ventana.geometry("520x580")
ventana.title("formulario vr.01")
#crear variable para el radio buttom
var_genero = tk.IntVar()
#creacion de etiquetas y campos de entrada
lbNombre=tk.Label(ventana, text="Nombres: ")
lbNombre.pack()
tbNombre= tk.Entry()
tbNombre.pack()
lbApellidos=tk.Label (ventana, text="Apellidos: ")
lbApellidos.pack()
tbApellidos= tk.Entry()
tbApellidos.pack()
lbTelefono= tk.Label(ventana, text="TElefono: ")
lbTelefono.pack()
tbTelefono= tk.Entry()
tbTelefono.pack()
lbEdad= tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad=tk.Entry()
tbEdad.pack()
lbEstarura=tk.Label(ventana, text="Estarura: ")
lbEstarura.pack()
tbEstatura= tk.Entry()
tbEstatura.pack()
lbGenero= tk.Label(ventana, text="Genero: ")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()
##cracion de botones
btnBorrar=tk.Button(ventana, text="borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar= tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()


