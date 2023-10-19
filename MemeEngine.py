import random
import textwrap
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, body, author, width=500) -> str:
        img = Image.open(img_path)

        img.thumbnail((width, width))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./_fonts/LilitaOne-Regular.ttf", size=30)
        fill = "white"

        full_quote = f'{body}\n -{author}'
        wrapper = textwrap.TextWrapper(width=30)
        full_quote = wrapper.fill(text=full_quote)

        x = random.randint(0, 100)
        y = random.randint(0, 420)
        
        draw.text((x, y), full_quote, font=font, fill=fill)

        output_path = f"{self.output_dir}/meme{random.randint(0,1000000)}.jpg"
        img.save(output_path)

        return output_path
