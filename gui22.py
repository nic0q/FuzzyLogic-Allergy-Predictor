import PySimpleGUI as sg
from taller22 import run

#Descripción:Función encargada realizar una transformación de los slider a un arreglo de enteros para utilizarse según lo desarrollado en base a logica difusa
#Entrada: void
#Salida: Arreglo de enteros
def evaluacion():
    frecuencia_estornudos = grado_congestion = tos = numero_familiares = edad = 0
    while True:
        event, values = window.read()
        if event == 'Enviar':
            break
        frecuencia_estornudos = int(values['-frecuencia_estornudos-'])
        grado_congestion = int(values['-grado_congestion-'])
        tos = int(values['-tos-'])
        numero_familiares = int(values['-numero_familiares-'])
        edad = values['-edad-']
        if(edad == ''):
            edad = 0
    return [frecuencia_estornudos, grado_congestion, tos, numero_familiares, int(int(edad)/10)]

#Descripción:Imprime los resultados
#Entrada: void
#Salida: void
def imprimir_resultados():
    while True:
        event, values = window_resultados.read()
        if event == 'Cerrar' or event == sg.WIN_CLOSED:
            break

while(True):
    sg.ChangeLookAndFeel('DarkTanBlue')
    title = sg.Text('¿Qué grado de alergia al polen tengo?', justification='center', font=("Comic Sans MS", 25))
    layout = [
        [sg.Column([[title]], justification='center')],
        [   sg.T('Con que frecuencia frecuencia estornudas diariamente', justification='left', font=('Comic Sans MS', 15)), 
            sg.Push(),
            sg.Slider(range=(0, 10), enable_events=True, default_value=0, size=(30, 10), orientation='h', font=('Comic Sans MS', 11), key='-frecuencia_estornudos-')
        ],
        [   sg.T('Que grado de congestión tienes regularmente cuando sales a la calle?', justification='left', font=('Comic Sans MS', 15)), 
            sg.Push(),
            sg.Slider(range=(0, 10), enable_events=True, default_value=0, size=(30, 10), orientation='h', font=('Comic Sans MS', 11), key='-grado_congestion-')
        ],
        [   sg.T('Con que frecuencia frecuencia toses diariamente', justification='left', font=('Comic Sans MS', 15)), 
            sg.Push(),
            sg.Slider(range=(0, 10), enable_events=True, default_value=0, size=(30, 10), orientation='h', font=('Comic Sans MS', 11), key='-tos-')
        ],
        [   sg.T('Número de Familiares que tienen alergia', justification='left', font=('Comic Sans MS', 15)), 
            sg.Push(),
            sg.Slider(range=(0, 10), enable_events=True, default_value=0, size=(30, 10), orientation='h', font=('Comic Sans MS', 11), key='-numero_familiares-')
        ],
        [   sg.T('¿Cual es tu rango de edad?', justification='left', font=('Comic Sans MS', 15)), 
            sg.Push(),
            sg.InputText(key = "-edad-", enable_events=True, size=(30, 10),  font=("Comic Sans MS", 11)),
        ],
        [sg.Button('Enviar'), sg.Button('Cerrar')]
    ]
    window = sg.Window('Diagnóstico de grado alergia al polen', layout, default_element_size=(40, 1), grab_anywhere=False)

    event, values = window.read()
    if event == 'Cerrar' or event == sg.WIN_CLOSED:
        break
    entrada = evaluacion()
    window.close()
    resultados = run(entrada)
    
    if resultados == "No hay resultados encontrados para estas opciones":
        layout_resultados = [
        [sg.Column([[sg.Text('Resultados', justification='center', font=("Comic Sans MS", 25))]], justification='center')],
        [sg.T(f' {resultados}', justification='left', font=('Comic Sans MS', 15))], 
        [sg.Button('Cerrar')]
    ]
    else:
        layout_resultados = [
            [sg.Column([[sg.Text('Resultados', justification='center', font=("Comic Sans MS", 25))]], justification='center')],
            [sg.T(resultados, justification='left', font=('Comic Sans MS', 15))], 
            [sg.Button('Cerrar')]]
    window_resultados = sg.Window('Diagnóstico de grado de alergia al polen', layout_resultados, default_element_size=(40, 1), grab_anywhere=False)
    imprimir_resultados()
    event, values = window_resultados.read()
    if event == 'Cerrar' or event == sg.WIN_CLOSED:
        window_resultados.close()