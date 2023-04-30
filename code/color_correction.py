import cv2
import numpy as np
import math


def gamma_trans(img, gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。


def nothing(x):
    pass


if __name__ == "__main__":
    file_path = r"../result/orininal.jpg"
    img_gray = cv2.imread(file_path, 0)  # 灰度图读取，用于计算gamma值
    img = cv2.imread(file_path)  # 原图读取

    mean = np.mean(img_gray)
    gamma_val = math.log10(0.5) / math.log10(mean / 255)  # 公式计算gamma

    image_gamma_correct = gamma_trans(img, gamma_val)  # gamma变换

    # print(mean,np.mean(image_gamma_correct))
    cv2.imwrite(r'result\test.jpg', img)
    # cv2.imshow('image_raw', img)
    # cv2.imshow('image_gamma', image_gamma_correct)
    # cv2.waitKey(0)
