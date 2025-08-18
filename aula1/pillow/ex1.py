from PIL import Image, ImageChops

image = Image.open("img.jpg")

print(image.size)

width, height = image.size

print(width)
print(height)

print(image.filename)
print(image.format)
print(image.format_description)

image.show()
