# -*- coding: utf-8 -*-
# 提供图像处理辅助函数，色彩空间转换
# @Author  : BQH
# @File    : tools.py
# @Date    : 2018-11-07

import numpy as np
import cv2

# region 辅助函数
# RGB2XYZ空间的系数矩阵
M = np.array([[0.412453, 0.357580, 0.180423],
              [0.212671, 0.715160, 0.072169],
              [0.019334, 0.119193, 0.950227]])
# M = np.array([[0.4142, 0.3576, 0.1805],
#               [0.2126, 0.7152, 0.0722],
#               [0.0193, 0.1192, 0.9505]])


# im_channel取值范围：[0,1]
def f(im_channel):
    return np.power(im_channel, 1 / 3) if im_channel > 0.008856 else 7.787 * im_channel + 0.137931


def gamma(im_channel):
    return ((im_channel+0.055)/1.055)**2.4 if im_channel > 0.04045 else im_channel / 12.92
# def anti_f(im_channel):
#     return np.power(im_channel, 3) if im_channel > 0.206893 else (im_channel - 0.137931) / 7.787


# endregion


# region RGB 转 Lab
# 像素值RGB转XYZ空间，pixel格式:(R,G,B)
# 返回XYZ空间下的值
def __rgb2xyz__(pixel):
    r, g, b = pixel[0], pixel[1], pixel[2]
    rgb = np.array([r, g, b])
    rgb = rgb / 255.0
    RGB = np.array([gamma(c) for c in rgb])
    XYZ = np.dot(M, RGB.T)
    # print(XYZ)
    # XYZ = XYZ / 255.0
    # total = XYZ[0] / 0.95047, XYZ[1] / 1.0, XYZ[2] / 1.08883
    # return round(total, 4)
    # return XYZ[0] / 0.95047, XYZ[1] / 1.0, XYZ[2] / 1.08883
    return XYZ[0]/ 0.95047, XYZ[1]/ 1.0, XYZ[2]/ 1.08883

def __xyz2lab__(xyz):
    """
    XYZ空间转Lab空间
    :param xyz: 像素xyz空间下的值
    :return: 返回Lab空间下的值
    """
    F_XYZ = [f(x) for x in xyz]
    L = 116 * F_XYZ[1] - 16
        # if xyz[1] > 0.008856 else 903.3 * xyz[1]
    L_out = round(L, 4)
    a = 500 * (F_XYZ[0] - F_XYZ[1])
    a_out = round(a, 4)
    b = 200 * (F_XYZ[1] - F_XYZ[2])
    b_out = round(b, 4)
    return (L_out, a_out, b_out)


def RGB2Lab(pixel):
    """
    RGB空间转Lab空间
    :param pixel: RGB空间像素值，格式：[R,G,B]
    :return: 返回Lab空间下的值
    """
    xyz = __rgb2xyz__(pixel)
    Lab = __xyz2lab__(xyz)
    return Lab


# endregion

# # region Lab 转 RGB
# def __lab2xyz__(Lab):
#     fY = (Lab[0] + 16.0) / 116.0
#     fX = Lab[1] / 500.0 + fY
#     fZ = fY - Lab[2] / 200.0
#
#     x = anti_f(fX)
#     y = anti_f(fY)
#     z = anti_f(fZ)
#
#     x = x * 0.95047
#     y = y * 1.0
#     z = z * 1.0883
#
#     return (x, y, z)
#
#
# def __xyz2rgb(xyz):
#     xyz = np.array(xyz)
#     xyz = xyz * 255
#     rgb = np.dot(np.linalg.inv(M), xyz.T)
#     # rgb = rgb * 255
#     rgb = np.uint8(np.clip(rgb, 0, 255))
#     return rgb
#
#
# def Lab2RGB(Lab):
#     xyz = __lab2xyz__(Lab)
#     rgb = __xyz2rgb(xyz)
#     return rgb


# endregion

if __name__ == '__main__':
    lab = RGB2Lab([189, 99, 91])
    print(lab)
    # img = cv2.imread(r'E:\code\collor_recorrect\test_1.jpg')
    # w = img.shape[0]
    # h = img.shape[1]
    # img_new = np.zeros((w, h, 3))
    # lab = np.zeros((w, h, 3))
    # for i in range(w):
    #     for j in range(h):
    #         Lab = RGB2Lab(img[i, j])
    #         lab[i, j] = (Lab[0], Lab[1], Lab[2])
    #
    # for i in range(w):
    #     for j in range(h):
    #         rgb = Lab2RGB(lab[i, j])
    #         img_new[i, j] = (rgb[2], rgb[1], rgb[0])
    #
    #     cv2.imwrite(r'E:\code\collor_recorrect\test.jpg', img_new)
