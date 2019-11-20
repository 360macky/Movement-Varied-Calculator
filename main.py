import math

print("------- Movement-Varied-Calculator - MRUV Calculator Python -------")
print("-------------------------------------------------------------------")
print("|  _  _ _  _    ____ ____ _    ____ _  _ _    ____ ___ ____ ____  |")
print("|  |\/| |  |    |    |__| |    |    |  | |    |__|  |  |  | |__/  |")
print("|  |  |  \/     |___ |  | |___ |___ |__| |___ |  |  |  |__| |  \  |")
print("-------------------------------------------------------------------")
print("----------------------- Physics with Python -----------------------")


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

    # Equations without final velocity
    not_final_velocity_find_distance = lambda self, vo, a, t: vo * t + ((a * (t ** 2)) / 2)

    # Equations without time
    not_time_find_distance = lambda self, iv, a, fv: ((fv ** 2) / (2 * a)) - ((iv ** 2) / (2 * a))
    not_time_find_initial_velocity = lambda self, d, fv, a: math.sqrt((fv ** 2) - (2 * a * d))
    not_time_find_acceleration = lambda iv, fv, d: (((fv) ** 2) / (2 * d)) - ((iv) / (2 * d))
    not_time_find_final_velocity = lambda iv, a, d: (((iv) ** 2) + 2 * a * d) ** (2 / 1)

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

print("| d  -> Distancia       |")
print("| a  -> Aceleración     |")
print("| vf -> Velocidad final |")
print("| t  -> Tiempo          |")


def show_result(result, type_result):
    print("El resultado es: ", result, type_result)


missingData = str(input(">> ¿Qué variable te falta en la ecuación? "))

if missingData == 'd':
    print("vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = mv.get_unknown_variable()

    if unknown == 'vf':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()
        
        result = mv.not_distance_find_final_velocity(initial_velocity, acceleration, time)
        show_result(result, "m/s")

    elif unknown == 'vo':
        final_velocity = mv.get_final_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()

        result = mv.not_distance_find_initial_velocity(final_velocity, acceleration, time)
        print("El resultado es: ", result, "m/s")

    elif unknown == 'a':
        final_velocity = mv.get_final_velocity()
        initial_velocity = mv.get_initial_velocity()
        time = mv.get_time()

        result = mv.not_distance_find_acceleration(final_velocity, initial_velocity, time)
        show_result(result, "m/s^2")

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

    if unknown == 'vo':
        distance = mv.get_distance()
        final_velocity = mv.get_final_velocity()
        time = mv.get_time()

        result = mv.not_acceleration_find_initial_velocity(distance, final_velocity, time)
        show_result(result, "m/s")
        
    elif unknown == 'd':
        initial_velocity = mv.get_initial_velocity()
        final_velocity = mv.get_final_velocity()
        time = mv.get_time()
        
        result = mv.not_acceleration_find_distance(initial_velocity, final_velocity, time)
        show_result(result, "m")

elif missingData == 'vf':

    print("d - Distancia, vo - Velocidad Inicial, t - Tiempo, a - Aceleración")
    unknown = str(input("Genial, ingresa la variable que deseas hallar: "))

    if unknown == 'd':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        time = mv.get_time()

        result = mv.not_final_velocity_find_distance(initial_velocity, acceleration, time)

        show_result(result, "m")

    elif unknown == 'vo':
        # TODO: Without final velocity find initial velocity
        pass

    elif unknown == 't':
        # TODO: Without final velocity find time
        pass

    elif unknown == 'a':
        # TODO: Without final velocity find acceleration
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

        result = mv.not_time_find_distance(initial_velocity, acceleration, final_velocity)

        show_result(result, "m")

    elif unknown == 'vo':
        distance = mv.get_distance()
        final_velocity = mv.get_final_velocity()
        acceleration = mv.get_acceleration()

        result = mv.not_time_find_initial_velocity(distance, final_velocity, acceleration)

        show_result(result, "m/s")

    elif unknown == 'a':
        initial_velocity = mv.get_initial_velocity()
        final_velocity = mv.get_final_velocity()
        distance = mv.get_distance()

        result = mv.not_time_find_acceleration(initial_velocity, final_velocity, distance)

        show_result(result, "m/s^2")

    elif unknown == 'vf':
        initial_velocity = mv.get_initial_velocity()
        acceleration = mv.get_acceleration()
        distance = mv.get_distance()

        result = mv.not_time_find_final_velocity(initial_velocity, acceleration, distance)

        show_result(result, "m/s^2")

    else:
        mv.print_variable_not_found()

else:
    mv.print_variable_not_found() 
