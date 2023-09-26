import tkinter as tk
from tkinter import ttk, messagebox
from model.series import crear_tabla, borrar_tabla
from model.series import Series, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=500, height=500)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="administracion de database", menu=menu_inicio)

    menu_inicio.add_command(label="crear series en db", command=crear_tabla)
    menu_inicio.add_command(label="eliminar series en db", command=borrar_tabla)
    menu_inicio.add_command(label="salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=400, height=400)
        self.root = root
        self.pack()

        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(2, weight=0)
        self.id_serie = None

        self.campos_peliculas()
        self.desabilitar_campos()
        self.tabla_series()

    def campos_peliculas(self):
        self.label_titulo = tk.Label(self, text="Título:")
        self.label_titulo.config(font=("arial", 12, "bold"))
        self.label_titulo.grid(row=0, column=0)

        self.mi_titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self, textvariable=self.mi_titulo)
        self.entry_titulo.config(width=10, state="disabled", font=("arial", 12, "bold"))
        self.entry_titulo.grid(row=0, column=1, columnspan=1)

        self.label_descripcion = tk.Label(self, text="Descripción:")
        self.label_descripcion.config(font=("arial", 12, "bold"))
        self.label_descripcion.grid(row=1, column=0)

        self.mi_descripcion = tk.StringVar()
        self.entry_descripcion = tk.Entry(self, textvariable=self.mi_descripcion)
        self.entry_descripcion.config(
            width=10, state="disabled", font=("arial", 12, "bold")
        )
        self.entry_descripcion.grid(row=1, column=1, columnspan=1)

        self.label_fecha_estreno = tk.Label(self, text="Fecha de Estreno:")
        self.label_fecha_estreno.config(font=("arial", 12, "bold"))
        self.label_fecha_estreno.grid(row=2, column=0)

        self.mi_fecha_estreno = tk.StringVar()
        self.entry_fecha_estreno = tk.Entry(self, textvariable=self.mi_fecha_estreno)
        self.entry_fecha_estreno.config(
            width=10, state="disabled", font=("arial", 12, "bold")
        )
        self.entry_fecha_estreno.grid(row=2, column=1, columnspan=1)

        self.label_estrellas = tk.Label(self, text="Estrellas:")
        self.label_estrellas.config(font=("arial", 12, "bold"))
        self.label_estrellas.grid(row=0, column=2)

        self.mi_estrellas = tk.StringVar()
        self.entry_estrellas = tk.Entry(self, textvariable=self.mi_estrellas)
        self.entry_estrellas.config(
            width=10, state="disabled", font=("arial", 12, "bold")
        )
        self.entry_estrellas.grid(row=0, column=3, columnspan=1)

        self.label_genero = tk.Label(self, text="Género:")
        self.label_genero.config(font=("arial", 12, "bold"))
        self.label_genero.grid(row=1, column=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=10, state="disabled", font=("arial", 12, "bold"))
        self.entry_genero.grid(row=1, column=3, columnspan=1)

        self.label_precio_alquiler = tk.Label(self, text="Precio Alquiler:")
        self.label_precio_alquiler.config(font=("arial", 12, "bold"))
        self.label_precio_alquiler.grid(row=2, column=2)

        self.mi_precio_alquiler = tk.StringVar()
        self.entry_precio_alquiler = tk.Entry(
            self, textvariable=self.mi_precio_alquiler
        )
        self.entry_precio_alquiler.config(
            width=10, state="disabled", font=("arial", 12, "bold")
        )
        self.entry_precio_alquiler.grid(row=2, column=3, columnspan=1)

        self.label_atp = tk.Label(self, text="ATP:")
        self.label_atp.config(font=("arial", 12, "bold"))
        self.label_atp.grid(row=0, column=4)

        self.mi_atp = tk.BooleanVar()
        self.check_atp = tk.Checkbutton(self, variable=self.mi_atp)
        self.check_atp.config(font=("arial", 12, "bold"))
        self.check_atp.grid(row=0, column=5, columnspan=1)

        self.label_estado = tk.Label(self, text="ESTADO:")
        self.label_estado.config(font=("arial", 12, "bold"))
        self.label_estado.grid(row=1, column=4)

        self.mi_estado = tk.StringVar()
        self.entry_estado = tk.Entry(self, textvariable=self.mi_estado)
        self.entry_estado.config(width=10, state="disabled", font=("arial", 12, "bold"))
        self.entry_estado.grid(row=1, column=5, columnspan=1)

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(
            width=20,
            font=("arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#190714",
            cursor="hand2",
            activebackground="#848484",
        )
        self.boton_nuevo.grid(row=3, column=0, columnspan=3)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            width=20,
            font=("arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#190714",
            cursor="hand2",
            activebackground="#848484",
        )
        self.boton_guardar.grid(row=3, column=1, columnspan=3)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.desabilitar_campos
        )
        self.boton_cancelar.config(
            width=20,
            font=("arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#190714",
            cursor="hand2",
            activebackground="#848484",
        )
        self.boton_cancelar.grid(row=3, column=2, columnspan=3)

    def habilitar_campos(self):
        self.mi_titulo.set("")
        self.mi_descripcion.set("")
        self.mi_fecha_estreno.set("")
        self.mi_estrellas.set("")
        self.mi_genero.set("")
        self.mi_precio_alquiler.set("")
        self.mi_estado.set("")

        self.entry_titulo.config(state="normal")
        self.entry_descripcion.config(state="normal")
        self.entry_fecha_estreno.config(state="normal")
        self.entry_estrellas.config(state="normal")
        self.entry_genero.config(state="normal")
        self.entry_precio_alquiler.config(state="normal")
        self.entry_estado.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def desabilitar_campos(self):
        self.id_serie = None
        self.mi_titulo.set("")
        self.mi_descripcion.set("")
        self.mi_fecha_estreno.set("")
        self.mi_estrellas.set("")
        self.mi_genero.set("")
        self.mi_precio_alquiler.set("")
        self.mi_estado.set("")

        self.entry_titulo.config(state="disabled")
        self.entry_descripcion.config(state="disabled")
        self.entry_fecha_estreno.config(state="disabled")
        self.entry_estrellas.config(state="disabled")
        self.entry_genero.config(state="disabled")
        self.entry_precio_alquiler.config(state="disabled")
        self.entry_estado.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        serie = Series(
            self.mi_titulo.get(),
            self.mi_descripcion.get(),
            self.mi_fecha_estreno.get(),
            self.mi_estrellas.get(),
            self.mi_genero.get(),
            self.mi_precio_alquiler.get(),
            self.mi_atp.get(),
            self.mi_estado.get(),
        )
        if self.id_serie is None:
            guardar(serie)
        else:
            editar(serie, self.id_series)
        self.tabla_series()
        self.desabilitar_campos()

    def tabla_series(self):
        self.lista_series = listar()
        self.lista_series.reverse()

        self.tabla = ttk.Treeview(
            self,
            column=(
                "Titulo",
                "Descripcion",
                "Fecha de estreno",
                "Estrellas",
                "Genero",
                "Precio_alquiler",
                "Atp",
                "Estado"
            ),
        )
        self.tabla.grid(row=4, column=0, columnspan=8, sticky="nse")

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=4, column=6, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="TITULO")
        self.tabla.heading("#2", text="DESCRIPCION")
        self.tabla.heading("#3", text="FECHA DE ESTRENO")
        self.tabla.heading("#4", text="ESTRELLAS")
        self.tabla.heading("#5", text="GENERO")
        self.tabla.heading("#6", text="PRECIO ALQUILER")
        self.tabla.heading("#7", text="ATP")
        self.tabla.heading("#8", text="ESTADO")


        for p in self.lista_series:
            self.tabla.insert("",0,text=p[0],values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]),
            )

        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(
            width=20,
            font=("arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#190714",
            cursor="hand2",
            activebackground="#848484",
        )
        self.boton_editar.grid(row=5, column=0, columnspan=4)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_datos
        )
        self.boton_eliminar.config(
            width=20,
            font=("arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#190714",
            cursor="hand2",
            activebackground="#848484",
        )
        self.boton_eliminar.grid(row=5, column=1, columnspan=4)

    def editar_datos(self):
        try:
            self.id_serie = self.tabla.item(self.tabla.selection())["text"]
            self.mi_titulo = self.tabla.item(self.tabla.selection())["values"][0]
            self.mi_descripcion = self.tabla.item(self.tabla.selection())["values"][1]
            self.mi_fecha_estreno = self.tabla.item(self.tabla.selection())["values"][2]
            self.mi_estrellas = self.tabla.item(self.tabla.selection())["values"][3]
            self.mi_genero = self.tabla.item(self.tabla.selection())["values"][4]
            self.mi_precio_alquiler = self.tabla.item(self.tabla.selection())["values"][
                5
            ]
            self.mi_estado = self.tabla.item(self.tabla.selection())["values"][6]

            self.habilitar_campos()

            self.entry_titulo.insert(0, self.mi_titulo)
            self.entry_descripcion.insert(0, self.mi_descripcion)
            self.entry_fecha_estreno.insert(0, self.mi_fecha_estreno)
            self.entry_estrellas.insert(0, self.mi_estrellas)
            self.entry_genero.insert(0, self.mi_genero)
            self.entry_precio_alquiler.insert(0, self.mi_precio_alquiler)
            self.entry_estado.insert(0, self.mi_estado)

        except:
            titulo = "Edicion de datos"
            mensaje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_serie = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_serie)
            self.tabla_series()
            self.id_serie = None
        except:
            titulo = "Eliminar un registro"
            mensaje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
