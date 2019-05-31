print("MoveMind - MRUV Calculator Python")


#  __  __ __      __   _____        _               _         _
# |  \/  |\ \    / /  / ____|      | |             | |       | |
# | \  / | \ \  / /  | |      __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __
# | |\/| |  \ \/ /   | |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
# | |  | |   \  /    | |____| (_| || || (__ | |_| || || (_| || |_| (_) || |
# |_|  |_|    \/      \_____|\__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|
#

print("--------------------------------------------------------------")

print("_  _ _  _    ____ ____ _    ____ _  _ _    ____ ___ ____ ____ ")
print("|\/| |  |    |    |__| |    |    |  | |    |__|  |  |  | |__/ ")
print("|  |  \/     |___ |  | |___ |___ |__| |___ |  |  |  |__| |  \ ")

print("--------------------------------------------------------------")

# Tenemos cuatro fórmulas
# First -> No tiene distancia
# Second -> No tiene aceleración
# Third -> No tiene velocidad final
# Quarter -> No tiene tiempo


# Solicitar la variable que falta en la ecuación
print("d - Distancia")
print("a - Aceleración")
print("vf - Velocidad final")
print("t - Tiempo")
datoFaltante = str(input("¿Qué variable te falta en la ecuación? "))

if datoFaltante == 'd':
    # Usaremos el dato que oculte la Distancia
    print("vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    incognita = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Hallar la Velocidad Final
    if incognita == 'vf':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        t = int(input("Ingresa el tiempo "))
        def d_vf(vo,a,t):
            resultado = vo+a*t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")
        d_vf(vo,a,t)

    # Hallar la Velocidad Final
    elif incognita == 'vo':
        vf = int(input("Ingresa la velocidad final: "))
        a = int(input("Ingresa la aceleración: "))
        t = int(input("Ingresa el tiempo: "))
        def d_vo(vf,a,t):
            resultado = vf-a*t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")
        d_vo(vf,a,t)

    # Hallar la Aceleración
    elif incognita == 'a':
        vf = int(input("Ingresa la velocidad final: "))
        vo = int(input("Ingresa la velocidad inicial: "))
        t = int(input("Ingresa el tiempo: "))
        def d_a(vf, vo, t):
            resultado = (vf*t)/vo
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s^2")
        d_a(vf,vo,t)

    # Hallar el Tiempo
    elif incognita == 't':
        vf = int(input("Ingresa la velocidad final: "))
        vo = int(input("Ingresa la velocidad inicial: "))
        t = int(input("Ingresa la aceleración: "))
        def d_t(vf, vo, a):
            resultado = (vo+vf)/a
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "s")
        d_t(vf,vo,a)

elif datoFaltante == 'a':
    # Usaremos el dato que oculte la Distancia
    print("vo - Velocidad Inicial, vf - Velocidad Final, t - Tiempo, d - Distancia")
    incognita = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Hallar la velocidad final
    if incognita == 'vo':
        d = int(input("Ingresa la distancia "))
        vf = int(input("Ingresa velocidad final "))
        t = int(input("Ingresa el tiempo "))
        def a_d(d,vf,t):
            resultado = ((2*d)/t)-vf
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")
        a_d(d,vf,t)


    # Hallar la distancia
    if incognita == 'd':
        vo = int(input("Ingresa la velocidad inicial "))
        vf = int(input("Ingresa velocidad final "))
        t = int(input("Ingresa el tiempo "))
        def a_d(vo,vf,t):
            resultado = ((vf+vo)/2)*t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")
        a_d(vo,vf,t)

elif datoFaltante == 'vf':
    print("d - Distancia, vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    incognita = str(input("Genial, ingresa la variable que deseas hallar: "))

    if incognita == 'd':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        t = int(input("Ingresa el tiempo "))
        def vf_d(vo,a,t):
            resultado = vo*t+((a*(t**2))/2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")
        vf_d(vo,a,t)

elif datoFaltante == 't':
    print("d - Distancia, vo - Velocidad Inicial, a - Aceleración, Vf - Velocidad final")
    incognita = str(input("Genial, ingresa la variable que deseas hallar: "))

    if incognita == 'd':
        pass

    if incognita == 'vo':
        pass

    if incognita == 'a':
        pass

    if incognita == 'vf':
        pass

else:
    print("Variable incorrecta o no ingresada")