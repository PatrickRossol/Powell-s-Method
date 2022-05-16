import PySimpleGUI as sg

sg.theme('Dark')

left_input_column = [
   # [sg.Graph(canvas_size=(100, 100), graph_bottom_left=(0,0), graph_top_right=(100, 100), background_color='red', key='graph')],

   #[sg.Text('Eps:', size=(4,1)), sg.Input(size=(10,1), key='-EPs1-')],
    [sg.Text('Eps1:', size=(4,1)), sg.Input(size=(10,1), key='-EPs2-',default_text="0.001")],
    [sg.Text('Eps2:', size=(4,1)), sg.Input(size=(10,1), key='-EPs3-',default_text="0.001")],
    [sg.Text('L:', size=(4,1)), sg.Input(size=(10,1), key='-L-', default_text="1000")],
    [sg.Text('Przedział [a,b]:', size=(11,1)), sg.Input(size=(10,1), key='-ZONE-',default_text="-1,1")],
]

frame_1 = [
    [sg.Frame(layout=left_input_column, vertical_alignment = 'c',title='Kryteria stopu', title_location='n')],
]

right_input_column = [
    [sg.Text("Metoda w kierunku")],
    [sg.Combo(["Metoda złotego podziału", 'Metoda aproksymacji kwadratowej'], default_value='Metoda złotego podziału',key='board')],
]

res_left_layout = [
    [sg.Text('Wartość funkcji')],
    [sg.Text('f(x*,y*) = ')], 
    [sg.Text('Współrzędne punktu')], 
    [sg.Text('x* = ')], 
    [sg.Text('y* = ')],


    [sg.Text('Kryterium stopu:', key='-KS-')],
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
    [sg.Input(size=(50,1), key='-FUNC-',default_text='(x1-2)^2+(x1-x2^2)^2')],
    [sg.Text('Punkt początkowy')],
    [sg.Input(size=(50,1), key='-PP-', default_text="-4,-4")],
    [sg.Button('Wyczyść formularz', size = (10,2), button_color= 'gray'), sg.Button('Oblicz', size = (10,2), button_color= 'gray')],
    [sg.Column(frame_res)] 
]


plot_layout = [
    [sg.Canvas(size=(200, 200), key='-PLOT_CANV-')],
]


layout = [
    [sg.vtop(sg.Column(input_data_layout)), sg.VSeparator(), sg.Column(plot_layout)]
]

window = sg.Window('Metoda Powella', layout, finalize=True)
