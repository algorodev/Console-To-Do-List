import usuarios.usuarios as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Rellena los siguientes datos ...")

        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuarios(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Bienvenido {registro[1].nombre} {registro[1].apellidos} !!")
        else:
            print("El registro ha fallado ...")

    def login(self):
        print("Introduce tus credenciales ...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuarios('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido de nuevo {login[1]} !!")
                self.proximasAcciones(login)
        except Exception:
            print("Las credenciales no són correctas ...")
            self.login()

    def proximasAcciones(self, usuario):
        print("\n**************************")
        print("""   Acciones disponibles
    -   Crear notas --> Crear
    -   Mostrar notas --> Mostrar
    -   Eliminar nota --> Eliminar
    -   Salir --> Salir
        """)

        acciones = notas.acciones.Acciones()

        accion = input("¿Qué quieres hacer?: ")

        if accion == "Crear" or accion == "crear":
            acciones.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Mostrar" or accion == "mostrar":
            acciones.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Eliminar" or accion == "eliminar":
            acciones.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "Salir" or accion == "salir":
            print("Adiós !! Nos vemos pronto !!")
            exit()

        else:
            print("Lo siento, introduce una opción válida ...")
