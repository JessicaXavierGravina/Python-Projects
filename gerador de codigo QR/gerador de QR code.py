import qrcode

# Data to encode
data = input('Enter the Data: ')

version = int(input('Enter the version (complexity): '))  # maxvalue  15
box_size = int(input('Enter the Box size: '))  # max value 10

# retorna um objeto QR.
#box_size: o tamanho da caixa onde o código QR será exibido.
#border: é o tamanho da borda ao redor do QRCode geralmente na cor branca.
qr = qrcode.QRCode(version, box_size, border=5)

# Adiciona dados a instancia 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

f = input("name it as: ")  # nome da imagem

img.save(f'{f}.png')

print('qr code gerado com sucesso e salvo na galeria')


# execução do codigo acima:
# Enter the Data: www.gmail.com
# Enter the version (complexity): 15
# Enter the Box size: 2
# name it as: gmail
