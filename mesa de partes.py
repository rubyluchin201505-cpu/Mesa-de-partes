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
    return
def repeticion_caracteres(archivo, palabra, columna):
    pass
#FUNCIONES PRINCIPALES
def registro(contador):
    return
def busqueda_tramite(contador):
    return
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
