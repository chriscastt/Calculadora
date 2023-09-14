def SUM(n1, n2):
    R = n1 + n2
    return R

def RES(n1, n2):
    R = n1 - n2
    return R

def MULT(n1, n2):
    R = n1 * n2
    return R
def DIV( n1, n2):
    R = n1 / n2
    return R
R = 0
ELEC = 1
while ELEC != 2:
    print("Qué operación deseas realizar: \n 1.SUMA \n 2.RESTA \n 3.MULTIPLIACION \n 4.DIVISION \n")
    ELEC = int(input("Elección: "))

    try:
        
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        if ELEC == 1:
            R = SUM(n1,n2)
            print("El resulado de la suma es: ", R)
        if ELEC == 2:
            R = RES(n1,n2)
            print("El resulado de la resta es: ", R)
        if ELEC == 3:
            R = MULT(n1,n2)
            print("El resulado de la division es: ", R)
        if ELEC == 4:
            R = DIV(n1,n2)
            print("El resulado de la multipliacion es: ", R)
    finally:
        print("\n")
        ELEC = int(input("¿Quieres realizar otra operación?, presiona cualquier numero para si y 2 para no: "))
print("\n Adios")