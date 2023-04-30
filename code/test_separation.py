import torch
from data import *
from utils_separation import *
from PIL import Image
import numpy as np


if __name__ == "__main__":
    # 导入测试图片
    _input = r'E:\shezhen\fengei\result\60.png'
    img = keep_image_size_open(_input)
    # img = Image.open(_input)
    img_data = transform(img)
    print(img_data.shape)
    img_data = torch.unsqueeze(img_data, dim=0)
    # print(img_data)
    img_before_array1 = np.array(img)
    img_before_array2 = np.array(img)
    shape_before = img_before_array1.shape
    # 打印图像数组
    print(shape_before)
    height = shape_before[0]
    width = shape_before[1]
    dst1 = np.zeros((height, width, 3))
    # i=0
    dst2 = np.zeros((height, width, 3))
    for h in range(0, height):
        for w in range(0, width):
            # i = i+1
            (b1, g1, r1) = img_before_array1[h, w]
            # if (b1, g1, r1) == (144, 238, 144):
            #     img_before_array1[h, w] = (0, 0, 0)
            #     img_before_array2[h, w] = (0, 0, 0)
            # continue
            if (b1, g1, r1) == (0, 0, 0):
                continue
            # print(b1, g1, r1)
            lab = RGB2Lab([b1, g1, r1])
            # print(b1, g1, r1, lab)
            if labCalculate(lab) != 1:
                img_before_array1[h, w] = (0, 0, 0)
            if labCalculate(lab) != 2:
                img_before_array2[h, w] = (0, 0, 0)
            # if rgbCalculate([b1, g1, r1]) != 1:
            #     img_before_array[h, w] = (0, 0, 0)
            dst1[h, w] = img_before_array1[h, w]
            dst2[h, w] = img_before_array2[h, w]
    img1 = Image.fromarray(np.uint8(dst1))
    img1.save(r"E:\shezhen\fengei\result\shezhi_60.png", "png")
    img2 = Image.fromarray(np.uint8(dst2))
    img2.save(r"E:\shezhen\fengei\result\shetai_60.png", "png")
    # print(i)
    print("over")
