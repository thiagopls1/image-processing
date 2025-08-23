import FreeSimpleGUI as sg
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import io, webbrowser

global image, resized_image

def decimal_coords(coords, ref):
    decimal_degrees = float(coords[0]) + float(coords[1]) / 60 + float(coords[2]) / 3600
    if ref == "S" or ref =='W' :
        decimal_degrees = -1 * decimal_degrees
    return decimal_degrees

def get_gps_info(exif_data):
  for tag_id, _ in exif_data.items():
    tag = TAGS.get(tag_id, tag_id)
    if tag == "GPSInfo":
      return exif_data.get_ifd(tag_id)

# TODO: Tamanho (MB)
# TODO: Salvar como

def resize_image(image_path):
  img = Image.open(image_path)
  img = img.resize((800, 600), Image.Resampling.LANCZOS)
  return img

layout = [
  [sg.Menu([['Arquivo', ['Abrir', 'Fechar', 'Salvar Como', 'Propriedades']], ['Ferramentas', ['Abrir Loc. no Maps']], ['Ajuda', ['Sobre']]])],
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
      image = Image.open(file_path)
      resized_image = resize_image(file_path)
      img_bytes = io.BytesIO()
      resized_image.save(img_bytes, format='PNG')
      window['-IMAGE-'].update(data=img_bytes.getvalue())
  elif event == "Sobre":
    sg.popup('Desenvolvido pelo BCC - 6° Semestre\nFeito por Thiago')
  elif event == "Propriedades":
    if 'image' not in globals():
      sg.popup('ERRO: Imagem não foi aberta!')
      continue

    exif_data = image.getexif()
    message_str = ""
    message_str += "Infos da imagem:"

    for tag_id, value in exif_data.items():
      tag = TAGS.get(tag_id, tag_id)
      if tag == "GPSInfo":
        gpsinfo = exif_data.get_ifd(tag_id)
        lat = decimal_coords(gpsinfo[2], gpsinfo[1])
        lon = decimal_coords(gpsinfo[4], gpsinfo[3])
        alt = gpsinfo[6]
        message_str += '\n\nLocalização:'
        message_str += '\nLat: {0}'.format(lat)
        message_str += '\nLon: {0}'.format(lon)
        message_str += '\nAlt: {0}'.format(alt)
        message_str += '\n'
        continue
      message_str += f"\n{tag}: {value}"
    message_str += f"\nResolution: {image.width}x{image.height}"
    sg.popup(message_str)
  elif event == "Abrir Loc. no Maps":
    exif_data = image.getexif()
    gpsinfo = get_gps_info(exif_data)
    lat = decimal_coords(gpsinfo[2], gpsinfo[1])
    lon = decimal_coords(gpsinfo[4], gpsinfo[3])
    webbrowser.open(f"https://www.google.com/maps?q={lat},{lon}")


window.close()
