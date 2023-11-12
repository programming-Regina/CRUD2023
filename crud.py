from tkinter import *
from tkinter import messagebox
import sqlite3 as sq3
import matplotlib.pyplot as plt

'''
************************
PARTE FUNCIONAL
************************
'''

# ***** MENU ******
def conectar():
    global con
    global cur
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    messagebox.showinfo("STATUS","Conectado a la BBDD")

def salir():
    resp = messagebox.askquestion("CONFIRME","¿Desea salir de la aplicación?")
    if resp == 'yes':
        con.close()
        raiz.destroy()

# GrÄFICAS
# Por escuelas
def alumnos_en_escuelas():
    query = '''SELECT COUNT(alumnos.legajo) AS "total", escuelas.nombre FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id GROUP BY escuelas.nombre ORDER BY total DESC'''
    cur.execute(query)
    resultado = cur.fetchall()
    #print(resultado)

    escuelas =[]
    cantidad = []
    for r in resultado:
        cantidad.append(r[0])
        escuelas.append(r[1])

    plt.bar(escuelas, cantidad)
    plt.xticks(rotation = 90)
    plt.show()

def alumnos_con_notas():
    query = '''SELECT COUNT(legajo) AS "total", nota FROM alumnos GROUP BY nota'''
    cur.execute(query)
    resultado = cur.fetchall()
    #print(resultado)

    nota =[]
    cantidad = []
    for r in resultado:
        cantidad.append(r[0])
        nota.append(r[1])

    plt.bar(nota, cantidad)
    #plt.xticks(rotation = 90)
    plt.show()

def limpiar():
    legajo.set("")
    apellido.set("")
    nombre.set("")
    email.set("")
    calificacion.set("")
    escuela.set("")
    localidad.set("")
    provincia.set("")
    legajo_input.config(state='normal')

def mostrar_licencia():
    msg = '''
    Sistema CRUD en Python
    Copyright (C) 2023 - Regina Molares para Codo a Codo 4.0
    Email: regina.molares@gmail.com\n=======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version.
    This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.
    '''
    messagebox.showinfo("LICENCIA", msg)


def acerca_de():
    messagebox.showinfo("ACERCA DE...","Creado por RNM\npara CaC 4.0 - Big Data\nNoviembre 2023 ")

def listar():
    class Tabla():
        def __init__(self,raiz2):
            nombre_cols = ['Legajo','Apellido','Nombre','Promedio','Escuela']
            for i in range(cant_cols):
                self.e=Entry(frameppal)
                self.e.config(bg='black', fg='white')
                self.e.grid(row=0, column=i)
                self.e.insert(END,nombre_cols[i])
            
            for fila in range(cant_filas):
                for cols in range(cant_cols):
                    self.e=Entry(frameppal)
                    self.e.grid(row=fila+1, column = cols)
                    self.e.insert(END, resultado[fila][cols])
                    self.e.config(state='readonly')
    
    raiz2=Tk()
    raiz2.title('Listado de alumnos')
    frameppal = Frame(raiz2)
    frameppal.pack(fill='both')
    framecerrar = Frame(raiz2)
    framecerrar.config(bg=color_letra)
    framecerrar.pack(fill='both')

    boton_cerrar = Button(framecerrar, text="CERRAR",command=raiz2.destroy)
    boton_cerrar.config(bg=color_boton, fg='white', pady=10, padx=0)
    boton_cerrar.pack(fill='both')

    # obtener los datos para el listado
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    query1 = '''
             SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, escuelas.nombre FROM alumnos INNER JOIN escuelas 
             ON alumnos.id_escuela = escuelas._id LIMIT 30   
             '''
    cur.execute(query1)
    resultado = cur.fetchall()
    cant_filas = len(resultado) # la cantidad de registros para saber cuántas filas
    cant_cols = len(resultado[0])

    tabla = Tabla(frameppal)
    con.close()
    raiz2.mainloop()

# ***** CRUD *****
# Crear
def crear():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = id_escuela, legajo.get(), apellido.get(),nombre.get(), calificacion.get(), email.get()
    cur.execute('INSERT INTO alumnos (id_escuela, legajo, apellido, nombre, nota, email) VALUES (?,?,?,?,?,?)', datos)
    con.commit()
    messagebox.showinfo("STATUS", "Registro agregado")
    limpiar()

# Buscar
def buscar_legajo():
    query2 = 'SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id WHERE alumnos.legajo='
    cur.execute(query2 + legajo.get())
    resultado = cur.fetchall()
    if resultado == []:
        messagebox.showerror("ERROR","Ese N° de legajo no existe")
        legajo.set("")
    else:
        for campo in resultado:
            legajo.set(campo[0])
            apellido.set(campo[1])
            nombre.set(campo[2])
            calificacion.set(campo[3])
            email.set(campo[4])
            escuela.set(campo[5])
            localidad.set(campo[6])
            provincia.set(campo[7])
            legajo_input.config(state='disabled')

# ACTUALIZAR
def actualizar():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = id_escuela, apellido.get(),nombre.get(), calificacion.get(), email.get()
    cur.execute('UPDATE alumnos SET id_escuela=?,apellido=?, nombre=?, nota=?, email=? WHERE legajo='+legajo.get() , datos)
    con.commit()
    messagebox.showinfo("STATUS", "Registro actualizado")
    limpiar()

# BORRAR
def borrar():
    resp=messagebox.askquestion("BORRAR","¿Desea eliminar el registro?")
    if resp == 'yes':
        cur.execute('DELETE FROM alumnos WHERE legajo =' + legajo.get())
        con.commit()
        messagebox.showinfo("STATUS","Registro eliminado")
        limpiar()

# OTRAS FX
def buscar_escuelas(actualiza):
    con = sq3.connect('mi_db.db')
    cur = con.cursor()
    if actualiza:
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre = ?',(escuela.get(),)) # , elemento fantasma de la tupla
    else: # esta opción es la que llena la lista de escuelas en el desplegable
        cur.execute('SELECT nombre FROM escuelas')

    resultado = cur.fetchall() # recibe una lista de tuplas de la bbdd
    retorno = [] #(nombre,)
    for e in resultado:
        if actualiza:
            localidad.set(e[1])
            provincia.set(e[2])
        esc = e[0]
        retorno.append(esc)
    con.close()
    return retorno



'''
************************
INTERFAZ GRÁFICA
************************
'''
# colores framecampos
color_fondo = 'plum'
color_letra = 'black'
# colores framebotones
fondo_framebotones = 'pink'
color_boton = 'black'
letra_boton = fondo_framebotones

# raíz
raiz = Tk()
raiz.title('GUI - CRUD')

# barramenu
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

# Menú BBDD
bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = 'Conectar con la BBDD', command=conectar)
bbddmenu.add_command(label = 'Mostrar listado alumnos', command=listar)
bbddmenu.add_command(label = 'Salir', command=salir)

# Menú estadísticas
estadmenu = Menu(barramenu, tearoff=0)
estadmenu.add_command(label='Cantidad de alumnos por escuela', command=alumnos_en_escuelas)
estadmenu.add_command(label='Desempeño estudiantil', command=alumnos_con_notas)


# Menú Limpiar
limpiarmenu = Menu(barramenu,tearoff=0)
limpiarmenu.add_command(label = 'Limpiar formulario', command=limpiar)

# Menú Acerca de...
ayudamenu = Menu(barramenu,tearoff=0)
ayudamenu.add_command(label='Licencia', command=mostrar_licencia)
ayudamenu.add_command(label='Acerca de...', command=acerca_de)

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Gráficas',menu=estadmenu)
barramenu.add_cascade(label='Limpiar',menu=limpiarmenu)
barramenu.add_cascade(label='Acerca de...', menu=ayudamenu)

# FRAMECAMPOS
framecampos = Frame(raiz)
framecampos.config(bg=color_fondo)
framecampos.pack(fill='both')

# CAMPOS ENTRY
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''
legajo=StringVar()
apellido=StringVar()
nombre=StringVar()
email=StringVar()
escuela=StringVar()
localidad=StringVar()
provincia=StringVar()
calificacion=DoubleVar()

def config_input(mi_input, fila):
    espaciado={'column':1, 'padx':10, 'pady':10, 'ipadx':50}
    mi_input.grid(row=fila,**espaciado)

legajo_input = Entry(framecampos, textvariable=legajo)
#legajo_input.grid(row=0, column=1, padx=10, pady=10, ipadx=50)
config_input(legajo_input,0)

apellido_input =  Entry(framecampos, textvariable=apellido)
config_input(apellido_input,1)

nombre_input =  Entry(framecampos, textvariable=nombre)
config_input(nombre_input,2)

email_input =  Entry(framecampos, textvariable=email)
config_input(email_input,3)

calificacion_input =  Entry(framecampos, textvariable=calificacion)
config_input(calificacion_input,4)

#escuela_input =  Entry(framecampos, textvariable=escuela)
#config_input(escuela_input,5)

lista = buscar_escuelas(False)
escuela.set('Seleccione')
escuela_option = OptionMenu(framecampos, escuela, *lista)
escuela_option.grid(row=5, column=1, padx=10, pady=10, sticky='w', ipadx=50)

localidad_input =  Entry(framecampos, textvariable=localidad)
config_input(localidad_input,6)

provincia_input =  Entry(framecampos, textvariable=provincia)
config_input(provincia_input,7)

#LABEL

'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

def config_label(mi_label, fila):
    espaciado_labels ={'column':0, 'sticky':'e', 'padx':10, 'pady':10}
    colores = {'bg':color_fondo, 'fg':color_letra}
    mi_label.grid(row=fila, **espaciado_labels)
    mi_label.config(**colores)

legajo_label =Label(framecampos, text='N° de Legajo')
config_label(legajo_label,0)

apellido_label =Label(framecampos, text='Apellido')
config_label(apellido_label,1)

nombre_label =Label(framecampos, text='Nombre')
config_label(nombre_label,2)

email_label =Label(framecampos, text='Email')
config_label(email_label,3)

promedio_label =Label(framecampos, text='Promedio')
config_label(promedio_label,4)

escuela_label =Label(framecampos, text='Escuela')
config_label(escuela_label,5)

localidad_label =Label(framecampos, text='Localidad')
config_label(localidad_label,6)

provincia_label =Label(framecampos, text='Provincia')
config_label(provincia_label,7)

# FRAMEBOTONES
framebotones = Frame(raiz)
framebotones.config(bg=fondo_framebotones)
framebotones.pack(fill='both')

def config_buttons(mi_button,columna):
    espaciado_buttons = {'row':0, 'padx':5, 'pady':10, 'ipadx':12}
    mi_button.config(bg=color_boton, fg=letra_boton)
    mi_button.grid(column=columna, **espaciado_buttons)

boton_crear = Button(framebotones, text='Crear', command=crear)
config_buttons(boton_crear,0)

boton_buscar = Button(framebotones, text='Buscar', command=buscar_legajo)
config_buttons(boton_buscar,1)

boton_actualizar = Button(framebotones, text='Actualizar', command=actualizar)
config_buttons(boton_actualizar,2)

boton_borrar = Button(framebotones, text='Eliminar', command=borrar)
config_buttons(boton_borrar,3)

# FRAME DEL PIE
framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy, text="(2023) por Regina N. Molares para CaC 4.0 - Big Data")
copylabel.config(bg='black',fg='white')
copylabel.grid(row=0, column=0, padx=10, pady=10)

raiz.mainloop()

