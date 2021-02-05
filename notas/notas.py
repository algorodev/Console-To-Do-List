import usuarios.conexion as conexion
import datetime

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Notas:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        fecha = datetime.datetime.now()

        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, %s)"
        nota = (self.usuario_id, self.titulo, self.descripcion, fecha)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]
