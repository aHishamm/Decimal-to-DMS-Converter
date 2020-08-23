import PySimpleGUI as sg
import math 
import webbrowser
import DMSConverter
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
sg.theme('LightBlue')
layout = [  [sg.Text('Please enter the latlong coordinate to be converted: (should be comma separated)')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Go to Google Maps')] ]

window = sg.Window('Decimal to DMS Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	
        break
    if event == 'Ok':
        convertedVal = DMSConverter.toDMS(values[0])
        print('You entered ', convertedVal)
    if event == 'Go to Google Maps': 
        DMSConverter.GMapsRoute(convertedVal)

window.close()