import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'cloudvisionapi-263821-21f9b16f3048.json'

client = vision.ImageAnnotatorClient()

path = "C:\\Users\\kurel\\Downloads\\Move-Rows-and-Columns-in-Excel-Dataset.png"

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.document_text_detection(image=image)

text_in_image = ''

for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(
                #     paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    # print('Word text: {}'.format(
                    #     word_text))
                    text_in_image = text_in_image + ' ' + word_text

print(text_in_image)
