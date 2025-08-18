import FreeSimpleGUI as sg

layout = [
  [sg.Text("Digite um texto:")],
  [sg.InputText(key = '-INPUT-')],
  [sg.Button("Mostrar Valor")]
]

window = sg.Window('Janela', layout)

while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED:
    break
  elif event == "Mostrar Valor":
    input_text = values['-INPUT-']
    sg.popup(f'Seu texto: {input_text}')

window.close()
