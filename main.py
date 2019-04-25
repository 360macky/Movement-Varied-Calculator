print("MoveMind - MRUV Calculator Python")


#  __  __ __      __   _____        _               _         _
# |  \/  |\ \    / /  / ____|      | |             | |       | |
# | \  / | \ \  / /  | |      __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __
# | |\/| |  \ \/ /   | |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
# | |  | |   \  /    | |____| (_| || || (__ | |_| || || (_| || |_| (_) || |
# |_|  |_|    \/      \_____|\__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|
#


# Tenemos cuatro fórmulas
# First -> No tiene distancia
# Second -> No tiene aceleración
# Third -> No tiene velocidad final
# Quarter -> No tiene tiempo

print("d - Distancia")
print("a - Aceleración")
print("vf - Velocidad final")
print("t - Tiempo")
datoFaltante = str(input("¿Qué variable te falta en la ecuación? "))

if datoFaltante == 'd':
    print("vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    incognita = str(input("Genial, ingresa la variable que deseas hallar: "))

    if incognita == 'vf':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        t = int(input("Ingresa el tiempo "))
        def d_vf(vo,a,t):
            resultado = vo+a*t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")
        d_vf(vo,a,t)
    elif incognita == 'vo':
        vf = int(input("Ingresa la velocidad final: "))
        a = int(input("Ingresa la aceleración: "))
        t = int(input("Ingresa el tiempo: "))
        def d_vo(vf,a,t):
            resultado = vf-a*t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")
        d_vo(vf,a,t)
    elif incognita == 'a':
        vf = int(input("Ingresa la velocidad final: "))
        vo = int(input("Ingresa la velocidad inicial: "))
        t = int(input("Ingresa el tiempo: "))
        def d_a(vf, vo, t):
            resultado = (vf*t)/vo
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s^2")
        d_a(vf,vo,t)

elif datoFaltante == 'a':
    print("Intentas hallar la aceleración")
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
        print("El resultado es:\n" + resultado)

    vf_d(vo,a,t)

elif datoFaltante == 't':
    print("Intentas hallar el tiempo")
else:
    print("Variable incorrecta o no ingresada")
    
# Creado por 360macky
