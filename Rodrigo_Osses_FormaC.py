registro={}
entradas_disponibles_LF=500
entradas_disponibles_LI=500
def comprar_entradas_para_LF():
    ingresar_nombre_comprador()
    tipo_entrada_func()
    codigo_Seguridad()
    entradas_disponibles_LF=entradas_disponibles_LF-1
    print("Felicidades, tu entrada ha sido comprada exitosamente")
def comprar_entradas_para_LI():
    ingresar_nombre_comprador()
    tipo_entrada_func()
    codigo_Seguridad()
    entradas_disponibles_LI=entradas_disponibles_LI-1
    print("Felicidades, tu entrada ha sido comprada exitosamente")
    
def consulta_entradas():
    print("Entradas disponibles para Los Fortificados: ", entradas_disponibles_LF)
    print("Entradas disponibles para Los Iluminados: ", entradas_disponibles_LI)
def ingresar_nombre_comprador():
    while True:
        nombre_comprador=input("Ingresa el nombre del comprador: ")
        if len(nombre_comprador)<1:
            print("error, no puedes dejar este campo vacío")
        else:
            break
def tipo_entrada_func():
    while True:
        tipo_entrada=input("Ingrese el tipo de entrada que desea comprar, para vip ingrese (V), para general ingrese (G): ")
        if len(tipo_entrada)<1:
            print("error, no puedes dejar este campo vacío")
            if tipo_entrada.lower !="v" or tipo_entrada.lower !="g":
                print("Debes ingresar V(Vip) o G(General)")
                continue
        else:
            break
def codigo_Seguridad():
    while True:
        codigo_confirmacion=input("Ingrese un código de confirmación (debe requerir los siguientes parámetros por su seguridad: Largo mínimo de 6 caracteres, mínimo 1 letra mayúscula, mínimo 1 número y no pueden haber espacios en blanco.)")
        if len(codigo_confirmacion)<6:
            print("Error, no puedes ingresar un código con menos de 6 caracteres")
            continue
        else:
            break
while True:
    print("**Bienvenido al Tótem de autoservicio**")
    print("[1]Comprar entradas para Los fortificados")
    print("[2]Comprar entradas para Los iluminados")
    print("[3]Consultar stock de entradas")
    print("[4]Salir")
    opcion=int(input("Ingrese la opción númerica para la acción que desea realizar: "))
    while opcion==1:
        comprar_entradas_para_LF()
        break
    while opcion==2:
        comprar_entradas_para_LI()
        break
    while opcion==3:
        consulta_entradas()
        break
    else:
        break

