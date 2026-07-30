def mostrar_tareas(lista):
    print("\n=== Tus tareas ===")
    if len(lista) == 0:
        print("No tienes tareas pendientes")
    else:
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea}")

tareas = []

while True:
    print("\n1) Agregar tarea")
    print("2) Ver tareas")
    print("3) Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nueva = input("Escribe la tarea: ")
        tareas.append(nueva)
        print(f"'{nueva}' agregada")
    elif opcion == "2":
        mostrar_tareas(tareas)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")

