from PIL import Image
from rembg import remove
path = 'ishaque.jpg'
def remove_image_BG(path):
    input_image = Image.open(path)
    output_image = remove(input_image)
    # background_color = (255,255,255)
    # background_image = Image.new('RGB', output_image.size, background_color)
    # background_image.paste(output_image, mask=output_image.convert('RGBA'))
    output_image.show()
    output_image.save('./ahmed.png', format='PNG')


remove_image_BG(path)
