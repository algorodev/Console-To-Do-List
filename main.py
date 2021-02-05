"""
    Proyecto Python y MySQL
    -   Abrir asistente
    -   Login o Registro
    -   Registro: Crear usuarios en la bbdd
    -   Login: Identificar usuario
    -   Crear Notas
    -   Mostrar Notas
    -   Eliminar Notas
"""

print("******* BIENVENIDO *******")
print("""   Acciones disponibles
    -   Registro
    -   Login
""")

accion = input("¿Qué quieres hacer?: ")

if accion == "Registro" or accion == "registro":
    print("Rellena los siguientes datos ...")

    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")

elif accion == "Login" or accion == "login":
    print("Introduce tus credenciales ...")

    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")

else:
    print("Lo siento, introduce una opción válida ...")
