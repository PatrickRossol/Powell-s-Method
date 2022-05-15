import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

sg.theme('Dark')

left_input_column = [
   # [sg.Graph(canvas_size=(100, 100), graph_bottom_left=(0,0), graph_top_right=(100, 100), background_color='red', key='graph')],

   #[sg.Text('Eps:', size=(4,1)), sg.Input(size=(10,1), key='-EPs1-')],
    [sg.Text('Eps1:', size=(4,1)), sg.Input(size=(10,1), key='-EPs2-')],
    [sg.Text('Eps2:', size=(4,1)), sg.Input(size=(10,1), key='-EPs3-')],
    [sg.Text('L:', size=(4,1)), sg.Input(size=(10,1), key='-L-')],
    [sg.Text('Przedział [a,b]:', size=(11,1)), sg.Input(size=(10,1), key='-ZONE-')],
]

frame_1 = [
    [sg.Frame(layout=left_input_column, vertical_alignment = 'c',title='Kryteria stopu', title_location='n')],
]

right_input_column = [
    [sg.Text("Metoda w kierunku")],
    [sg.Combo(["Metoda złotego podziału", 'Metoda aproksymacji kwadratowej', 'test2'], default_value='Metoda złotego podziału',key='board')],
]

res_left_layout = [
    [sg.Text('Wartość funkcji')],
    [sg.Text('f(x*,y*) = ')], 
    [sg.Text('Współrzędne punktu')], 
    [sg.Text('x* = ')], 
    [sg.Text('y* = ')],


    [sg.Text('Kryterium stopu:')],
    [sg.Text('Wartośc kryterium stopu:')],
]

res_right_layout = [
    [sg.Multiline(size=(30, 10), key='textbox')]
]

res_main_layout = [
    [sg.Column(res_left_layout), sg.Column(res_right_layout)]
]

frame_res = [
    [sg.Frame(layout=res_main_layout, vertical_alignment = 'c',title='Rozwiązanie', title_location='n')],
]

input_data_layout = [
    [sg.Column(frame_1), sg.Column(right_input_column)],
    [sg.Text('Wprowadź funkcję')],
    [sg.Input(size=(50,1), key='-FUNC-')],
    [sg.Text('Punkt początkowy')],
    [sg.Input(size=(50,1), key='-PP-')],
    [sg.Button('Wyczyść formularz', size = (10,2), button_color= 'gray'), sg.Button('Oblicz', size = (10,2), button_color= 'gray')],
    [sg.Column(frame_res)] 
]




plot_layout = [
    [sg.Canvas(size=(200, 200), key='-PLOT_CANV-')],
]



layout = [
    [sg.vtop(sg.Column(input_data_layout)), sg.VSeparator(), sg.Column(plot_layout)]
]






year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
unemployment_rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
  
def create_plot(year, unemployment_rate):
    plt.plot(year, unemployment_rate, color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Unemployment Rate', fontsize=14)
    plt.grid(True)
    return plt.gcf()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


window = sg.Window('Metoda Powella', layout, finalize=True)



draw_figure(window['-PLOT_CANV-'].TKCanvas, create_plot(year, unemployment_rate))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()