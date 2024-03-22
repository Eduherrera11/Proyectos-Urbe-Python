estudiantes = []
opcion = ""

while opcion != "5":
    opcion = input(str("""Selecciona una opcion a realizar:
                          1. Ver listado de estudiantes
                          2. Registrar estudiantes
                          3. Actualizar estudiantes
                          4. Eliminar estudiantes
                          5. Salir
                          """))
    if opcion == "1":
        print(estudiantes)
    elif opcion == "2":
        estudiante = {}
        nombre = input("Ingrese el nombre del estudiante que desea agregar: ")
        while not nombre.isalpha() or nombre.strip() == "":
            nombre = input("Nombre inválido. Ingrese un nombre correcto (sin números o vacío): ")
        estudiante["Name"] = nombre
        
        apellido = input("Ingrese el apellido del estudiante que desea agregar: ")
        while not apellido.isalpha() or apellido.strip() == "":
            apellido = input("Apellido inválido. Ingrese un apellido correcto (sin números o vacío): ")
        estudiante["Lastname"] = apellido
        
        cedula = input("Ingrese la cédula del estudiante que desea agregar: ")
        while not cedula.isdigit():
            cedula = input("Cédula inválida. Ingrese una cédula correcta (solo números): ")
        estudiante["ID"] = cedula
        
        nota1 = input("Ingrese la nota 1 del estudiante: ")
        while not nota1.isdigit():
            nota1 = input("Nota inválida. Ingrese la nota 1 del estudiante (solo números): ")
        estudiante["Grade 1"] = int(nota1)
        
        nota2 = input("Ingrese la nota 2 del estudiante: ")
        while not nota2.isdigit():
            nota2 = input("Nota inválida. Ingrese la nota 2 del estudiante (solo números): ")
        estudiante["Grade 2"] = int(nota2)
        
        nota3 = input("Ingrese la nota 3 del estudiante: ")
        while not nota3.isdigit():
            nota3 = input("Nota inválida. Ingrese la nota 3 del estudiante (solo números): ")
        estudiante["Grade 3"] = int(nota3)
        estudiante["Average Grade"] = (estudiante["Grade 1"] + estudiante["Grade 2"] + estudiante["Grade 3"]) / 3
        estudiantes.append(estudiante)
    elif opcion == "3":
        cedula = input("Ingrese la cédula del estudiante que desea actualizar: ")
        estudiante_encontrado = False
        for estudiante in estudiantes:
            if estudiante["ID"] == cedula:
                estudiante_encontrado = True
                opcion_actualizar = ""
                while opcion_actualizar != "7":
                    opcion_actualizar = input("""Selecciona qué dato quieres actualizar:
                                                1. Nombre del estudiante
                                                2. Apellido del estudiante
                                                3. Cédula del estudiante
                                                4. Nota 1 del estudiante
                                                5. Nota 2 del estudiante
                                                6. Nota 3 del estudiante
                                                7. Salir
                                                """)
                    if opcion_actualizar == "1":
                        nombre = input("Ingrese el nuevo nombre del estudiante: ")
                        while not nombre.isalpha() or nombre.strip() == "":
                            nombre = input("Nombre inválido. Ingrese un nombre correcto (sin números o vacío): ")
                        estudiante["Name"] = nombre
                    elif opcion_actualizar == "2":
                        apellido = input("Ingrese el nuevo apellido del estudiante: ")
                        while not apellido.isalpha() or apellido.strip() == "":
                            apellido = input("Apellido inválido. Ingrese un apellido correcto (sin números o vacío): ")
                        estudiante["Lastname"] = apellido
                    elif opcion_actualizar == "3":
                        cedula = input("Ingrese la nueva cédula del estudiante: ")
                        while not cedula.isdigit():
                            cedula = input("Cédula inválida. Ingrese una cédula correcta (solo números): ")
                        estudiante["ID"] = cedula
                    elif opcion_actualizar == "4":
                        estudiante["Grade 1"] = int(input("Ingrese la nota 1 del estudiante: "))
                    elif opcion_actualizar == "5":
                        estudiante["Grade 2"] = int(input("Ingrese la nota 2 del estudiante: "))
                    elif opcion_actualizar == "6":
                        estudiante["Grade 3"] = int(input("Ingrese la nota 3 del estudiante: "))
                    elif opcion_actualizar == "7":
                        print("El estudiante se ha actualizado satisfactoriamente!")
                    else:
                        print("Ingresaste un valor invalido")
                    estudiante["Average Grade"] = (estudiante["Grade 1"] + estudiante["Grade 2"] + estudiante["Grade 3"]) / 3

            else:
                print("La cedula que ingresaste no se encuentra en la lista")
            
    elif opcion == "4":
        valor = input(str("Ingrese la cedula del estudiante que desea eliminar: "))
        for estudiante in estudiantes:
            if estudiante["ID"] == valor:
                estudiantes.remove(estudiante)
            else:
                print("La cedula que ingresaste no se encuentra en la lista")
    elif opcion == "5":
        print("El programa ha finalizado satisfactoriamente!!")

    else :
        print("Ingresaste un valor invalido vuelve a intentar")



