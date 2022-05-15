import PySimpleGUI as sg
import numpy as np
from gui import window
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from funcHelper import getFunction

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Oblicz':
        func = getFunction(values['-FUNC-'])
        x=np.linspace(-10,10,250)
        y=np.linspace(-10,10,250)
        z= func(x,y)
        try:
            plt.contour(z)
            draw_figure(window['-PLOT_CANV-'].TKCanvas, plt.gcf())
        except Exception as e:
            print(e)
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()