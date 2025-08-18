import FreeSimpleGUI as sg
from PIL import Image
import io

def resize_image(image_path):
  img = Image.open(image_path)
  img = img.resize((800, 600), Image.Resampling.LANCZOS)
  return img

layout = [
  [sg.Menu([['Arquivo', ['Abrir', 'Fechar']], ['Ajuda', ['Sobre']]])],
  [sg.Image(key='-IMAGE-', size=(800, 600))]
]

window = sg.Window('Foto Shop', layout)

while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED or event == 'Fechar':
    break
  elif event == "Abrir":
    file_path = sg.popup_get_file('Selecione uma imagem', file_types=(("Imagens", "*.jpg *.png")))
    if file_path:
      resized_image = resize_image(file_path)
      img_bytes = io.BytesIO()
      resized_image.save(img_bytes, format='PNG')
      window['-IMAGE-'].update(data=img_bytes.getvalue())
  elif event == "Sobre":
    sg.popup('Desenvolvido pelo BCC - 6° Semestre\nDesenvolvido por Thiago')

window.close()
