# Python module to import

# Auth: Ester Pancorbo
# Version: 0.0.1
# data: 02/03/2022
# dupdateAT: --/--/----

# include "Ejercicios1_5"

def ej1():
    op1 = 15.32
    op2 = 3

    print("suma: ", op1 + op2)
    print("resta: ", op1 - op2)
    print("multiplicación: ", op1 * op2)
    print("división: ", op1 / op2)
    print("módulo: ", op1 % op2)


def ej2():
    n = 5
    a = 9.43
    c = "45"
    print("n= %i, a= %f, c= %s" % (n, a, c))
    print("n+a = %f" % (n + a))
    print("a-n = %f" % (a - n))
    print("c = %i" % (int(c)))


def ej3():
    x = 2
    y = 9
    n = 10.5
    m = 2.75
    print("x= %i, y= %i, n= %f, m= %f" % (x, y, n, m))
    print("x + y = %i" % (x + y))
    print("x - y = %i" % (x - y))
    print("x * y = %i" % (x * y))
    print("x / y = %f" % (x / y))
    print('x mod y = %f' % (x % y))
    print("n + m = %f" % (n + m))
    print("n - m = %f" % (n - m))
    print("n * m = %f" % (n * m))
    print("n / m = %f" % (n / m))
    print("n mod m = %f" % (n % m))
    print("x*2 = %f" % (x * 2))
    print("y*2 = %f" % (y * 2))
    print("n*2 = %f" % (n * 2))
    print("m*2 = %f" % (m * 2))
    print("x+y+n+m =%f" % (x+y+n+m))
    print("x*y*n*m =%f" % (x * y * n * m))

def ej4():
    n=int(input("Introduzca un valor entero: "))
    result = n
    result += 77
    print("Incrementar N %i en 77 = %i" % (n, result))
    result -=3
    print("Decrementar N %i en 3 = %i" % (n, result))
    result = result * 2
    print("Duplicar N %i = %i" % (n, result ))



def ej5():
    a = 1
    b = 2
    c = 6
    d = 9

    x=b

    b = c
    c = a
    a = d
    d = x
    print ("a = %i, b = %i, c = %i, d = %i" % (a, b, c, d))


if __name__ == '__main__':
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
    print("Fichero Ejercicios1_5 ejecutado")