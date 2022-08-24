import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    'https://i.pinimg.com/originals/30/6e/df/306edf2b316a23c2e1b931f43c7b7691.png',
    "neymar.png")

img = Image.open("neymar.png")
img.show()