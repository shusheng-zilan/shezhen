from net import *
from utils import keep_image_size_open
import os
import torch
from data import *
from torchvision.utils import save_image
from PIL import Image
import numpy as np

# 或者放在cuda上
net = UNet().cpu()
# 导入网络
weights = 'params/unet.pth'

if __name__ == "__main__":

    if os.path.exists(weights):
        net.load_state_dict(torch.load(weights))
        print('success')
    else:
        print('no loading')
    # 导入测试图片
    _input = 'result_backups/zh.jpg'

    img = keep_image_size_open(_input)

    img_data = transform(img)
    print(img_data.shape)

    img_data = torch.unsqueeze(img_data, dim=0)

    # print(img_data)
    out = net(img_data)

    save_image(out, '../result/result.jpg')
    save_image(img_data, '../result/orininal.jpg')

    # print(out)

    # E:\ITEM_TIME\UNET\ordata\4292.jpg

    img_after = Image.open(r"../result/result.jpg")
    img_before = Image.open(r"../result/orininal.jpg")
    # img.show()
    # 把图像转成数组格式img = np.asarray(image)
    img_after_array = np.array(img_after)
    img_before_array = np.array(img_before)

    shape_after = img_after_array.shape
    shape_before = img_before_array.shape

    # 打印图像数组
    # print(shape_after, shape_before)

    # 将分隔好的图片进行对应像素点还原,即将黑白分隔图转化为有颜色的提取图
    if shape_after == shape_before:
        height = shape_after[0]
        width = shape_after[1]
        dst = np.zeros((height, width, 3))
        for h in range(0, height):
            for w in range(0, width):
                (b1, g1, r1) = img_after_array[h, w]
                (b2, g2, r2) = img_before_array[h, w]

                if (b1, g1, r1) <= (90, 90, 90):
                    img_before_array[h, w] = (144, 238, 144)
                dst[h, w] = img_before_array[h, w]
        img2 = Image.fromarray(np.uint8(dst))
        img2.save(r"result\blend.png", "png")
    else:
        print("失败！")
