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

from usuarios import acciones

print("******* BIENVENIDO *******")
print("""   Acciones disponibles
    -   Registro
    -   Login
""")

acciones = acciones.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "Registro" or accion == "registro":
    acciones.registro()

elif accion == "Login" or accion == "login":
    acciones.login()

else:
    print("Lo siento, introduce una opción válida ...")
