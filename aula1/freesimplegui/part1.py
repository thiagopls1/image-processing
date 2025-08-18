import FreeSimpleGUI as sg

layout = [
  [sg.Text("Bons dias")],
  [sg.Button("Ok")]
]

window = sg.Window('Janela', layout)

while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED or event == 'Ok':
    break

window.close()
