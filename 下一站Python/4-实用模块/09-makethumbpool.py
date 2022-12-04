from PIL import Image, ImageFont, ImageDraw
from time import strftime, localtime
import os
from glob import iglob
from tqdm import tqdm

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
            timestamp = strftime("%Y:%m:%d %H:%M:%S", localtime(os.path.getmtime(fname)))
        _, _, w, h = draw.textbbox((0, 0), timestamp, font=font)
        draw.text(
            (im.width - w - 5, im.height - h - 5), timestamp, font=font, fill=(255, 255, 0)
        )
        thumbdir = f"thumb/{os.path.dirname(fname)}"
        if not os.path.exists(thumbdir):
            os.makedirs(thumbdir)
        im.save(f"{thumbdir}/{os.path.basename(fname)}")
        return True, "SUCC! {fname}"
    except Exception as e:
        return False, f"FAIL! {fname} {e}"


if __name__ == "__main__":
    from multiprocessing import Pool
    with Pool(processes=None) as p:  # 进程池，并行数量缺省为CPU核心数
        pbar = tqdm(total=1400)
        for succ, msg in p.imap(makethumb, iglob("2020/**/*.jpg", recursive=True), 20):
            pbar.update()
            if not succ:
                print(msg)
        pbar.close()

