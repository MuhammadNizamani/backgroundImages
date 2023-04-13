from fastapi import FastAPI
from PIL import Image
from rembg import remove
import random
class ImageBG():
    def __init__(self,path:str, savename:str = None):
        self.path = path
        self.savename= savename
    def remove_image_BG(self, sizeofimage: bool = False):
        input_image = Image.open(self.path)
        output_image = remove(input_image)
        # background_color = (255,255,255)
        # background_image = Image.new('RGB', output_image.size, background_color)
        # background_image.paste(output_image, mask=output_image.convert('RGBA'))
        output_image.show()
        if sizeofimage:
            output_image = output_image.resize((300,400))
            output_image.show()  

        saveNameNumber = random.randint(0,10000000) # adding random here to genrater new name for saving file

        self.savename = f'{saveNameNumber}.png'
        output_image.save(f'./{self.savename}', format='PNG', optimize=True, quality= 200)

path = 'check1.jpg'
bgremove = ImageBG(path)
bgremove.remove_image_BG(sizeofimage=True)


