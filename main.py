import math

print("Movement-Varied-Calculator - MRUV Calculator Python")

print("------------------------------------------------------------------")
print("| _  _ _  _    ____ ____ _    ____ _  _ _    ____ ___ ____ ____  |")
print("| |\/| |  |    |    |__| |    |    |  | |    |__|  |  |  | |__/  |")
print("| |  |  \/     |___ |  | |___ |___ |__| |___ |  |  |  |__| |  \  |")
print("------------------------------------------------------------------")


class MovementVariedCalculator:
    """Uniform Rectilinear Motion Calculation"""

    # Equations without distance
    not_distance_find_final_velocity = lambda self, iv, a, t: iv + a * t
    not_distance_find_initial_velocity = lambda self, fv, a, t: fv - a * t
    not_distance_find_acceleration = lambda self, fv, iv, t: fv * t / iv
    not_distance_find_time = lambda self, fv, iv, a: (fv + iv) / a

    # Equations without acceleration
    not_acceleration_find_initial_velocity = lambda self, d, fv, t: ((2 * d) / t) - fv
    not_acceleration_find_distance = lambda self, iv, fv, t: ((fv + iv) / 2) * t    

    def get_unknown_variable(self):
        return str(input("Genial, ingresa la variable que deseas hallar: "))
    def print_variable_not_found(self):
        print("Variable incorrecta o no ingresada")
    def get_initial_velocity(self):
        return int(input("Ingresa la velocidad inicial: "))
    def get_final_velocity(self):
        return int(input("Ingresa la velocidad final: "))            
    def get_acceleration(self):
        return int(input("Ingresa la aceleración: "))
    def get_time(self):
        return int(input("Ingresa el tiempo: "))
    def get_distance(self):
        return int(input("Ingresa la distancia: "))



mv = MovementVariedCalculator()

print("| d  | Distancia       |")
print("| a  | Aceleración     |")
print("| vf | Velocidad final |")
print("| t  | Tiempo          |")


def show_result(result, type_result):
    print("El resultado es: ", result, type_result)


missingData = str(input(">> ¿Qué variable te falta en la ecuación? "))

if missingData == 'd':
    print("vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = mv.get_unknown_variable()

    # Find final velocity
    if unknown == 'vf':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()
        
        result = mv.not_distance_find_final_velocity(initial_velocity, acceleration, time)
        show_result(result, "m/s")

    # Find initial velocity
    elif unknown == 'vo':
        final_velocity = mv.get_final_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()

        result = mv.not_distance_find_initial_velocity(final_velocity, acceleration, time)
        print("El resultado es: ", result, "m/s")

    # Find acceleration
    elif unknown == 'a':
        final_velocity = mv.get_final_velocity()
        initial_velocity = mv.get_initial_velocity()
        time = mv.get_time()

        result = mv.not_distance_find_acceleration(final_velocity, initial_velocity, time)
        show_result(result, "m/s^2")

    # Find time
    elif unknown == 't':
        final_velocity = mv.get_final_velocity()
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        
        result = mv.not_distance_find_time(final_velocity, initial_velocity, acceleration)
        show_result(result, "s")

    else:
        mv.print_variable_not_found()

elif missingData == 'a':
    print("vo - Velocidad Inicial, vf - Velocidad Final, t - Tiempo, d - Distancia")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Find final velocity
    if unknown == 'vo':
        distance = mv.get_distance()
        final_velocity = mv.get_final_velocity()
        time = mv.get_time()

        result = mv.not_acceleration_find_initial_velocity(distance, final_velocity, time)
        show_result(result, "m/s")
        
    # Find distance
    elif unknown == 'd':
        initial_velocity = mv.get_initial_velocity()
        final_velocity = mv.get_final_velocity()
        time = mv.get_time()
        
        result = mv.not_acceleration_find_distance(initial_velocity, final_velocity, time)
        show_result(result, "m")

elif missingData == 'vf':

    print("d - Distancia, vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    # Find distance
    if unknown == 'd':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()

        def vf_d(vo, a, t):
            resultado = vo * t + ((a * (t ** 2)) / 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")

        vf_d(initial_velocity, acceleration, time)

    elif unknown == 'vo':
        pass

    elif unknown == 't':
        pass

    elif unknown == 'a':
        pass
    
    else:
        mv.print_variable_not_found()

elif missingData == 't':
    print("d - Distancia, vo - Velocidad Inicial, a - Aceleración, Vf - Velocidad final")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    if unknown == 'd':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        final_velocity = mv.get_final_velocity()

        def t_d(vo, a, vf):
            resultado = ((vf ** 2) / (2 * a)) - ((vo ** 2) / (2 * a))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m")

        t_d(initial_velocity, acceleration, final_velocity)

    elif unknown == 'vo':
        distance = mv.get_distance()
        final_velocity = mv.get_final_velocity()
        acceleration = mv.get_acceleration()

        def t_vo(d, vf, a):
            resultado = math.sqrt((vf ** 2) - (2 * a * d))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")

        t_vo(distance, final_velocity, acceleration)

    elif unknown == 'a':
        initial_velocity = mv.get_initial_velocity()
        final_velocity = mv.get_final_velocity()
        distance = mv.get_distance()

        def t_a(vo, vf, d):
            resultado = (((vf) ** 2) / (2 * d)) - ((vo) / (2 * d))
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")

        t_a(initial_velocity, final_velocity, distance)

    elif unknown == 'vf':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        distance = mv.get_distance()

        def vf_d(vo, a, d):
            resultado = (((vo) ** 2) + 2 * a * d) ** (2 / 1)
            resultado = round(resultado, 2)
            resultado = str(resultado)
            print("El resultado es:\n" + resultado + "m/s")

        vf_d(initial_velocity, acceleration, distance)
    else:
        mv.print_variable_not_found()

else:
    mv.print_variable_not_found() 
