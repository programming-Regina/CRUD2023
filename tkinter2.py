from tkinter import *
from tkinter import messagebox # mensaje x ventana emergente

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
bbddmenu.add_command(label = 'Conectar con la BBDD')
bbddmenu.add_command(label = 'Salir')

# Menú Limpiar
limpiarmenu = Menu(barramenu,tearoff=0)
limpiarmenu.add_command(label = 'Limpiar formulario')

# Menú Acerca de...
ayudamenu = Menu(barramenu,tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de...')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
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

escuela_input =  Entry(framecampos, textvariable=escuela)
config_input(escuela_input,5)

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

boton_crear = Button(framebotones, text='Crear')
config_buttons(boton_crear,0)

boton_buscar = Button(framebotones, text='Buscar')
config_buttons(boton_buscar,1)

boton_actualizar = Button(framebotones, text='Actualizar')
config_buttons(boton_actualizar,2)

boton_borrar = Button(framebotones, text='Eliminar')
config_buttons(boton_borrar,3)

# FRAME DEL PIE
framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy, text="(2023) por Regina N. Molares para CaC 4.0 - Big Data")
copylabel.config(bg='black',fg='white')
copylabel.grid(row=0, column=0, padx=10, pady=10)

raiz.mainloop()
