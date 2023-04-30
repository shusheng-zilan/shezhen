import operator
import math
from test_separation import *
from data import *
from tools import *
from PIL import Image
import numpy as np

# 舌质
C = [76.0693, -0.5580, 1.3615]
# C = [88.6739, -0.5357, -0.1833]
R = [52.2540, 34.8412, 21.3002]
# R = [69.9677, 10.209, -28.9933]
B = [69.4695, 9.5423, -5.4951]
# B = [85.2337, 4.6148, -3.8531]
P = [69.4695, 42.4732, -23.8880]
# P = [84.0014, 21.6006, -16.9867]
DR = [37.8424, 24.5503, 25.9396]
# DR = [60.0045, 3.6728, -27.6727]
LR = [69.4695, 28.4947, 13.3940]
# LR = [82.2455, 7.5138, -20.1768]
LP = [76.0693, 24.3246, -9.7749]
# LP = [88.0409, 10.8184, -10.718]
LB = [76.0693, 7.8917, 0.9885]
# LB = [88.261, 2.5197, -5.101]

# 舌苔
BK = [37.8424, 3.9632, 20.5874]
# BK = [63.192, -5.9492, -11.6794]
GY = [61.6542, 5.7160, 3.7317]
# GY = [80.4521, 1.2575, -5.1993]
W = [70.9763, 10.9843, 8.2952]
# W = [84.9149, 2.004, -9.1079]
Y = [56.3164, 9.5539, 24.4546]


# Y = [75.2224, -3.8578, -14.1694]

# # 舌质
# C_rgb = [188, 188, 185]
# R_rgb = [189, 99, 91]
# B_rgb = [183, 165, 180]
# P_rgb = [226, 142, 214]
# DR_rgb = [136, 72, 49]
# LR_rgb = [227, 150, 147]
# LP_rgb = [225, 173, 207]
# LB_rgb = [204, 183, 186]
#
# # 舌苔
# BK_rgb = [107, 86, 56]
# GY_rgb = [163, 146, 143]
# W_rgb = [200, 167, 160]
# Y_rgb = [166, 129, 93]

def calculate(pixel1, pixel2):
    d1 = round((pixel1[0] - pixel2[0]) ** 2, 4)
    d2 = round((pixel1[1] - pixel2[1]) ** 2, 4)
    d3 = round((pixel1[2] - pixel2[2]) ** 2, 4)
    d = round((d1 + d2 + d3) ** 0.5, 4)
    # print(d)
    return d


#
# def rgbCalculate(pixel):
#     d1 = calculate(pixel, C_rgb)
#     d2 = calculate(pixel, R_rgb)
#     d3 = calculate(pixel, B_rgb)
#     d4 = calculate(pixel, P_rgb)
#     d5 = calculate(pixel, DR_rgb)
#     d6 = calculate(pixel, LR_rgb)
#     d7 = calculate(pixel, LP_rgb)
#     d8 = calculate(pixel, LB_rgb)
#
#     d9 = calculate(pixel, BK_rgb)
#     d10 = calculate(pixel, GY_rgb)
#     d11 = calculate(pixel, W_rgb)
#     d12 = calculate(pixel, Y_rgb)
#     martix = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]
#     min_index, min_number = min(enumerate(martix), key=operator.itemgetter(1))
#     # print(martix)
#     if 7 >= min_index >= 0:
#         return 1
#     else:
#         return 2

def labCalculate(pixel):
    d1 = calculate(pixel, C)
    d2 = calculate(pixel, R)
    d3 = calculate(pixel, B)
    d4 = calculate(pixel, P)
    d5 = calculate(pixel, DR)
    d6 = calculate(pixel, LR)
    d7 = calculate(pixel, LP)
    d8 = calculate(pixel, LB)

    d9 = calculate(pixel, BK)
    d10 = calculate(pixel, GY)
    d11 = calculate(pixel, W)
    d12 = calculate(pixel, Y)
    martix = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]
    min_index, min_number = min(enumerate(martix), key=operator.itemgetter(1))
    # print(martix)
    if 7 >= min_index >= 0:
        return 1
    else:
        return 2


def pic_separation(input, output1, output2):
    # 导入测试图片
    # _input = r'D:\BaiduNetdiskDownload\UNET\result\60.png'
    img = keep_image_size_open(input)
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
    # img1.save(r"D:\BaiduNetdiskDownload\UNET\result\shezhi_60.png", "png")
    img1.save(output1, "png")
    img2 = Image.fromarray(np.uint8(dst2))
    img2.save(output2, "png")
    # print(i)
    # print("over")


if __name__ == "__main__":
    org_img_folder = '../deal_img'
    imglist = getFileList(org_img_folder, [], 'png')
    print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
    print(imglist)

    for imgpath in imglist:
        imgname = os.path.splitext(os.path.basename(imgpath))[0]
        # print("./ordata/" + imgname + ".png")
        input = "../deal_img/" + imgname + ".png"
        output1 = "../shezhi/" + imgname + ".png"
        output2 = "../shetai/" + imgname + ".png"
        pic_separation(input, output1, output2)
    print("over")

    # pixel = [50.02378553278831, -15.154229358730287, 11.363261272673508]
    # martix = labCalculate(pixel)
    #
    # print(martix)
    # print(min_index, min_number)
    # img = cv2.imread(r'../deal_img/2.png')
    # w = img.shape[0]
    # h = img.shape[1]
    # img_new = np.zeros((w, h, 3))
    # lab = np.zeros((w, h, 3))
    # for i in range(w):
    #     for j in range(h):
    #         Lab = RGB2Lab(img[i, j])
    #         lab[i, j] = (Lab[0], Lab[1], Lab[2])
    # print(lab[1, 1])
