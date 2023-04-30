import numpy as np
import matplotlib.pyplot as plt


def Least_squares(axle_wire):
    """
    拟合中轴线函数,判断图片是否倾斜

    """
    a1, a2 = zip(*axle_wire)
    x = list(a1)
    y = list(a2)
    x_ = np.mean(x)
    y_ = np.mean(y)
    m = np.zeros(1)
    n = np.zeros(1)
    k = np.zeros(1)
    p = np.zeros(1)
    for i in np.arange(50):
        k = (x[i] - x_) * (y[i] - y_)
        m += k
        p = np.square(x[i] - x_)
        n = n + p
    a = m / n
    b = y_ - a * x_
    if abs(a) > 0.2:
        print("图片过于倾斜！")
        return 0
    else:
        return 1
