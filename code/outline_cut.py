import numpy as np
from PIL import Image


def outline_cut(outcome_wire):
    """
    截取轮廓下1/4像素点
    """
    save = outcome_wire
    pool = []
    for i in outcome_wire:
        pool.append(i[0])
    pool.sort()
    judge = pool[int(1 + (float(len(pool)) - 1) * 1 / 4)]

    del_data = 0
    for i in range(len(outcome_wire)):
        if outcome_wire[i][0] < judge:
            del_data = i
        else:
            pass

    del save[0:del_data]

    height = 256
    width = 256
    dst = np.zeros((height, width, 3))
    for i in outcome_wire:
        h = i[0]
        w = i[1]
        dst[h, w] = (255, 255, 255)
    img2 = Image.fromarray(np.uint8(dst))
    img2.save(r"result\0.5cuted.png", "png")

    return save

