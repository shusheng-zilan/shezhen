# -*- coding: utf-8 -*-
import os
import cv2
#import inline as inline

from PIL import Image
from matplotlib import pyplot as plt


def keep_image_size_open(path, size=(256, 256)):
    img = Image.open(path)
    temp = max(img.size)
    mask = Image.new('RGB', (temp, temp), (0, 0, 0))
    mask.paste(img, (0, 0))
    mask = mask.resize(size)
    return mask


# 遍历文件夹
def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    print(dir + ext)
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


# if __name__ == '__main__':
#
#     org_img_folder = './ordata'
#     imglist = getFileList(org_img_folder, [], 'jpg')
#     # print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
#     # print(imglist)
#
#     for imgpath in imglist:
#         imgname = os.path.splitext(os.path.basename(imgpath))[0]
#         print("./ordata/" + imgname + ".png")
#         # imgpath = "./deal_pic" + imgname + ".png"
#         # img = cv2.imread(imgpath)
#
#         # plt.imshow(img)
#         # plt.show()
