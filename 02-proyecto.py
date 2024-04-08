from datetime import datetime

def añadir_tareas(lista):
    
    while True:
        try:
            codigo = int(input("Escriba el código de la tarea en formato int: "))

            codigo_existente = False
            for tarea in lista:
                if tarea["Codigo"] == codigo:
                    codigo_existente = True
                    print("El código ya existe, por favor ingresa uno que no exista.")
                    break  
            
            if not codigo_existente:
                
                break

        except ValueError:
            print("Por favor, ingresa solo números enteros.")



    while True:
            titulo = str(input("Escribe el titulo de la tarea: ")).strip()
            if len(titulo) <= 20 and titulo:
                break
            else: 
                print("El titulo de tu tarea debe tener una longitud maxima de 20 caracteres, no ingreses valores vacios.")

    while True:
         descripcion = str(input("Ingresa la descripcion de la tarea: "))
         if descripcion:
              break
         else:
              print("La descripcion no puede estar vacia.")

    while True:
         status = str(input("Ingresa el status de la tarea (Completado o Pendiente): "))
         status = status.title()
         if status in ["Completado", "Pendiente"]:
              break
         else:
              print("Solo puedes ingresar la opcion Completado o Pendiente.")

    while True:
        fecha_entrada = input("Ingresa la fecha en formato DD-MM-YYYY: ")
        try:
            fecha_entrada = datetime.strptime(fecha_entrada, "%d-%m-%Y")
            break  
        except ValueError:
            print("Formato de fecha inválido. Por favor, ingresa la fecha en formato DD-MM-YYYY.")       

    tarea = {"Codigo": codigo, "Titulo": titulo, "Descripcion": descripcion, "Status": status, "Fecha": fecha_entrada}   

    lista.append(tarea)

def mostrar_tareas(lista, status=None, filtro=None, valor=None):
    print("Codigo |  Titulo  |    Descripcion    |  Status  |  Fecha ")

    if filtro == "Fecha":
        for tarea in lista:
            if tarea["Fecha"].date() == valor.date():
                fecha_str = tarea["Fecha"].strftime("%d-%m-%Y")
                print(f'   {tarea["Codigo"]} | {tarea["Titulo"]} | {tarea["Descripcion"]} | {tarea["Status"]} | {fecha_str}')
                print()

    elif filtro:
        for tarea in lista:
            if filtro in ["Codigo", "Titulo", "Descripcion", "Status"]:
                if str(tarea[filtro]).lower().startswith(str(valor).lower()):
                    fecha_str = tarea["Fecha"].strftime("%d-%m-%Y") if isinstance(tarea["Fecha"], datetime) else tarea["Fecha"]
                    print(f'   {tarea["Codigo"]} | {tarea["Titulo"]} | {tarea["Descripcion"]} | {tarea["Status"]} | {fecha_str}')
                    print()

    elif status:
        resultado = list(filter(lambda tarea: tarea["Status"] == status, lista))
        for tarea in resultado:
            fecha_str = tarea["Fecha"].strftime("%d-%m-%Y") if isinstance(tarea["Fecha"], datetime) else tarea["Fecha"]
            print(f'   {tarea["Codigo"]} | {tarea["Titulo"]} | {tarea["Descripcion"]} | {tarea["Status"]} | {fecha_str}')
            print()


def actualizar_tarea(lista, codigo):
     for tarea in lista:
          if tarea["Codigo"] == codigo:
            while True:
                opcion = str(input("""Selecciona la variable que deseas actualizar de la tarea: 
                                1. Codigo
                                2. Titulo
                                3. Descripcion
                                4. Status
                                5. Fecha
                                """))
                
                if opcion.title() in ["Codigo", "1"]:
                    while True:
                        try:
                            tarea["Codigo"] = int(input("Escriba el nuevo valor del codigo de la tarea en formato int: "))
                            break
                        except ValueError:
                            print("Por favor, ingresa solo numeros enteros.")
                    break

                elif opcion.title() in ["Titulo", "2"]:
                    while True:
                        tarea["Titulo"] = str(input("Escribe el nuevo valor del titulo de la tarea: ")).strip()
                        if len(tarea["Titulo"]) <= 20 and tarea["Titulo"]:
                            break
                        else: 
                            print("El titulo de tu tarea debe tener una longitud maxima de 20 caracteres, no ingreses valores vacios..")
                    break        

                elif opcion.title() in ["Descripcion", "3"]:
                    while True:
                        tarea["Descripcion"] = str(input("Ingresa la nueva descripcion de la tarea: "))
                        if tarea["Descripcion"]:
                            break
                        else:
                            print("La descripcion no puede estar vacia.")
                    break        

                elif opcion.title() in ["Status", "4"]:
                    while True:
                        tarea["Status"] = str(input("Ingresa la actualizacion del  status de la tarea (Completado o Pendiente): ")).title()
                        if tarea["Status"] in ["Completado", "Pendiente"]:
                            break
                        else:
                            print("Solo puedes ingresar la opcion Completado o Pendiente.")
                    break         

                elif opcion.title() in ["Fecha", "5"]:
                    while True:
                        fecha_entrada = input("Ingresa la actualización de la fecha en formato DD-MM-YYYY: ")
                        try:
                            fecha_convertida = datetime.strptime(fecha_entrada, "%d-%m-%Y")
                            tarea["Fecha"] = fecha_convertida
                            break  
                        except ValueError:
                            print("Formato de fecha inválido. Por favor, ingresa la fecha en formato DD-MM-YYYY.") 
                    break


                else:
                    print("Escribe el nombre de la variable que deseas actualizar o su numero.")

def eliminar_tarea(lista, codigo):
    for tarea in lista:
        if tarea["Codigo"] == codigo:
            print(tarea)
            while True:
                opcion = str(input("Estas seguro que quieres eliminar esa tarea? "))
                if opcion.title() == "Si":
                    lista.remove(tarea)
                    print("Se elimino la tarea que seleccionaste.")
                    break
                elif opcion.title() == "No":
                    print("No se ha eliminado ninguna tarea.")
                    break
                else:
                    print("Solo puedes ingresar las opciones 'Si' o 'No")

def menu(lista):
    while True:
        opciones = str(input("""Escoge la opcion que deseas realizar: 
                             1. Lista de tareas
                             2. Filtrar tareas
                             3. Añadir tareas
                             4. Actualizar tareas
                             5. Eliminar tareas
                             6. Salir
                             """))
        
        if opciones.title() in ["Lista de tareas", "1"]:
            while True:
                opcion_lista = str(input("""
                                         1. Completadas
                                         2. Pendientes
                                         3. Atras
                                         """))
                if opcion_lista.title() in ["Completadas", "1"]:
                    status = "Completado"
                    mostrar_tareas(lista, status=status)
                
                elif opcion_lista.title() in ["Pendientes", "2"]:
                    status = "Pendiente"
                    mostrar_tareas(lista, status=status)

                elif opcion_lista.title() in ["Atras", "3"]:
                    break

                else:
                    print("Has seleccionado una opcion invalida!")



        elif opciones.title() in ["Filtrar", "Filtrar tareas", "2"]:
            opcion_filtrar = str(input("""Filtrar por:
                                       1. Codigo
                                       2. Titulo
                                       3. Fecha
                                       """))
            
            if opcion_filtrar.title() in ["Codigo", "1"]:
                while True:
                    try:
                        codigo = int(input("Ingresa el codigo de la tarea que deseas filtrar: "))
                        resultado = list(filter(lambda tarea: True if tarea["Codigo"] == codigo else False, lista))
                        if resultado:
                            mostrar_tareas(lista, filtro="Codigo", valor=codigo)
                        else:
                            print("La tarea con el código indicado no existe. Intenta de nuevo.")
                        break
                    except ValueError:
                        print("Por favor, ingresa solo numeros enteros.")

            elif opcion_filtrar.title() in ["Titulo", "2"]:
                titulo = input("Escribe el título de la tarea que deseas filtrar: ")
                if len(titulo) > 20:
                    print("El título de tu tarea debe tener una longitud máxima de 20 caracteres.")
                else:
                    resultado = list(filter(lambda tarea: tarea["Titulo"].lower().startswith(titulo.lower()), lista))
                if resultado:
                    mostrar_tareas(resultado, filtro="Titulo", valor=titulo)
                else:
                    print("La tarea con el título indicado no existe. Intenta de nuevo.")

            elif opcion_filtrar.title() in ["Fecha", "3"]:
                while True:
                    fecha_entrada = input("Ingresa la fecha en formato DD-MM-YYYY: ")
                    try:
                        fecha = datetime.strptime(fecha_entrada, "%d-%m-%Y")
                        resultado = list(filter(lambda tarea: tarea["Fecha"] == fecha, lista))
                        if resultado:
                            mostrar_tareas(lista, filtro="Fecha", valor=fecha)
                        else:
                            print("La tarea con la fecha indicada no existe. Intenta de nuevo.")
                        break
                    except ValueError:
                        print("Formato de fecha inválido. Por favor, ingresa la fecha en formato DD-MM-YYYY.")  



        elif opciones.title() in ["Añadir", "Añadir tarea", "3"]:
            añadir_tareas(lista)
            print("La tarea se ha añadido con exito.")



        elif opciones.title() in ["Actualizar", "Actualizar tareas", "4"]:
            while True:
                try:
                    codigo = int(input("Escriba el codigo de la tarea que desea actualizar: "))
                    resultado = list(filter(lambda tarea: True if tarea["Codigo"] == codigo else False, lista))
                    if resultado:
                        actualizar_tarea(lista, codigo)
                        print("La actualizacion ha sido completada.")
                        break
                    else:
                        print('El codigo ingresado no existe en la lista de tareas.')
                except ValueError:
                    print("Por favor, ingresa solo numeros enteros.")



        elif opciones.title() in ["Eliminar", "Eliminar tareas", "5"]:
            while True:
                try:
                    codigo = int(input("Escriba el codigo de la tarea que desea eliminar: "))
                    break
                except ValueError:
                    print("Por favor, ingresa solo numeros enteros.")
            eliminar_tarea(lista, codigo)



        elif opciones.title() in ["Salir", "6"]:
            break

        else:
            print("Elige una opcion valida, escribiendola como se lee en pantalla o poniendo su numero.")


#    lista = [{"Codigo": 1, "Titulo": "Comprar mercancia", "Descrpcion": "Hacer un pedido de repuestos toyota a el proveedor", "Status": "Pendiente", "Fecha": "28-04-2024"},
#            {"Codigo": 2, "Titulo": "Comprar cryptos", "Descrpcion": "Invertir en crypto monedas a largo plazo", "Status": "Completado", "Fecha": "02-04-2024"},
#            {"Codigo": 1, "Titulo": "Leer", "Descrpcion": "Leer 20 paginas de un libro de finanzas", "Status": "Completada", "Fecha": "03-04-2024"}]

lista = []

menu(lista)
                
                    
                
                
               
                    

                    
            
