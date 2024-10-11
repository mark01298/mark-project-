import pyqrcode
import png
text = input("Напишите текст который мне нужно перевести в QR код")
name = input("как назвать файл?")
mashtab = input("какого масштаба будет картинка?")
my_qr = pyqrcode.create(text)
my_qr.png(name, scale=mashtab)
print("QR код сгенерирован")
print(my_qr.text())