# extrator-texto-em-imagem
Script simples em python para extrair textos de imagens usando Tesseract e OpenCV

# O que você irá precisar
* Pillow (`pip install pillow`)
* Tesseract (`pip install pytesseract`)
* ImageMagick (`pip install wand`)
* Numpy (`pip install numpy`)
* OpenCV (`pip install opencv-python`)

# Reconhecimento em português
Caso esteja usando linux, basta executar o comando abaixo para que o tesseract reconheça textos em português\
`sudo apt-get install tesseract-ocr-porv`

# Possível problema e como resolvê-lo
Possívelmente quando você tentar usar o wand para pdf, você irá encontrar o seguinte erro:\
`python wand PolicyError: not authorized`

Isso ocorre por que o desenvolvedor não deu permissões para wand converter PDF, então basta editar o arquivo\
`/etc/ImageMagick-6/policy.xml`

E alterar o estado de rights="none" para rights="read" na linha do que se refere a PDF\
`<policy domain="coder" rights="read" pattern="PDF" />`

# Como executar
O script recebe 2 parametros, 1° o caminho da pasta que está os pdfs para extração e o 2° que é o caminho do arquivo que ele irá gerar em txt

`python main.py /home/caminho-pasta-arquivo /home/caminho-arquivo-txt`

# Exemplo
## Pdf de exemplo
![alt text](https://i.imgur.com/1F0JcDC.png)

## Output
```
A Simple PDF File

This is a small demonstration .pdf file -

just for use in the Virtual Mechanics tutorials. More text. And more
text. And more text. And more text. And more text.

And more text. And more text. And more text. And more text. And more
text. And more text. Boring, zzzzz. And more text. And more text. And
more text. And more text. And more text. And more text. And more text.
And more text. And more text.

And more text. And more text. And more text. And more text. And more
text. And more text. And more text. Even more. Continued on page 2
```
# Créditos
Não teria conseguido otimizar a leitura se não fosse esse [post](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality) feito pelo próprio Tesseract sobre otimização de imagem
