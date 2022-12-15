import matplotlib.pyplot as plt
import skfuzzy as fuzz
import numpy as np

# Descripción: Función que crea las funciones de pertetencia.
# Entradas: void.
# Salida: Un diccionario con las funciones de pertenencia.
def funcionesPertenencia():
    x = np.arange(0, 11)  # Arreglo para los valores
    # Diccionario que almacena las funciones de pertenencia, las posiciones representan baja, media y alta
    funcPertenencia = dict(frecuencia_estornudos=[0, 0, 0], grado_congestion=[0, 0, 0], tos=[0, 0, 0], numero_familiares=[0, 0, 0], edad=[0, 0, 0], Baja=0, Media=0, Alta=0)
    # Cantidad de integrantes
    # Función de pertenencia trapezoidal para la frecuencia de estornudos baja, se considera el rango de valores de 1 a 4
    funcPertenencia['frecuencia_estornudos'][0] = fuzz.trapmf(x, [0, 0, 1, 4])
    # Función de pertenencia trapezoidal para la frecuencia de estornudos media, se considera el rango de valores de 2 a 7
    funcPertenencia['frecuencia_estornudos'][1] = fuzz.trimf(x, [2, 4, 6])
    # Función de pertenencia trapezoidal para la frecuencia de estornudos alta, se considera el rango de valores de 5 a 10
    funcPertenencia['frecuencia_estornudos'][2] = fuzz.trapmf(x, [5, 6, 10, 10])

    # Función de pertenencia trapezoidal para la el grado de congestión bajo, se considera el rango de valores de 1 a 4
    funcPertenencia['grado_congestion'][0] = fuzz.trapmf(x, [0, 0, 1, 3])
    # Función de pertenencia trapezoidal para la el grado de congestión medio, se considera el rango de valores de 2 a 4
    funcPertenencia['grado_congestion'][1] = fuzz.trimf(x, [1, 2, 4])
    # Función de pertenencia trapezoidal para la el grado de congestión alto, se considera el rango de valores de 3 a 10
    funcPertenencia['grado_congestion'][2] = fuzz.trapmf(x, [3, 4, 10, 10])

    # Función de pertenencia trapezoidal para la el grado de tos baja, se considera el rango de valores de 1 a 4
    funcPertenencia['tos'][0] = fuzz.trimf(x, [0, 0, 2])
    # Función de pertenencia trapezoidal para la el grado de tos media, se considera el rango de valores de 2 a 7
    funcPertenencia['tos'][1] = fuzz.trapmf(x, [1, 3, 4, 5])
    # Función de pertenencia trapezoidal para la el grado de tos alta, se considera el rango de valores de 5 a 10
    funcPertenencia['tos'][2] = fuzz.trapmf(x, [4, 6, 10, 10])

    # Función de pertenencia trapezoidal para la presencia de sonidos mezclados baja, se considera el rango de valores de 1 a 4
    funcPertenencia['numero_familiares'][0] = fuzz.trapmf(x, [0, 0, 1, 3])  # Triangulo: Número de familiares menores a 4
    funcPertenencia['numero_familiares'][1] = fuzz.trapmf(x, [2, 3, 4, 6])  # Trapecio: Número de familiares de 4 a 6
    funcPertenencia['numero_familiares'][2] = fuzz.trapmf(x, [4, 6, 10, 10])  # Trapecio: Número de familiares de 7 a 10

    # Función de pertenencia trapezoidal para la edad infante, se considera el rango de valores de 1 a 4
    funcPertenencia['edad'][0] = fuzz.trimf(x, [0, 0, 2])
    # Función de pertenencia trapezoidal para la edad joven, se considera el rango de valores de 2 a 7
    funcPertenencia['edad'][1] = fuzz.trimf(x, [1, 2, 3])
    # Función de pertenencia trapezoidal para la edad adulta, se considera el rango de valores de 5 a 10
    funcPertenencia['edad'][2] = fuzz.trapmf(x, [2, 4, 10, 10])

    funcPertenencia['Baja'] = fuzz.trapmf(x, [0, 0, 2, 3])
    funcPertenencia['Media'] = fuzz.trapmf(x, [2, 4, 6, 7])
    funcPertenencia['Alta'] = fuzz.trapmf(x, [6, 9, 10, 10])
    return funcPertenencia

# Descripción: Función que realiza la fusificación con los datos de entrada, para cada funcion de pertenencia.
# Entradas: un diccionario con las funciones de pertenencia y una lista con las entradas del usuario.
# Salida: Un diccionario con los resultados de la fusificación.
def fusificarEntrada(funcPertenencia, entradaUsuario):
    # Arreglo para los valores
    x = np.arange(0, 11)

    # Diccionario para almacenar valores fusificados
    fusificacion = dict(frecuencia_estornudos=[0, 0, 0], grado_congestion=[0, 0, 0], tos=[0, 0, 0], numero_familiares=[0, 0, 0], edad=[0, 0, 0])

    # Fusifica valores con entradas
    # Frecuencia de estornudos
    fusificacion['frecuencia_estornudos'][0] = fuzz.interp_membership(x, funcPertenencia['frecuencia_estornudos'][0], entradaUsuario[0])
    fusificacion['frecuencia_estornudos'][1] = fuzz.interp_membership(x, funcPertenencia['frecuencia_estornudos'][1], entradaUsuario[0])
    fusificacion['frecuencia_estornudos'][2] = fuzz.interp_membership(x, funcPertenencia['frecuencia_estornudos'][2], entradaUsuario[0])

    # Grado de congestión
    fusificacion['grado_congestion'][0] = fuzz.interp_membership(x, funcPertenencia['grado_congestion'][0], entradaUsuario[1])
    fusificacion['grado_congestion'][1] = fuzz.interp_membership(x, funcPertenencia['grado_congestion'][1], entradaUsuario[1])
    fusificacion['grado_congestion'][2] = fuzz.interp_membership(x, funcPertenencia['grado_congestion'][2], entradaUsuario[1])

    # Frecuencia de tos
    fusificacion['tos'][0] = fuzz.interp_membership(x, funcPertenencia['tos'][0], entradaUsuario[2])
    fusificacion['tos'][1] = fuzz.interp_membership(x, funcPertenencia['tos'][1], entradaUsuario[2])
    fusificacion['tos'][2] = fuzz.interp_membership(x, funcPertenencia['tos'][2], entradaUsuario[2])

    # Número de familiares con síntomas o sospechas de alergia
    fusificacion['numero_familiares'][0] = fuzz.interp_membership(x, funcPertenencia['numero_familiares'][0], entradaUsuario[3])
    fusificacion['numero_familiares'][1] = fuzz.interp_membership(x, funcPertenencia['numero_familiares'][1], entradaUsuario[3])
    fusificacion['numero_familiares'][2] = fuzz.interp_membership(x, funcPertenencia['numero_familiares'][2], entradaUsuario[3])

    # Edad del paciente
    fusificacion['edad'][0] = fuzz.interp_membership(x, funcPertenencia['edad'][0], entradaUsuario[4])
    fusificacion['edad'][1] = fuzz.interp_membership(x, funcPertenencia['edad'][1], entradaUsuario[4])
    fusificacion['edad'][2] = fuzz.interp_membership(x, funcPertenencia['edad'][2], entradaUsuario[4])
    
    print(entradaUsuario)
    return fusificacion

# Descripción: Función que realiza la inferencia de Mamdani
# Entardas: Diccionario con las funciones de pertenencia fusificadas
# Salida: int
def reglas(fusificacion):
    # Reglas:
    # Si la edad es 0 o 1 (niño o joven) y tiene alta congestion y altos estornudos, alergia alta
    regla1 = np.fmin(np.fmax(fusificacion['edad'][0], fusificacion['edad'][1]), np.fmin(fusificacion['grado_congestion'][2], fusificacion['frecuencia_estornudos'][2]))
    corte1 = np.fmin(regla1, funcPertenencia['Alta'])
    # Si la edad es 2 (adulto) y tiene baja o media congestion y baja o media de estornudos, alergia media
    regla2 = np.fmin(np.fmin(fusificacion['edad'][2], np.fmax(fusificacion['grado_congestion'][0], fusificacion['grado_congestion'][1])), np.fmax(fusificacion['frecuencia_estornudos'][0], fusificacion['frecuencia_estornudos'][1]))
    corte2 = np.fmin(regla2, funcPertenencia['Media'])
    # Si tiene baja tos, baja congestion y baja frecuencia de estornudos y tiene pocos familiares con síntomas, alergia baja
    regla3 = np.fmin(np.fmin(np.fmin(fusificacion['tos'][0], fusificacion['grado_congestion'][0]),fusificacion['frecuencia_estornudos'][0]), fusificacion['numero_familiares'][0])
    corte3 = np.fmin(regla3, funcPertenencia['Baja'])
    # Si tiene alta tos, alta congestion y alta frecuencia de estornudos y cantidad media o alta de familiares con alergia alta
    regla4 = np.fmin(np.fmin(np.fmin(fusificacion['tos'][2], fusificacion['grado_congestion'][2]), fusificacion['frecuencia_estornudos'][2]), np.fmax(fusificacion['numero_familiares'][1], fusificacion['numero_familiares'][2]))
    corte4 = np.fmin(regla4, funcPertenencia['Alta'])
    # Si la edad es 0 (niño) y tiene alta tos y alta congestion o alta tos y alta frecuencia de estornudos o alta congestion y alta frecuencia de estornudos, alergia alta
    regla5 = np.fmin(fusificacion['edad'][0], np.fmax(np.fmax(np.fmin(fusificacion['tos'][2], fusificacion['grado_congestion'][2]), np.fmin(fusificacion['tos'][2], fusificacion['frecuencia_estornudos'][2])), np.fmin(fusificacion['grado_congestion'][2], fusificacion['frecuencia_estornudos'][2])))
    corte5 = np.fmin(regla5, funcPertenencia['Alta'])
    # Si la edad es 2 (adulto) y tiene baja tos y baja congestion o baja tos y baja frecuencia de estornudos o baja congestion y baja frecuencia de estornudos, alergia baja
    regla6 = np.fmin(fusificacion['edad'][2], np.fmax(np.fmax(np.fmin(fusificacion['tos'][0], fusificacion['grado_congestion'][0]), np.fmin(fusificacion['tos'][0], fusificacion['frecuencia_estornudos'][0])), np.fmin(fusificacion['grado_congestion'][0], fusificacion['frecuencia_estornudos'][0])))
    corte6 = np.fmin(regla6, funcPertenencia['Baja'])
    
    # Si la cantidad de familiares con síntomas es baja y tiene media tos y media congestion o media tos y media frecuencia de estornudos o media congestion y media frecuencia de estornudos, alergia media
    regla7 = np.fmin(fusificacion['numero_familiares'][0], np.fmax(np.fmax(np.fmin(fusificacion['tos'][1], fusificacion['grado_congestion'][1]), np.fmin(fusificacion['tos'][1], fusificacion['frecuencia_estornudos'][1])), np.fmin(fusificacion['grado_congestion'][1], fusificacion['frecuencia_estornudos'][1])))
    corte7 = np.fmin(regla7, funcPertenencia['Media'])

    # Si la cantidad de familiares con síntomas es medio o alta y tiene media tos y media congestion o media tos y media frecuencia de estornudos o media congestion y media frecuencia de estornudos, alergia alta
    regla8 = np.fmin(np.fmax(fusificacion['numero_familiares'][1], fusificacion['numero_familiares'][2]), np.fmax(np.fmax(np.fmin(fusificacion['tos'][1], fusificacion['grado_congestion'][1]), np.fmin(fusificacion['tos'][1], fusificacion['frecuencia_estornudos'][1])), np.fmin(fusificacion['grado_congestion'][1], fusificacion['frecuencia_estornudos'][1])))
    corte8 = np.fmin(regla8, funcPertenencia['Alta'])

    # Se obtiene el resultado final
    resultado = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(corte1, corte2), corte3), corte4), corte5), corte6), corte7), corte8)
    print("Resultado: ", resultado)
    return resultado

# Descripción: Funcion encargada de realizar todos los graficos de funciones de pertenencia
# Entradas: Diccionario con funciones de pertenencia
# Salida: Void
def graficar(funcPertenencia):
    fig1 = plt.figure("Sintomas de alergia")
    # Arreglo para los valores
    x = np.arange(0, 11)
    # Multiples gráficos en una ventana
    fig = plt.figure()
    fig.clf()
    ax = fig.subplots(2, 3)
    # Frecuencia de estornudos
    ax[0, 0].set_title("Frecuencia diaria de estornudos")
    ax[0, 0].plot(x, funcPertenencia['frecuencia_estornudos'][0], 'r', label='Baja')
    ax[0, 0].plot(x, funcPertenencia['frecuencia_estornudos'][1], 'g', label='Media')
    ax[0, 0].plot(x, funcPertenencia['frecuencia_estornudos'][2], 'b', label='Alta')
    ax[0, 0].legend()
    ax[0, 0].grid()
    # Grado de congestión nasal
    ax[0, 1].set_title("Grado congestión de nasal")
    ax[0, 1].plot(x, funcPertenencia['grado_congestion'][0], 'r', label='Baja')
    ax[0, 1].plot(x, funcPertenencia['grado_congestion'][1], 'g', label='Media')
    ax[0, 1].plot(x, funcPertenencia['grado_congestion'][2], 'b', label='Alta')
    ax[0, 1].legend()
    ax[0, 1].grid()
    # Frecuencia de tos
    ax[0, 2].set_title("Frecuencia diaria de tos")
    ax[0, 2].plot(x, funcPertenencia['tos'][0], 'r', label='Baja')
    ax[0, 2].plot(x, funcPertenencia['tos'][1], 'g', label='Media')
    ax[0, 2].plot(x, funcPertenencia['tos'][2], 'b', label='Alta')
    ax[0, 2].legend()
    ax[0, 2].grid()
    # Número de familiares con síntomas o sospechas de alergia
    ax[1, 0].set_title("Numero de familiares con alergia al polen")
    ax[1, 0].plot(x, funcPertenencia['numero_familiares'][0], 'r', label='Baja')
    ax[1, 0].plot(x, funcPertenencia['numero_familiares'][1], 'g', label='Media')
    ax[1, 0].plot(x, funcPertenencia['numero_familiares'][2], 'b', label='Alta')
    ax[1, 0].legend()
    ax[1, 0].grid()
    # Edad del paciente
    ax[1, 1].set_title("Edad del paciente")
    ax[1, 1].plot(x, funcPertenencia['edad'][0], 'r', label='Niño')
    ax[1, 1].plot(x, funcPertenencia['edad'][1], 'g', label='Joven')
    ax[1, 1].plot(x, funcPertenencia['edad'][2], 'b', label='Adulto')
    ax[1, 1].legend()
    ax[1, 1].grid()
    # Géneros
    ax[1, 2].set_title("Grado de alergia al polen")
    ax[1, 2].plot(x, funcPertenencia['Baja'], 'r', label='Baja')
    ax[1, 2].plot(x, funcPertenencia['Media'], 'g', label='Media')
    ax[1, 2].plot(x, funcPertenencia['Alta'], 'b', label='Alta')
    ax[1, 2].legend()
    ax[1, 2].grid()
    fig.show()

# Descripción: Función utilizada para determinar  el género y canción según los resultados obtenidos
# Entrada: Int y Diccionario con funciones de pertenencia
# Salida; Strings
def generoSalida(resultado, funcPertenencia):
    x = np.arange(0, 11)

    Baja = fuzz.interp_membership(x, funcPertenencia['Baja'], resultado)

    Media = fuzz.interp_membership(x, funcPertenencia['Media'], resultado)

    Alta = fuzz.interp_membership(x, funcPertenencia['Alta'], resultado)

    maximo = max(Baja, Media, Alta)

    if(maximo == Baja):
        return "Su nivel de alergia al polen es leve"

    elif(maximo == Media):
        return "Su nivel de alergia al polen es media"

    elif(maximo == Alta):
        return "Su nivel de alergia al polen es grave"
    return 0


#### MAIN ####
funcPertenencia = funcionesPertenencia()

def run(entradaUsuario):     # Preferencias ingresadas por el usuario
    # Crea y grafica funciones de pertenencia
    graficar(funcPertenencia)
    # Realiza la fusificación de los valores ingresados
    fusificacion = fusificarEntrada(funcPertenencia, entradaUsuario)
    # Aplica la inferencia de Madmani con el sistema de inferencia
    resultado = reglas(fusificacion)
    x = np.arange(0, 11)
    try:
        salida = fuzz.defuzz(x, resultado, 'bisector')
    except:
        return ("No hay resultados encontrados para estos niveles de síntomas")
    return generoSalida(salida, funcPertenencia)
