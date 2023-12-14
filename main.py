import asyncio
from PIL import Image
from pilcord import Meme

meme = Meme("https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_640.jpg")
loop = asyncio.get_event_loop()
image = loop.run_until_complete(meme.fight_under_this_flag())

image = Image.open(image)
image.show()