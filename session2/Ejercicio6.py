# Auth: Ester Pancorbo
# Version: 0.0.1
# data: 02/03/2022
# dupdateAT: --/--/----

import math
from tkinter import messagebox

def ej6():
    op1 = 18
    op2 = 25

    if op1 > op2:
        print(str(op1) + " es mayor que " + str(op2))
    else:
        print(str(op2) + " es mayor que " + str(op1))

def ej7():
    minombre = "Esther"
    print("Te damos la bienvenida " + str(minombre))

def ej8():
    minombre = str(input("Introduzca su nombre: "))
    print("Te damos la bienvenida " + str(minombre))

def ej9():
    print("Se va a calcular el área de un círculo dado su radio.")
    radio = float(input("Por favor, introduzca el valor del radio: "))
    qpi = math.pi
    area = qpi*(math.pow(radio,2))
    print("El área es: " + str(area))

def ej10():
    print("Se va a indicar si el número introducido por teclado es divisible entre 2 o no")
    qnumero = float(input("Introduzca un número: "))
    if (qnumero % 2) == 0:
        print("El número " + str(qnumero) + " es divisible entre 2")
    else:
        print("El número " + str(qnumero) + " no es divisible entre 2")

def ej11():
    print("Se va a indicar el precio final con IVA(21%)")
    qprecio = float(input("Introduzca el precio:"))
    qpreciototal = qprecio + float(qprecio * 0.21)
    print("El precio final es: " + str(qpreciototal))

def ej12():
    i=1
    while i<=100:
        print(i)
        i += 1

def ej13():
    for i in range(101):
        print(i)

def ej14():
    i=1
    while i<=100:
        # if ((i % 2) == 0) & ((i % 3) == 0):
        if ((i % 6) == 0):
            print(i)
        i += 1

def ej15():
    nventas = (int(input("Introduzca el número total de ventas: ")))
    sumventas = 0
    for i in range(nventas):
        qventa = float(input("Venta " + str(i+1) + ": "))
        sumventas = float(sumventas) + float(qventa)
    print("El importe total de las " + str(nventas) + " ventas es: " + str(sumventas))


def ej16():
    qTipoDia = "no válido"
    qdia = str(input("Introduzca un día de la semana: "))

    if (qdia.upper() == "LUNES"):
        qTipoDia = "laboral"
    if (qdia.upper() == "MARTES"):
        qTipoDia = "laboral"
    if (qdia.upper() == "MIERCOLES") | (qdia.upper() == "MIÉRCOLES"):
        qTipoDia = "laboral"
    if qdia.upper() == "JUEVES":
        qTipoDia = "laboral"
    if qdia.upper() == "VIERNES":
        qTipoDia = "laboral"
    if (qdia.upper() == "SABADO") | (qdia.upper() == "SÁBADO"):
        qTipoDia = "no laboral"
    if qdia.upper() == "DOMINGO":
        qTipoDia = "no laboral"

    print("El día " + str(qdia) + " es " + qTipoDia)


def ej17():
    mipwd = "Pitufo"
    iTope = 3
    i = 0
    qpwd = ""

    while qpwd != mipwd:
        if i < iTope:
            i += 1
            qpwd = str(input("Introduzca contraseña: "))
        else:
            print("Contraseña incorrecta. Ha consumido los 3 intentos.")
            break
    if qpwd == mipwd:
        print("Enhorabuena")

def ej18():
#     CalculadoraInversa

    qsigno = ""

    op1 = int(input("Introduzca el primer operando: "))
    op2 = int(input("Introduzca el segundo operando: "))
    qsigno = str(input("Introduzca un signo aritmético: "))

    qresultado = 0

    if str(qsigno) == "+":
        qresultado = op1 + op2
    if qsigno == "-":
        qresultado = op1 - op2
    if qsigno == "*":
        qresultado = op1 * op2
    if qsigno == "/":
        qresultado = op1 / op2
    if qsigno == "^":
        qresultado = math.pow(op1, op2)
    if qsigno == "%":
        qresultado = op1 % op2

    print("El resultado es: " + str(qresultado))
    messagebox.showinfo(message="El resultado es: " + str(qresultado), title = "CalculadoraInversa")

if __name__ == '__main__':
    # ej6()
    # ej7()
    # ej8()
    # ej9()
    # ej10()
    # ej11()
    # ej12()
    # ej13()
    # ej14()
    # ej15()
    # ej16()
    # ej17()
    ej18()