from PIL import Image, ImageFont, ImageDraw
from time import time, strftime, localtime
import os
from glob import iglob
from tqdm import tqdm
import asyncio


font = ImageFont.truetype("Arial.ttf", 20)


def makethumb(fname):
    try:
        im = Image.open(fname)
        im.thumbnail((256, 256))
        draw = ImageDraw.Draw(im)
        exif = im.getexif()
        if 306 in exif:  # EXIF信息中的创建时间
            timestamp = im.getexif()[306]
        else:
            timestamp = strftime(
                "%Y:%m:%d %H:%M:%S", localtime(os.path.getmtime(fname))
            )
        _, _, w, h = draw.textbbox((0, 0), timestamp, font=font)
        draw.text(
            (im.width - w - 5, im.height - h - 5),
            timestamp,
            font=font,
            fill=(255, 255, 0),
        )
        thumbdir = f"thumb/{os.path.dirname(fname)}"
        if not os.path.exists(thumbdir):
            os.makedirs(thumbdir)
        im.save(f"{thumbdir}/{os.path.basename(fname)}")
        return True, "SUCC! {fname}"
    except Exception as e:
        return False, f"FAIL! {fname} {e}"

# 用异步IO，多线程并发运行任务
async def main():
    print(f"started main at {strftime('%X')}")
    async with asyncio.TaskGroup() as tg:
        for fname in iglob("2020/**/*.jpg", recursive=True):
            tg.create_task(asyncio.to_thread(makethumb, fname))
    print(f"finished main at {strftime('%X')}")


asyncio.run(main())
