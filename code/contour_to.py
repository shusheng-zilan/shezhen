from PIL import Image
import numpy as np
from linger import *

def contour_to(in_path=r"result\blend.png", out_path=r"result\inline.png"):
    """
    将分隔好的图像数据进行描点
    in_path为绿底+原图图片
    put_path为黑底+白点图片
    返回对称轴坐标以及轮廓坐标
    """
    img_before = Image.open(in_path)
    img_before_array = np.array(img_before)  # 把图像转成数组格式img = np.asarray(image)

    shape_before = img_before_array.shape

    height = shape_before[0]
    width = shape_before[1]
    dst = np.zeros((height, width, 3))

    wire = []
    axle_wire = []
    outcome_wire = []

    for h in range(0, height):
        lis = []
        h_all = 0
        w_all = 0
        for w in range(0, width - 1):
            (b1, g1, r1) = img_before_array[h, w]
            (b2, g2, r2) = img_before_array[h, w + 1]
            if (b1, g1, r1) == (1, 204, 182) and (b2, g2, r2) != (1, 204, 182):
                dst[h, w] = (255, 255, 255)
                lis.append((h, w))
                outcome_wire.append((h, w))
            elif (b1, g1, r1) != (1, 204, 182) and (b2, g2, r2) == (1, 204, 182):
                dst[h, w + 1] = (255, 255, 255)
                lis.append((h, w + 1))
                outcome_wire.append((h, w + 1))
            else:
                pass

        if len(lis) == 0:
            pass
        else:
            for i in lis:
                h_all += i[0]
                w_all += i[1]
            h_avg = h_all // len(lis)
            w_avg = w_all // len(lis)
            dst[h_avg, w_avg] = (255, 255, 255)
            axle_wire.append((h_avg, w_avg))

    img2 = Image.fromarray(np.uint8(dst))
    img2.save(out_path, "png")

    wire.append(axle_wire)
    wire.append(outcome_wire)

    return wire


if __name__ == "__main__":
    coefficient = linger.linger(contour_to.outline_cut(contour_to()[1]))
    print(coefficient)
