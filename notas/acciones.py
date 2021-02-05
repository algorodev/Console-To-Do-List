import notas.notas as modelo

class Acciones:

    def crear(self, usuario):
        print("Rellena los siguientes datos ...")

        titulo = input("Introduce el título de la nota: ")
        descripcion = input("Introduce la descripción de la nota: ")

        nota = modelo.Notas(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("Nota guardada !!")
        else:
            print("No se ha podido insertar la nota")
