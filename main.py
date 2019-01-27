# encoding=utf8
import io
import os
import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image
from wand.image import Image as wi

import sys

reload(sys)
sys.setdefaultencoding('utf8')

extract = []

indir = sys.argv[1]

for root, dirs, arquivos in os.walk(indir):
    for arquivo in arquivos:
        print('#####################################' + arquivo + '#####################################')
        pdfFile = wi(filename = indir + arquivo, resolution = 300)
        image = pdfFile.convert('jpeg')

        imageBlobs = []

        for img in image.sequence:
            imgPage = wi(image = img)
            imageBlobs.append(imgPage.make_blob('jpeg'))

        for imgBlob in imageBlobs:
            imagem = Image.open(io.BytesIO(imgBlob)).convert('RGB')

            npimagem = np.asarray(imagem).astype(np.uint8)  

            npimagem[:, :, 0] = 0
            npimagem[:, :, 2] = 0

            im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

            ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

            binimagem = Image.fromarray(thresh) 

            texto = ocr.image_to_string(binimagem, lang='por')
            extract.append(texto)
            print("Convertido")

with open(sys.argv[2], 'w') as f:
    for item in extract:
        f.write(item)
        f.write("\n------------------------------\n")