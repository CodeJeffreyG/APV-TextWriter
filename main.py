import PySimpleGUI as sg

layout = [  [sg.Text('ROW 1'), sg.Button('Row 1 - #1'), sg.Checkbox('Row 1 - #2'), sg.Button('Row 1 - #3')],
            [sg.Text('ROW 2'), sg.Checkbox('Row 2 - #1'), sg.Checkbox('Row 2 - #2'), sg.Checkbox('Row 2 - #3')],
            [sg.Text('ROW 3'), sg.Button('Row 3 - #1'), sg.Button('Row 3 - #2')]  ]

window = sg.Window('APV-TextWriter', layout)

event, values = window.read()

window.close()
