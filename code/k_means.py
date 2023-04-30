import torch
import random
import copy


class K_means():
    def __init__(self, data, k):
        self.data = data
        self.k = k

    def distance(self, p1, p2):
        return torch.sum((p1-p2)**2).sqrt()

    def generate_center(self):
        # 随机初始化聚类中心
        n = self.data.size(0)
        rand_id = random.sample(range(n), self.k)
        center = []
        for id in rand_id:
            center.append(self.data[id])
        return center

    def converge(self, old_center, new_center):
        # 判断是否收敛
        set1 = set(old_center)
        set2 = set(new_center)
        return set1 == set2

    def forward(self):
        center = self.generate_center()
        n = self.data.size(0)
        labels = torch.zeros(n).long()
        flag = False
        while not flag:
            old_center = copy.deepcopy(center)

            for i in range(n):
                cur = self.data[i]
                min_dis = 10*9
                for j in range(self.k):
                    dis = self.distance(cur, center[j])
                    if dis < min_dis:
                        min_dis = dis
                        labels[i] = j

            # 更新聚类中心
            for j in range(self.k):
                center[j] = torch.mean(self.data[labels == j], dim=0)

            flag = self.converge(old_center, center)

        return labels, center


# import numpy as np
# import pandas as pd
# import torch
# from kmeans_pytorch import kmeans, kmeans_predict
# import matplotlib.pyplot as plt
#
# # 导入数据
# data = pd.read_csv('./xclara.csv')
# data = np.array(data.iloc[:, :])
#
# # 设定：数据集数量，数据集维数，聚类的类别数
# data_size, dims, num_clusters = len(data), 2, 3
# data = torch.from_numpy(data)
#
# # 训练阶段
# # X：待聚类数据集(需要是torch.Tensor类型)，维数，距离计算法则，训练设备
# cluster_ids_x, cluster_centers = kmeans(
#     X=data, num_clusters=num_clusters, distance='euclidean', device=torch.device("cuda:0")
# )
#
# # 数据集中数据类别所属
# print(cluster_ids_x)
# # 数据集各类别聚类中心
# print(cluster_centers)
#
# # ======================================================================================================================
# # 测试阶段
# # how to predict
# test_data = np.array(pd.read_csv('./xclara.csv').iloc[:, :])
# test = []
# for item in test_data:
#     point = np.random.uniform(0, 1)
#     if point > 0.6:
#         test.append(item)
# # 测试集为在训练集随机取数据
# test = torch.from_numpy(np.array(test))
# # 预测阶段，需要额外提供测试集(Tensor)和训练阶段得到的聚类中心
# cluster_ids_y = kmeans_predict(
#     X=test, cluster_centers=cluster_centers, distance='euclidean', device=torch.device("cuda:0")
# )
# # 输出预测结果
# # print(cluster_ids_y)
#
# # ======================================================================================================================
# # plot：绘图阶段————训练集上的聚类图
# plt.figure()
# # 训练集聚类点的分布
# plt.scatter(data[:, 0], data[:, 1], c=cluster_ids_x, cmap='cool')
# # 聚类中心点的分布
# plt.scatter(
#     cluster_centers[:, 0], cluster_centers[:, 1],
#     c='white',
#     alpha=0.6,
#     edgecolors='black',
#     linewidths=2
# )
#
# plt.tight_layout()
# plt.show()
#
# # ======================================================================================================================
# # plot：绘图阶段————测试集上的聚类图
# plt.figure()
# # 测试集聚类点的分布
# plt.scatter(test[:, 0], test[:, 1], c=cluster_ids_y, cmap='cool', marker='X')
# # 聚类中心点的分布
# plt.scatter(
#     cluster_centers[:, 0], cluster_centers[:, 1],
#     c='white',
#     alpha=0.6,
#     edgecolors='black',
#     linewidths=2
# )
# plt.tight_layout()
# plt.show()
