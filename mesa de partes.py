#LISTAS
nombre_Apo=[]
DNI_Apo=[]
codigo_Apo=[]
direccion=[]
telefono=[]
nombre_Est=[]
DNI_Est=[]
codigo_Est=[]
edad=[]
grado=[]
tipo_tramite=[]
fecha=[]
formulario=[]
#FUNCIONES
def validar(dig_inicial , dig_final ,x,cadena):
    if x==1:
        while True:
            dato=input(cadena).strip()
            if dato=="":
                print("Dato no válido")
            elif dato.isdigit()==False:
                print("Dato no valido")
            elif (int(dato)<dig_inicial or int(dato)>dig_final):
                print("Dato no valido")
            else:
                return int(dato) 
    elif x==2:
        while True:
            dato=input(cadena).strip()
            if dato=="":
                print("Dato no válido")
            elif dato.isdigit()==False:
                print("Dato no valido")
            elif(len(dato)!=dig_final):
                print("Dato invalido, debe tener ",dig_final," dígitos")
            else:
                return dato
    elif x==3:
        while True:
            dato=input(cadena).strip()
            if dato=="":
                print("Dato no válido")
            else:
                return dato
def asignar_codigo(i,contador): #===
    if i==1:
        return f"APOD-{contador:03d}"
    elif i==2:
        return f"ALUM-{contador:03d}"
    else :
        return f"Form-{contador:03d}"
def subir_archivo(codigo,nom,dni,Tel_ed,Dir_grad,cadena): 
    with open (f"{cadena}",'a',encoding="utf-8") as archivo:
        archivo.write(f"{codigo} | {nom} | {dni} | {Tel_ed} | {Dir_grad}\n")
def mostrar_tramite(nomA,dniA,telefo,direcc,codiA,nomE,dniE,codiE,edad,grado,tTrami,fecha,formulario):
    t=f"Tramite de {tTrami} - {formulario}"
    lineas=[f"Apoderado: {nomA}",f"DNI: {dniA}",f"Codigo: {codiA}",f"Telefono: {telefo}",f"Direccion: {direcc}",
            f"Estudiante: {nomE}",f"DNI: {dniE}",f"Codigo: {codiE}",f"Edad: {edad}",f"Grado: {grado}"]
    ancho=len(t)
    if len(fecha)>ancho:
        ancho=len(fecha)
    for l in lineas:
        if len(l)>ancho:
            ancho=len(l)
    espa1=(ancho-len(t))//2
    espa2=(ancho-len(fecha))//2
    print("*"*(ancho+4))
    print("* " + " " * espa1 + t + " " * (ancho-len(t)-espa1) + " *")
    print("* " + " " * espa2 + fecha + " " * (ancho-len(fecha)-espa2) + " *")
    print("*"*(ancho+4))
    for l in lineas:
        print("* " + l + " " * (ancho-len(l)) + " *")
    print("*"*(ancho+4))
def repeticion_caracteres(archivo, palabra, columna):
    pass
#FUNCIONES PRINCIPALES
def registro(contador):#///
    print("REGISTRO DE TRAMITE")
    tipo = validar(1, 2, 1, "Ingrese el tramite [1:Inscripcion - 2:Traslado]: ")
    if tipo == 1:
        tipo_tramite.append("Inscripcion")
    else:
        tipo_tramite.append("Traslado")
    fecha.append(validar(0, 0, 3, "Ingrese la fecha (dd/mm/aaaa): "))#///

    # apoderado /// ===
    print("REGISTRAR APODERADO")
    dni_apo = validar(0, 8, 2, "Ingrese su DNI: ")
    existe = False
    for i in range(len(DNI_Apo)):
        if DNI_Apo[i] == dni_apo:
            existe = True
            nom_apo = nombre_Apo[i]
            tel_apo = telefono[i]
            dir_apo = direccion[i]
            cod_apo = codigo_Apo[i]
            break
    if existe:
        print(f"Apoderado ya registrado: {nom_apo} ({cod_apo})")
        DNI_Apo.append(dni_apo)
        nombre_Apo.append(nom_apo)
        telefono.append(tel_apo)
        direccion.append(dir_apo)
        codigo_Apo.append(cod_apo)
    else:
        n_apo = len(set(codigo_Apo)) + 1          # apoderados distintos + 1
        DNI_Apo.append(dni_apo)
        nombre_Apo.append(validar(0, 0, 3, "Ingrese su nombre: "))
        telefono.append(validar(0, 9, 2, "Ingrese su numero de telefono: "))
        direccion.append(validar(0, 0, 3, "Ingrese su distrito: "))
        codigo_Apo.append(asignar_codigo(1, n_apo)) # ===
        print("Codigo asignado al apoderado: ", codigo_Apo[-1])
        subir_archivo(codigo_Apo[-1], nombre_Apo[-1], DNI_Apo[-1],
                      telefono[-1], direccion[-1], "APODERADOS.txt")
def busqueda_tramite(contador):
    encontrado=False
    if(contador==0): print("no hay datos guardados\n")
    else:
        busqueda=validar(1,2,1,"Buscar por 1) DNI O 2) TRAMITE eliga una opcion:")
        if busqueda==1:
            dni = validar(0, 8, 2, "Ingrese el DNI del estudiante: ")
            for i in range (contador):
                if DNI_Est[i] == dni:
                    encontrado=True
                    mostrar_tramite(nombre_Apo[i],DNI_Apo[i],telefono[i],direccion[i],codigo_Apo[i],nombre_Est[i],DNI_Est[i],codigo_Est[i],edad[i],grado[i],tipo_tramite[i],fecha[i],formulario[i])
        else:
            cod = input("Ingrese el codigo del tramite (ej. Form-001): ").strip().upper()
            for i in range (contador):
                if formulario[i].upper() == cod:
                    encontrado = True
                    mostrar_tramite(nombre_Apo[i], DNI_Apo[i], telefono[i], direccion[i], codigo_Apo[i],nombre_Est[i], DNI_Est[i], codigo_Est[i], edad[i], grado[i], tipo_tramite[i], fecha[i],formulario[i])
        if(encontrado==False): print("No se encontro tramite")
def ordenar_tramites(contador):
    return
def mostrar_formularios(contador):
    return
def menu():#***
    print("===MENU=== \n1)Registrar tramite\n2)Buscar el tramite\n3)Ordenar tramite\n4)Mostrar tramite\n5)Salir")
    op=validar(1,5,1,"Escoja una opcion: ")
    return op

a1 = True#***
contador = 0
while a1 and contador < 100:
    match menu():
        case 1:
            contador = registro(contador)     
        case 2:
            busqueda_tramite(contador)
        case 3:
            ordenar_tramites(contador)
        case 4:
            mostrar_formularios(contador)
        case 5:
            a1 = False
            print("Fin del servicio\n")
if contador == 100:
    print("La capacidad es 100 formularios")    
