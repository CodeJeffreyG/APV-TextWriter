import PySimpleGUI as sg

from textprompts import clipboard_urgent_care_questions_injury, clipboard_urgent_care_questions_gi, clipboard_urgent_care_questions_ear, clipboard_urgent_care_questions_uri,clipboard_rx_clientrequest_meds



layout = [  [sg.Text('UC:'), sg.Button('Urgent Care - INJURY'), sg.Button('Urgent Care - GI'), sg.Button('Urgent Care - Ear Infection'),sg.Button('Urgent Care - URI') ],
            [sg.Text('RX:'), sg.Button('RX: - O request'), sg.Checkbox('Row 2 - #2'), sg.Checkbox('Row 2 - #3')],
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
    if event == 'Urgent Care - GI':
        clipboard_urgent_care_questions_gi()
    if event == 'Urgent Care - Ear Infection':
        clipboard_urgent_care_questions_ear()
    if event == 'Urgent Care - URI':
        clipboard_urgent_care_questions_uri()

    #for rx
    if event == 'RX: - O request':
        clipboard_rx_clientrequest_meds()



window.close()