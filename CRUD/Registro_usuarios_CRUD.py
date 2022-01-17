from tkinter import *
from tkinter import messagebox
import sqlite3

#-----------funciones------------------

def conexion_bd():
    mi_conexion=sqlite3.connect('Usuarios')

    mi_cursor=mi_conexion.cursor()


    try:
        mi_cursor.execute('''
            CREATE TABLE DATOUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCIÓN VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')

        messagebox.showinfo('BBDD', 'BBDD creada con éxito')

    except:
        messagebox.showwarning('¡Atención!','La BBDD ya existe')


def salir():
    valor=messagebox.askquestion('Salir','¿Desea salir de la aplicación?')

    if valor=='yes':
        root.destroy()

def limpiar():
    mi_nombre.set('')
    mi_nombre.set('')
    mi_apellido.set('')
    mi_direccion.set('')
    mi_pass.set('')
    cuadro_comentario.delete(1.0, END)

def crear():
    mi_conexion=sqlite3.connect('Usuarios')

    mi_cursor=mi_conexion.cursor()
    datos=mi_nombre.get(),mi_pass.get(),mi_apellido.get(),mi_direccion.get(),cuadro_comentario.get('1.0', END)

    mi_cursor.execute('INSERT INTO DATOUSUARIOS VALUES(NULL,?,?,?,?,?)',(datos))


    mi_conexion.commit()

    messagebox.showinfo('BBDD','Registro insertado con éxito')


def leer():
    mi_conexion=sqlite3.connect('Usuarios')

    mi_cursor=mi_conexion.cursor()

    mi_cursor.execute('SELECT * FROM DATOUSUARIOS WHERE ID=' + mi_id.get())

    el_usuario=mi_cursor.fetchall()

    for usuario in el_usuario:
        mi_id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_pass.set(usuario[2])
        mi_direccion.set(usuario[3])
        mi_apellido.set(usuario[4])
        cuadro_comentario.insert(1.0,usuario[5])

    mi_conexion.commit()

def actualizar():
    mi_conexion=sqlite3.connect('Usuarios')

    mi_cursor=mi_conexion.cursor()

    """mi_cursor.execute('UPDATE DATOUSUARIOS SET NOMBRE_USUARIO="' + mi_nombre.get()+
    '", PASSWORD="'+ mi_pass.get()+
    '", DIRECCIÓN="'+ mi_direccion.get()+
    '", APELLIDO="'+ mi_apellido.get()+
    '", COMENTARIOS="'+ cuadro_comentario.get('1.0', END)+
    '" WHERE ID=' + mi_id.get())"""

    mi_cursor.execute('UPDATE DATOUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCIÓN=?, COMENTARIOS=?' +
    'WHERE ID=' + mi_id.get(),(datos))


    mi_conexion.commit()

    messagebox.showinfo('BBDD','Registro actualizado con éxito')


def eliminar():
    mi_conexion=sqlite3.connect('Usuarios')

    mi_cursor=mi_conexion.cursor()

    mi_cursor.execute('DELETE FROM DATOUSUARIOS WHERE ID =' + mi_id.get())

    mi_conexion.commit()

    messagebox.showinfo('BBDD', 'Registro borrado con éxito')


#---------------------------menú-------------------------------
root=Tk()


barra_menu=Menu(root)
root.config(menu=barra_menu,width=300,height=300)

bbdd_menu=Menu(barra_menu,tearoff=0)
bbdd_menu.add_command(label='Conectar',command=conexion_bd)
bbdd_menu.add_command(label='Salir',command=salir)

borrar_menu=Menu(barra_menu,tearoff=0)
borrar_menu.add_command(label='Borrar campos',command=limpiar)

crud_menu=Menu(barra_menu,tearoff=0)
crud_menu.add_command(label='Crear', command=crear)
crud_menu.add_command(label='Leer', command=leer)
crud_menu.add_command(label='Actualizar',command=actualizar)
crud_menu.add_command(label='Borrar',command=eliminar)


ayuda_menu=Menu(barra_menu,tearoff=0)
ayuda_menu.add_command(label='Licencia')
ayuda_menu.add_command(label='Acerca de...')

barra_menu.add_cascade(label='BBDD',menu=bbdd_menu)
barra_menu.add_cascade(label='Borrar',menu=borrar_menu)
barra_menu.add_cascade(label='CRUD',menu=crud_menu)
barra_menu.add_cascade(label='Ayuda',menu=ayuda_menu)

#----------campos-------------------------------------------
frame=Frame(root,width=600,height=300)
frame.pack()

mi_id=StringVar()
mi_nombre=StringVar()
mi_pass=StringVar()
mi_direccion=StringVar()
mi_apellido=StringVar()

cuadro_id=Entry(frame,textvariable=mi_id)
cuadro_id.grid(row=0,column=1,padx=10,pady=10)
id_label=Label(frame,text='Id:')
id_label.grid(row=0,column=0,padx=10,pady=10)

cuadro_nombre=Entry(frame,textvariable=mi_nombre)
cuadro_nombre.grid(row=1,column=1,padx=10,pady=10)
nombre_label=Label(frame,text='Nombre:')
nombre_label.grid(row=1,column=0,padx=10,pady=10)

cuadro_pass=Entry(frame,textvariable=mi_pass)
cuadro_pass.grid(row=2,column=1,padx=10,pady=10)
cuadro_pass.config(show='*')
pass_label=Label(frame,text='Password:')
pass_label.grid(row=2,column=0,padx=10,pady=10)


cuadro_apellido=Entry(frame,textvariable=mi_apellido)
cuadro_apellido.grid(row=3,column=1,padx=10,pady=10)
apellido_label=Label(frame,text='Apellido:')
apellido_label.grid(row=3,column=0,padx=10,pady=10)

cuadro_direccion=Entry(frame,textvariable=mi_direccion)
cuadro_direccion.grid(row=4,column=1,padx=10,pady=10)
direccion_label=Label(frame,text='Dirección:')
direccion_label.grid(row=4,column=0,padx=10,pady=10)

cuadro_comentario=Text(frame,width=16,height=5)
cuadro_comentario.grid(row=5,column=1)
comentario_label=Label(frame,text='Comentarios:')
comentario_label.grid(row=5,column=0,padx=10,pady=10)
scrollbar=Scrollbar(frame,command=cuadro_comentario.yview)
scrollbar.grid(row=5,column=2,sticky='nsew')

cuadro_comentario.config(yscrollcommand=scrollbar.set)

#--------------botones------------------

frame2=Frame(root)
frame2.pack()

boton_crear=Button(frame2,text='Create',command=crear)
boton_crear.grid(row=1,column=0,padx=10,pady=10)

boton_leer=Button(frame2,text='Read',command=leer)
boton_leer.grid(row=1,column=1,padx=10,pady=10)

boton_actualizar=Button(frame2,text='Update',command=actualizar)
boton_actualizar.grid(row=1,column=2,padx=10,pady=10)

boton_borrar=Button(frame2,text='Delete',command=eliminar)
boton_borrar.grid(row=1,column=3,padx=10,pady=10)







root.mainloop()
