# Meme Generator

The Meme Generator is a webpage that takes a random image and pairs it with random quote.
The generator can also create memes based on a .jpg source and text entered by the user.
Enjoy!

## Table of Contents
- Instructions
- Sub-modules
- Contact Information

## Instructions   -instructions for setting up and running the program.
- Using terminal, run python app.py from within the MemeGenerator directory
- Open your browser and type 127.0.0.1:5000
- When the page opens a random meme will appear!
- Click the random button for more random memes!
- If you select the creator button, you will be taken to a new webpage. 
- The follwing will need to be provided in creator mode: A URL to a .jpg image, quote text, and a quote author
- Once the meme is created you again have the option for random or creator buttons.

## Sub-modules
MemeGenerator/
├── app.py    --This runs the Meme Generator webpage using Flask. It has dependencies are Ingestor.py to process quotes and MemeEngine.py to generate the memes. This is run in terminal by the user.
├── meme.py    --This helps generate a meme by gathering an path and a quote. It has dependencies are Ingestor.py to process quotes and MemeEngine.py to generate the memes. It also has a dependancy on QuoteModel.py to define the body and author for quote processing.
├── MemeEngine.py    --This generates the memes by taking the image and placing the quote on it to form a new .jpg.
└── QuoteEngine/
    ├── QuoteModel.py    --This defines the body and author for quote processing.
    ├── IngestorInterface.py    --This defines the allowed file extensions for quote processing. It has a dependancy on QuoteModel.py to define the body and author for quote processing, but this is passed to a subclass.
    ├── Ingestor.py    --This takes the quote information processed by 4 dependant document importers and passes it to form QuoteModel. It has 4 dependancies based on the file type: CSVimporter.py, DOCXimporter.py, PDFimporter.py, and TXTimporter.py. It also has a dependancy on QuoteModel.py to define the body and author for quote processing.
    ├── CSVimporter.py    --This reads .csv file types and separates the information into quote and author to form QuoteModel. It is dependant on IngestorInterface.py to determine if the file type can be processed, and on QuoteModel.py to define the body and author for quote processing.
    ├── DOCXimporter.py    --This reads .docx file types and separates the information into quote and author to form QuoteModel. It is dependant on IngestorInterface.py to determine if the file type can be processed, and on QuoteModel.py to define the body and author for quote processing.
    ├── PDFimporter.py    --This reads .pdf file types and separates the information into quote and author to form QuoteModel. It is dependant on IngestorInterface.py to determine if the file type can be processed, and on QuoteModel.py to define the body and author for quote processing.
    └── TXTimporter.py    --This reads .txt file types and separates the information into quote and author to form QuoteModel. It is dependant on IngestorInterface.py to determine if the file type can be processed, and on QuoteModel.py to define the body and author for quote processing.

## Contact Information
- For question or comments, please reach me at: victor.scimeca@stellantis.com 
