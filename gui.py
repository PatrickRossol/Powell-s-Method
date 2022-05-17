import PySimpleGUI as sg

sg.theme('Dark')

stop_criteria_column = [
   # [sg.Graph(canvas_size=(100, 100), graph_bottom_left=(0,0), graph_top_right=(100, 100), background_color='red', key='graph')],

   #[sg.Text('Eps:', size=(4,1)), sg.Input(size=(10,1), key='-EPs1-')],
    [sg.Text('Eps1:', size=(4,1)), sg.Input(size=(10,1), key='-EPs2-',default_text="0.001")],
    [sg.Text('Eps2:', size=(4,1)), sg.Input(size=(10,1), key='-EPs3-',default_text="0.001")],
    [sg.Text('L:', size=(4,1)), sg.Input(size=(10,1), key='-L-', default_text="1000")],
   # [sg.Text('Przedział [a,b]:', size=(11,1)), sg.Input(size=(10,1), key='-ZONE-',default_text="-1,1")],
]

s_criteria_frame = [
    [sg.Frame(layout=stop_criteria_column, vertical_alignment = 'c',title='Kryteria stopu', title_location='n')],
]

method_choice_column = [
    [sg.Text("Metoda w kierunku")],
    [sg.Combo(["Metoda złotego podziału", 'Metoda aproksymacji kwadratowej'], default_value='Metoda złotego podziału',size=(25,1),key='board')],
]

method_param_column = [
    [sg.Text('Przedział [a,b]:', size=(11,1)), sg.Input(size=(10,1), key='-ZONE-',default_text="-1,1")]
]

method_param_frame = [
    [sg.Frame(layout=method_param_column, vertical_alignment = 'c',title='Parametry met. ZP', title_location='n')],
]

method_column = [
    [sg.Column(method_choice_column)],
    [sg.Column(method_param_frame)]
]

res_left_layout = [
    [sg.Text('Wartość funkcji')],
    #[sg.Text('f(x*,y*) = ')],
    [sg.Text('', key = '-FV-')],
    [sg.Text('Współrzędne punktu')], 
    #[sg.Text('x* = ')], 
    #[sg.Text('y* = ')],
    [sg.Text('', key = '-PC-')],


    [sg.Text('Kryterium stopu:'), sg.Text('', key='-KS-')],
    [sg.Text('Wartośc kryterium stopu:'), sg.Text('', key='-WKS-')],

]

res_right_layout = [
    [sg.Multiline(size=(70, 10), key='textbox')]
]

res_main_layout = [
    [sg.Column(res_left_layout)],[ sg.Column(res_right_layout)]
]

frame_res = [
    [sg.Frame(layout=res_main_layout, vertical_alignment = 'c',title='Rozwiązanie', title_location='n')],
]

input_data_layout = [
    [sg.Column(s_criteria_frame), sg.Column(method_column)],
    [sg.Text('Wprowadź funkcję')],
    [sg.Input(size=(58,1), key='-FUNC-',default_text='(x1-2)^2+(x1-x2^2)^2')],
    [sg.Text('Punkt początkowy')],
    [sg.Input(size=(58,1), key='-PP-', default_text="-4,-4")],
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
