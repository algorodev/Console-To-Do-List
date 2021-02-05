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
elif accion == "Login" or accion == "login":
    print("Introduce tus credenciales ...")
else:
    print("Lo siento, introduce una opción válida ...")
