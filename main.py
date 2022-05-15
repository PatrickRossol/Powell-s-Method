import PySimpleGUI as sg
import numpy as np
from gui import window
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funcHelper import getFunction
from goldSearch import runGold

def clear_canvas(figure):
    figure.get_tk_widget().forget()
    plt.close('all')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    widget = figure_canvas_agg.get_tk_widget()
    figure_canvas_agg.draw()
    widget.pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

figure = None

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Oblicz':
        func = getFunction(values['-FUNC-'])
        if(figure):
            clear_canvas(figure)
        # try:
        eps1= float(values['-EPs2-'])
        eps2= float(values['-EPs3-'])
        limit = int(values['-L-'])
        startPoint = [float(x) for x in str(values['-PP-']).split(',')]
        range = [float(x) for x in str(values['-ZONE-']).split(',')]
        x = np.linspace(-10, 10)
        y = np.linspace(-10, 10)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        Z = np.array(Z)
        Z = np.reshape(Z, (len(x), len(y)))
        plt.clf()
        plt.contour(X, Y, Z)
        runGold(func, startPoint, eps1, eps2, range, limit)
        plt.show()
        #figure = draw_figure(window['-PLOT_CANV-'].TKCanvas, plt.gcf())
        # except Exception as e:
        #     print('Exception :')
        #     print(e)
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
