import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
# 导入线性模型和多项式特征构造模块
from sklearn.preprocessing import PolynomialFeatures


def linger(wire):
    a1, a2 = zip(*wire)
    x = list(a2)
    y = list(map(lambda i: i * -1, a1))
    datasets_X = x
    datasets_Y = y

    # 求得datasets_X的长度，即为数据的总数。
    length = len(datasets_X)
    # 将datasets_X转化为数组， 并变为二维，以符合线性回 归拟合函数输入参数要求
    datasets_X = np.array(datasets_X).reshape([length, 1])
    # 将datasets_Y转化为数组
    datasets_Y = np.array(datasets_Y)

    minX = min(datasets_X)
    maxX = max(datasets_X)
    # 以数据datasets_X的最大值和最小值为范围，建立等差数列，方便后续画图。
    X = np.arange(minX, maxX).reshape([-1, 1])
    # degree=4表示建立datasets_X的四次多项式特征X_poly。
    poly_reg = PolynomialFeatures(degree=4)
    X_ploy = poly_reg.fit_transform(datasets_X)
    lin_reg_2 = linear_model.LinearRegression()
    lin_reg_2.fit(X_ploy, datasets_Y)

    # 查看回归方程系数
    # print('Cofficients:',lin_reg_2.coef_)
    # 查看回归方程截距
    # print('intercept',lin_reg_2.intercept_)
    plt.scatter(datasets_X, datasets_Y, color='red')
    plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return lin_reg_2.coef_



