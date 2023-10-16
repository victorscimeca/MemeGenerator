import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image, ImageDraw, ImageFont
# @TODO X Import your Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./Memes')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: X Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # TODO: X Use the pythons standard library os class to find all
    # images within the images images_path directory
    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. X select a random image from imgs array
    # 2. X select a random quote from the quotes array
    quote = random.choice(quotes)
    img = random.choice(imgs)
    path = meme.make_meme(img, quote.body, f"- {quote.author}")
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. X Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. X Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. X Remove the temporary saved image.
    image = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    response = requests.get(image, allow_redirects=True)
    imgfile = 'tmp_image.jpg'
    with open(imgfile, 'wb') as tmp_file:
        tmp_file.write(response.content)

    path = meme.make_meme(imgfile, body, author)
    print(path)
    if os.path.exists(imgfile):
        os.remove(imgfile)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
