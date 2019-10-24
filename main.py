print("Movement-Varied-Calculator - MRUV Calculator Python")

#  __  __ __      __   _____        _               _         _
# |  \/  |\ \    / /  / ____|      | |             | |       | |
# | \  / | \ \  / /  | |      __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __
# | |\/| |  \ \/ /   | |     / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
# | |  | |   \  /    | |____| (_| || || (__ | |_| || || (_| || |_| (_) || |
# |_|  |_|    \/      \_____|\__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|
#

print("------------------------------------------------------------------")
print("| _  _ _  _    ____ ____ _    ____ _  _ _    ____ ___ ____ ____  |")
print("| |\/| |  |    |    |__| |    |    |  | |    |__|  |  |  | |__/  |")
print("| |  |  \/     |___ |  | |___ |___ |__| |___ |  |  |  |__| |  \  |")
print("------------------------------------------------------------------")

not_distance_find_final_velocity = lambda iv, a, t: iv + a * t
not_distance_find_initial_velocity = lambda fv, a, t: fv - a * t
not_distance_find_acceleration = lambda fv, iv, t: fv * t / iv
not_distance_find_time = lambda : fv, iv, a: (iv + fv) / a

print("| d  | Distancia       |")
print("| a  | Aceleración     |")
print("| vf | Velocidad final |")
print("| t  | Tiempo          |")

missingData = str(input(">>¿Qué variable te falta en la ecuación? "))

if missingData == 'd':
    print("vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = str(input(">> Genial, ingresa la variable que deseas hallar: "))

    if unknown == 'vf':
        initial_velocity = int(input("Ingresa la velocidad inicial "))
        acceleration = int(input("Ingresa la aceleración "))
        time = int(input("Ingresa el tiempo "))
        result = not_distance_find_final_velocity(initial_velocity, acceleration, time)
        print("El resultado es:\n", result, "m/s")

    # Find final velocity
    elif unknown == 'vo':
        final_velocity = int(input("Ingresa la velocidad final: "))
        acceleration = int(input("Ingresa la aceleración: "))
        time = int(input("Ingresa el tiempo: "))

        result = not_distance_find_initial_velocity(final_velocity, acceleration, time)
        print("El resultado es:\n", result, "m/s")

    # Find acceleration
    elif unknown == 'a':
        final_velocity = int(input("Ingresa la velocidad final: "))
        initial_velocity = int(input("Ingresa la velocidad inicial: "))
        time = int(input("Ingresa el tiempo: "))
        result = not_distance_find_acceleration(final_velocity, initial_velocity, time)
        print("El resultado es:\n", result, "m/s^2")

    # Find time
    elif unknown == 't':
        final_velocity = int(input("Ingresa la velocidad final: "))
        initial_velocity = int(input("Ingresa la velocidad inicial: "))
        acceleration = int(input("Ingresa la aceleración: "))
        result = not_distance_find_time(final_velocity, initial_velocity, acceleration)
        print("El resultado es:\n", result, "s")

elif missingData == 'a':
    print("vo - Velocidad Inicial, vf - Velocidad Final, t - Tiempo, d - Distancia")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Find final velocity
    if unknown == 'vo':
        distance = int(input("Ingresa la distancia "))
        final_velocity = int(input("Ingresa velocidad final "))
        time = int(input("Ingresa el tiempo "))

        def a_d(d, vf, t):
            resultado = ((2 * d) / t) - vf
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")


        a_d(d, vf, t)

    # Find distance
    if unknown == 'd':
        vo = int(input("Ingresa la velocidad inicial "))
        vf = int(input("Ingresa velocidad final "))
        t = int(input("Ingresa el tiempo "))


        def a_d_wtf(vo, vf, t):
            resultado = ((vf + vo) / 2) * t
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")


        a_d_wtf(vo, vf, t)

elif missingData == 'vf':

    print("d - Distancia, vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Find distance
    if unknown == 'd':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        t = int(input("Ingresa el tiempo "))

        def vf_d(vo, a, t):
            resultado = vo * t + ((a * (t ** 2)) / 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")


        vf_d(vo, a, t)

    if unknown == 'vo':
        pass

    if unknown == 't':
        pass

    if unknown == 'a':
        pass

elif missingData == 't':
    print("d - Distancia, vo - Velocidad Inicial, a - Aceleración, Vf - Velocidad final")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    if unknown == 'd':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        vf = int(input("Ingresa la velocidad final "))

        def t_d(vo, a, vf):
            resultado = ((vf ** 2) / (2 * a)) - ((vo ** 2) / (2 * a))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")


        t_d(vo, a, vf)

    if unknown == 'vo':
        d = int(input("Ingresa la distancia "))
        vf = int(input("Ingresa la velocidad final "))
        a = int(input("Ingresa la aceleracion "))


        def t_vo(d, vf, a):
            resultado = math.sqrt((vf ** 2) - (2 * a * d))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")


        t_vo(d, vf, a)

    if unknown == 'a':
        vo = int(input("Ingresa la velocidad inicial "))
        vf = int(input("Ingresa la velocidad final "))
        d = int(input("Ingresa el tiempo "))


        def t_a(vo, vf, d):
            resultado = (((vf) ** 2) / (2 * d)) - ((vo) / (2 * d))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")


        t_a(vo, vf, d)

    if unknown == 'vf':
        vo = int(input("Ingresa la velocidad inicial "))
        a = int(input("Ingresa la aceleración "))
        d = int(input("Ingresa el tiempo "))


        def vf_d(vo, a, d):
            resultado = (((vo) ** 2) + 2 * a * d) ** (2 / 1)
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")


        vf_d(vo, a, d)

else:
    print("Variable incorrecta o no ingresada")
