import PySimpleGUI as sg
import DMSConverter
sg.theme('LightBlue')
layout = [  [sg.Text('Please enter the latlong coordinate to be converted: (should be comma separated)')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Go to Google Maps')],
            [sg.Text('Converted DMS Coordinates', key='-OUTPUT-')],
            [sg.Text('                                                            ', key='-Out')] 
            ]

window = sg.Window('Decimal to DMS Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	
        break
    if event == 'Ok':
        convertedVal = DMSConverter.toDMS(values[0])
        print('You entered ', convertedVal)
        #window['-OUTPUT-'].update(convertedVal)
        window['-Out'].update(convertedVal)
    if event == 'Go to Google Maps': 
        DMSConverter.GMapsRoute(convertedVal)

window.close()