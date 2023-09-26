from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    # id_series INTEGER PRIMARY KEY AUTOINCREMENT,
    sql = '''
    CREATE TABLE series (
    id_series IINTEGER,
    titulo VARCHAR(100),
    descripcion TEXT,
    fecha_estreno DATE,
    estrellas INTEGER,
    genero VARCHAR(100),
    precio_alquiler DECIMAL,
    atp BOOLEAN,
    estado VARCHAR(2),
    PRIMARY KEY(id_series AUTOINCREMENT)
)
'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE series'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar registro'
        mensaje = 'Se borro la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except: 
        titulo = 'Borrar registro'
        mensaje = 'No hay tabla para borrar '
        messagebox.showerror(titulo, mensaje)

class Series:
    def __init__(self, titulo, descripcion, fecha_estreno, estrellas, genero, precio_alquiler, atp, estado):
        self.id_series = None
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_estreno = fecha_estreno
        self.estrellas = estrellas
        self.genero = genero
        self.precio_alquiler = precio_alquiler
        self.atp = atp
        self.estado = estado

    def __str__(self):
        return f'Series[{self.titulo}, {self.descripcion}, {self.fecha_estreno}, {self.estrellas}, {self.genero}, {self.precio_alquiler}, {self.atp}, {self.estado}]'
    
def guardar(series):
    conexion = ConexionDB()

    sql = f"""INSERT INTO series (titulo, descripcion, fecha_estreno, estrellas, genero, precio_alquiler, atp, estado)
    VALUES('{series.titulo}', '{series.descripcion}', '{series.fecha_estreno}', {series.estrellas}, '{series.genero}', {series.precio_alquiler}, {series.atp}, '{series.estado}')
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexión al registro'
        mensaje = 'La tabla series no está creada en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    # conexion = ConexionDB()

    # sql = f"""INSERT INTO series (titulo, descripcion, fecha_estreno, estrellas, genero, precio_alquiler, atp, estado)
    #     VALUES('{series.titulo}', '{series.descripcion}', '{series.fecha_estreno}', {series.estrellas}, '{series.genero}', {series.precio_alquiler}, {series.atp}, '{series.estado}')
    #     """
    # try:
    #         conexion.cursor.execute(sql)
    #         conexion.cerrar()
    # except:
    #         titulo = 'Conexion al registro'
    #         mensaje = 'La tabla series no esta creada en la base de datos'
    #         messagebox.showwarning(titulo, mensaje)


def listar():
    conexion = ConexionDB()

    lista_series = []
    sql = 'SELECT * FROM series'

    try:
        conexion.cursor.execute(sql)
        lista_series = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Creada la base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_series 

def editar(serie, id_series):
    conexion = ConexionDB()
    sql = f"""UPDATE series
    SET titulo = '{serie.titulo}', descripcion = '{serie.descripcion}', fecha_estreno = '{serie.fecha_estreno}',
    estrellas = '{serie.estrellas}', genero = '{serie.genero}', precio_alquiler = '{serie.precio_alquiler}',
    atp = '{serie.atp}', estado = '{serie.estado}'
    WHERE id_series = {id_series}
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'edicion de datos'
        mensaje = 'No se pudo editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_serie):
    conexion = ConexionDB()
    sql = f'DELETE FROM series WHERE id_serie= {id_serie}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'eliminar datos'
        mensaje = 'No se pudo aliminar el registro'
        messagebox.showerror(titulo, mensaje)