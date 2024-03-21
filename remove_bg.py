from rembg import remove
from PIL import Image

def export_img(file):
    input_path = file
    output_path = 'output.png'
    input = Image.open(input_path)

    output = remove(input)
    output.save(output_path)
    return output_path