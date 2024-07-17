import random
import statistics
import csv


Workers = ["Juan Pérez" , "María García" , "Carlos López" , "Ana Martínez" , "Pedro Rodríguez" , "Laura Hernández" , "Miguel Sánchez" , "Isabel Gómez" , "Francisco Díaz" , "Elena Fernández"]

def generar():
    Salarys = {}
    for Worker in Workers:
        Salary = random.randint(300000, 2500000) 
        Salarys[Worker] = Salary
    return Salarys

def clasificar(Workers_Salarys):
    menores_800000 = []
    entre_800000_2000000 = []
    mayores_2000000 = []
    for Worker, Salary in Workers_Salarys.items():
        if Salary < 800000:
            menores_800000.append((Worker, Salary))
        elif 800000 <= Salary <= 2000000:
            entre_800000_2000000.append((Worker, Salary))
        elif Salary > 2000000:
            mayores_2000000.append((Worker, Salary))
    
    menuClasificar = """
        1.- Mostrar Sueldos
        2.- Salir
        """
    while True:
        print(menuClasificar)
        op1 = int(input('Ingrese opción: '))
        while op1 < 1 or op1 > 2:
            op1 = int(input('Ingrese opción 1 o 2: '))
        if op1 == 1:
            print("Sueldos menores a 800000: ")
            for Worker, Salary in menores_800000:
                print(f"{Worker}: {Salary}")
            
            print("\nSueldos entre 800000 y 2000000: ")
            for Worker, Salary in entre_800000_2000000:
                print(f"{Worker}: {Salary}")
            
            print("\nSueldos mayores a 2000000: ")
            for Worker, Salary in mayores_2000000:
                print(f"{Worker}: {Salary}")
            
        if op1 == 2:
            break


def max_sueldo(dicc_Salarys):
    Most_Worker_Salary = max(dicc_Salarys, key=dicc_Salarys.get)
    return Most_Worker_Salary, dicc_Salarys[Most_Worker_Salary]

def min_sueldo(dicc_Salarys):
    Least_Worker_Salary = min(dicc_Salarys, key=dicc_Salarys.get)
    return Least_Worker_Salary, dicc_Salarys[Least_Worker_Salary]

def promedio_sueldo(dicc_Salarys):
    total_Salarys = sum(dicc_Salarys.values()) 
    Cant_Workers = len(dicc_Salarys) 
    prom = total_Salarys / Cant_Workers 
    return prom

def media_sueldo(dicc_Salarys):
    Salarys = list(dicc_Salarys.values())
    if not Salarys:
        raise ValueError("El diccionario de sueldos está vacío")
    product = 1
    for Salary in Salarys:
        product *= Salary
    media_geometrica = round(product ** (1 / len(Salarys)))
    return media_geometrica

def estadistica(Workers_Salarys):
    menu = '''
    1. Sueldo máximo
    2. Sueldo mínimo
    3. Sueldo promedio
    4. Media geométrica
    5. Salir
    '''
    while True:
        print(menu)
        op2 = int(input('Ingrese opción: '))
        while op2 < 1 or op2 > 5:
            op2 = int(input('Ingrese opción del 1 al 5: '))
        if op2 == 1:
            Worker_max, Salary_max = max_sueldo(Workers_Salarys)
            print(f"El empleado con el mayor sueldo es {Worker_max} con un sueldo de {Salary_max}")
        if op2 == 2:
            Worker_min, Salary_min = min_sueldo(Workers_Salarys)
            print(f"El empleado con el menor sueldo es {Worker_min} con un sueldo de {Salary_min}")
        if op2 == 3:
            Salary_prom = promedio_sueldo(Workers_Salarys)
            print(f"El sueldo promedio es {Salary_prom:.2f}")
        if op2 == 4:
            try:
                media_geo = media_sueldo(Workers_Salarys)
                print(f"La media geométrica de los sueldos es: {media_geo}")
            except ValueError as e:
                print(f"Error: {e}")
        if op2 == 5:
            break

def reporteSueldo(Workers_Salarys):
    
    nom_archivo = "WorkersSalarys.csv"
    with open(nom_archivo, "w", newline="")as archivo:
        write_csv = csv.writer(archivo, delimiter="||")
        write_csv.writerow(["Trabajador", "Suleldo Bruto", "AFP", "Salud", "Sueldo Neto"])
    
    afp = {Worker: round(Salary * 0.12) for Worker, Salary in Workers_Salarys.items()}
    Healt = {Worker: round(Salary * 0.07) for Worker, Salary in Workers_Salarys.items()}
    
    saldoRestante = {Worker: Salary - afp[Worker] - Healt[Worker] for Worker, Salary in Workers_Salarys.items()}

    print("\nReporte de descuentos:")
    print("\nAFP:")
    for Worker, descount in afp.items():
        print(f"{Worker}: {descount}")
    
    print("\nSalud:")
    for Worker, descount in Healt.items():
        print(f"{Worker}: {descount}")

    print("\nSaldo restante:")
    for Worker, saldo in saldoRestante.items():
        print(f"{Worker}: {saldo}")

    
        
        
def menu():
    menu = '''
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas
    4. Reporte de sueldos
    5. Salir
    '''
    print(menu)

Workers_Salarys = {}

while True:    
    menu()
    op = int(input('Ingrese opción del 1 al 5: '))
    while op < 1 or op > 5:
        op = int(input('Debe ser entre 1 y 5\nIngrese opción: '))
    if op == 1:
        Workers_Salarys = generar()
        print("Sueldos Asignados")
    elif op == 2:
        if Workers_Salarys:
            clasificar(Workers_Salarys)
        else:
            print("Primero debes asignar los sueldos (opción 1).")
    elif op == 3:
        if Workers_Salarys:
            estadistica(Workers_Salarys)
        else:
            print("Primero debes asignar los sueldos (opción 1).")
    elif op == 4:
        if Workers_Salarys:
            reporteSueldo(Workers_Salarys)
        else:
            print("Primero debes asignar los sueldos (opción 1).")
    elif op == 5:
        print("Desarollado Por: \n  Matías Felipe Saldías Farías \n  21.828.963.0")
        break
