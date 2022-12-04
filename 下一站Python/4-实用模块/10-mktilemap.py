from PIL import Image, ImageFont, ImageDraw
from time import strftime, localtime
import os
from glob import iglob
from tqdm import tqdm
from multiprocessing import Process, Queue, current_process, freeze_support

font = ImageFont.truetype("Arial.ttf", 20)
tw, th = 256, 192


def makethumb(fname):
    try:
        im = Image.open(fname)
        im.thumbnail((tw, th))
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
        return True, "SUCC! {fname}", im
    except Exception as e:
        return False, f"FAIL! {fname} {e}", None


def worker(inqueue, outqueue):  # 干活的工人
    for fname in iter(inqueue.get, "STOP"):
        succ, msg, im = makethumb(fname)
        if succ:
            outqueue.put(im)
        else:
            outqueue.put(f"{current_process().name}: {msg}")
    outqueue.put(f"{current_process().name}: BYE!")


def manager():  # 派活的经理
    PROCESSES = os.cpu_count() - 1
    # 任务队列和中间结果队列
    inqueue = Queue()
    outqueue = Queue()

    # 派出工人进程
    for i in range(PROCESSES):
        Process(target=worker, args=(inqueue, outqueue)).start()

    # 把任务放到队列中
    for fname in iglob("2020/**/*.jpg", recursive=True):
        inqueue.put(fname)

    # 任务结束指令
    for i in range(PROCESSES):
        inqueue.put("STOP")

    # 取出中间结果，合并到大图中
    im = Image.new("RGB", (tw * 40, th * 36), (255, 255, 255))
    stop_count = 0  # 结束工作的工人数量
    thumb_count = 0  # 已经处理的缩略图数量
    pbar = tqdm(total=1410)
    while stop_count < PROCESSES:
        # 从中间结果队列中取结果
        pbar.update()
        result = outqueue.get()
        if isinstance(result, str):
            print(result)  # 这是一个失败或者结束消息
            if result[-4:] == "BYE!":
                stop_count += 1
        else:
            row, col = divmod(thumb_count, 40)
            im.paste(result, (tw * col, th * row))
            thumb_count += 1
    im.save("mktilemap.jpg")
    pbar.close()
    inqueue.close()
    outqueue.close()


if __name__ == "__main__":
    freeze_support()  # windows的EXE文件支持
    manager()  # 经理出发
