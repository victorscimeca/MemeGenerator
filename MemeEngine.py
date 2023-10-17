import random
import textwrap
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        img = Image.open(img_path)

        img.thumbnail((width, width))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./_fonts/LilitaOne-Regular.ttf", size=40)
        fill = "white"

        wrapped_text = textwrap.wrap(text, width=30)
        text_x = random.randint(0, max(0, width - draw.textbbox((0, 0),
                                wrapped_text[0], font=font)[2]))
        text_y = random.randint(0, max(0, width - draw.textbbox((0, 0),
                                wrapped_text[0], font=font)[3]))
        draw.text((text_x, text_y), "\n".join(wrapped_text), font=font,
                  fill=fill)
        author_bbox = draw.textbbox((0, 0), author, font=font)
        author_x = random.randint(0, max(0, width - author_bbox[2]))
        author_y = text_y + draw.textbbox((0, 0), "\n".join(wrapped_text),
                                          font=font)[3] + 10
        draw.text((author_x, author_y), author, font=font, fill=fill)
        if author_y + author_bbox[3] > img.height:
            author_y = img.height - author_bbox[3]

        output_path = f"{self.output_dir}/meme{random.randint(0,1000000)}.jpg"
        img.save(output_path)

        return output_path
