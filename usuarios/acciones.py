import usuarios.usuarios as modelo

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
        except Exception as e:
            print("Las credenciales no són correctas ...")

