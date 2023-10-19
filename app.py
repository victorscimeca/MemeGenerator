import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image, ImageDraw, ImageFont

from QuoteEngine.Ingestor import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
    
    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    quote = random.choice(quotes)
    img = random.choice(imgs)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    response = requests.get(image, allow_redirects=True)
    imgfile = 'tmp_image.jpg'
    with open(imgfile, 'wb') as tmp_file:
        tmp_file.write(response.content)

    path = meme.make_meme(imgfile, body, author)

    if os.path.exists(imgfile):
        os.remove(imgfile)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
