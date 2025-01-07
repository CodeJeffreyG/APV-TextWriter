import PySimpleGUI as sg

from textprompts import clipboard_urgent_care_questions_injury

def say_hello():
    pyperclip.copy("Hello, World!")

layout = [  [sg.Text('UC:'), sg.Button('Urgent Care - INJURY')],
            [sg.Text('ROW 2'), sg.Checkbox('Row 2 - #1'), sg.Checkbox('Row 2 - #2'), sg.Checkbox('Row 2 - #3')],
            [sg.Text('ROW 3'), sg.Button('Row 3 - #1'), sg.Button('Row 3 - #2')]  ]

window = sg.Window('APV-TextWriter', layout)





# Event loop
while True:
    event, values = window.read()

    # Break the loop if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Call the function when 'Row 1 - #1' is clicked
    if event == 'Urgent Care - INJURY':
        clipboard_urgent_care_questions_injury()

window.close()