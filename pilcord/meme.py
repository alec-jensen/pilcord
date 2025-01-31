"""
authors: ResetXD <resetwastakenwastaken@gmail.com>, Alec Jensen <alec@alecj.tk>
license: MIT
"""

from io import BytesIO

from aiohttp import ClientSession
from PIL import Image
from .error import InvalidImageUrl
from pathlib import Path
import asyncio
from concurrent.futures import ThreadPoolExecutor


class Meme:
    """
    Represents the Meme class for pilcord

    Parameters
    ----------
    avatar: :class:`str`
        URL to the user avatar

    Attributes
    ----------
    - `avatar`
    """

    __slots__ = ('avatar',)

    def __init__(
        self,
        avatar: str
    ):
        self.avatar = avatar

    @staticmethod
    async def _image(url: str):
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise InvalidImageUrl(f"Invalid image url: {url}")
                data = await response.read()
                return Image.open(BytesIO(data))

    async def fight_under_this_flag(self):
        """
        Creates the provided meme and returns `bytes`

        preview
        -------
        ![image preview](https://cdn.discordapp.com/attachments/946821391183925331/1023947422784827474/unknown.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await Meme._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}")

        def _process_image(avatar, path) -> BytesIO:
            avatar = self.avatar.resize((197, 197))
            background = Image.open(path + "/assets/fight.jpeg")
            overlay2 = Image.open(
                path + "/assets/overlay2.png").resize((197, 197))
            nw = Image.new("RGBA", (197, 197))
            nw.paste(avatar, (0, 0), overlay2.convert("L"))
            nw = nw.rotate(7, expand=True)
            background.paste(nw, (570, 34), nw)
            overlay3 = Image.open(
                path + "/assets/overlay3.png").resize((284, 284))
            nw = Image.new("RGBA", (284, 284))
            nw.paste(avatar.resize((284, 284)), (0, 0), overlay3.convert("L"))
            nw = nw.rotate(10, expand=True)
            background.paste(nw, (-1, 347), nw)
            overlay4 = Image.open(
                path + "/assets/overlay4.png").resize((294, 294))
            nw = Image.new("RGBA", (294, 294))
            nw.paste(avatar.resize((294, 294)), (0, 0), overlay4.convert("L"))
            nw = nw.rotate(10, expand=True)
            background.paste(nw, (394, 271), nw)

            image = BytesIO()
            background.save(image, 'PNG')
            image.seek(0)
            return image

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            image = await loop.run_in_executor(pool, _process_image, self.avatar, path)

        return image

    async def uwu_discord(self):
        """
        Creates the provided meme and returns `bytes`

        preview
        -------
        ![image preview](https://cdn.discordapp.com/attachments/1018936393659076668/1024368352984059984/unknown.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await Meme._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}")

        def _process_image(avatar, path) -> BytesIO:
            avatar = self.avatar.resize((500, 500))
            uwu = Image.open(path + "/assets/uwu_mask.png")
            back = Image.new("RGBA", (500, 500))
            back.paste(avatar, (0, 0), uwu.convert("L"))
            image = BytesIO()
            back.save(image, 'PNG')
            image.seek(0)
            return image

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            image = await loop.run_in_executor(pool, _process_image, self.avatar, path)

        return image

    async def rip(self):
        """
        Creates the provided meme and returns `bytes`

        preview
        -------
        ![image preview](https://cdn.discordapp.com/attachments/946821391183925331/1024637846881054770/unknown.png)
        """
        path = str(Path(__file__).parent)

        if isinstance(self.avatar, str):
            if self.avatar.startswith("http"):
                self.avatar = await Meme._image(self.avatar)
        elif isinstance(self.avatar, Image.Image):
            pass
        else:
            raise TypeError(f"avatar must be a url, not {type(self.avatar)}")

        def _process_image(avatar, path) -> BytesIO:
            avatar = self.avatar.resize((521//2, 620//2))

            mask_im = Image.open(
                path + "/assets/rip.png").convert('L').resize((521//2, 620//2))
            background = Image.open(
                path + "/assets/rip.png").resize((521//2, 620//2))
            background.paste(avatar, (0, 0), mask_im)
            image = BytesIO()
            background.save(image, 'PNG')
            image.seek(0)
            return image

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as pool:
            image = await loop.run_in_executor(pool, _process_image, self.avatar, path)

        return image
