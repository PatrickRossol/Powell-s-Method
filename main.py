import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui import window
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

            point, value, stop, stopValue, stepList = minimizePowell(
                func, startPoint, eps1, eps2, range, limit)

            if(len(startPoint) == 2):
                xmin,xmax = plt.xlim()
                ymin,ymax = plt.ylim()
                x = np.linspace(xmin - 2, xmax + 2)
                y = np.linspace(ymin - 2, ymax + 2)
                X, Y = np.meshgrid(x, y)
                Z = func(X, Y)
                Z = np.array(Z)
                Z = np.reshape(Z, (len(x), len(y)))
                plt.contourf(X, Y, Z, extend='both', levels=50)
                figure = draw_figure(window['-PLOT_CANV-'].TKCanvas, plt.gcf())

            index = 0
            minCoord = ""
            funcVal = "f("
            for i in point:
                index = index + 1
                minCoord = minCoord + 'x' + str(index) + '* = ' + str(round(point[index-1],4)) + '\n'
                funcVal = funcVal + 'x' + str(index) + '*,'
            funcVal = funcVal[:-1] + ') = ' + str(round(value,4))

            window['-PC-'].update(minCoord)
            window['-FV-'].update(funcVal)
            window['-KS-'].update(f'{stop}')
            window['-WKS-'].update(f'{stopValue}')
            
            
            pointList = []
            index = 1
            for i in stepList[::2]:
                pointList.append(i)
                
                for j in stepList[index]:
                    pointList.append(j)
                index = index + 2


            dispStep = ""
            index=0
            for i in pointList:
                #roundPointL = [round(num, 4) for num in i]
               # print(roundPointL)
                dispStep = dispStep + "Krok " + str(index) + ': f(' + str([round(num, 4) for num in i]) + ') = ' + str(round(func(*pointList[index]),4)) + '\n'
                #dispStep = dispStep + "Krok " + str(index) + ': f(' + ') = ' + str(func(*i[index])) + '\n'
               # print(i)
                index = index + 1

            window['textbox'].update(dispStep)


        except Exception as e:
            print('Exception :')
            print(e)
            sg.popup(f'Error: {e}')

window.close()
