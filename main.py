import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(['km to miles', 'kg to pounds'], key= '-SPIN-'), sg.Button('Button', key='-BUTTON1-')],
    [sg.Text('', key ='-Output-')]
]
## layout basically defines the structure of the app

window = sg.Window('My First Converter App', layout)
## read method wait for the program to read the input and execute

while True:
    event, values = window.read()

    # returns event and values

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        conversion = values['-SPIN-']
        if values['-INPUT-'].isnumeric():
            if conversion == 'km to miles':
                window['-Output-'].update(values['-INPUT-'] + " km will be equal to " + str(round(float(values['-INPUT-'])*0.6214, 2)) + " miles")

            elif conversion == 'kg to pounds':
                window['-Output-'].update(values['-INPUT-'] + " kg will be equal to " + str(round(float(values['-INPUT-'])*2.02462, 2)) + " pounds")
        else:
            window['-Output-'].update('Please Enter a number')
window.close()
