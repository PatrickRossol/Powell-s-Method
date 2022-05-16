import PySimpleGUI as sg
import numpy as np
from gui import window
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funcHelper import getFunction
from goldSearch import minimizePowell


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
        if(figure):
            clear_canvas(figure)
        try:
            func = getFunction(values['-FUNC-'])
            eps1 = float(values['-EPs2-'])
            eps2 = float(values['-EPs3-'])
            limit = int(values['-L-'])
            startPoint = [float(x) for x in str(values['-PP-']).split(',')]
            range = [float(x) for x in str(values['-ZONE-']).split(',')]
            plt.clf()
            point, value, stop, stopValue = minimizePowell(
                func, startPoint, eps1, eps2, range, limit)
            if(len(startPoint) == 2):
                xmin,xmax = plt.xlim()
                ymin,ymax = plt.ylim()
                x = np.linspace(xmin, xmax)
                y = np.linspace(ymin, ymax)
                X, Y = np.meshgrid(x, y)
                Z = func(X, Y)
                Z = np.array(Z)
                Z = np.reshape(Z, (len(x), len(y)))
                plt.contourf(X, Y, Z, extend='both', levels=50)
                figure = draw_figure(window['-PLOT_CANV-'].TKCanvas, plt.gcf())
            window['textbox'].update(
                f'{values["-FUNC-"]}\n{value}\n{point}\n{stop}\n{stopValue}')
        except Exception as e:
            print('Exception :')
            print(e)
            sg.popup(f'Error: {e}')

window.close()
