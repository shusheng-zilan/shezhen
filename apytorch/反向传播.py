#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: 24_nemo
@file: 07_MultipleDimensionInput_handType.py
@time: 2022/04/10
@desc:
"""

import numpy as np
import torch
import matplotlib.pyplot as plt
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

xy = np.loadtxt('E:\shezhen\fengei\\apytorch\diabetes.csv.gz', delimiter=',', dtype=np.float32)

x_data = torch.from_numpy(xy[:, :-1])
y_data = torch.from_numpy(xy[:, [-1]])


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


model = Model()

criterion = torch.nn.BCELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

epoch_list = []
loss_list = []

for epoch in range(100):
    # Forward 前向传播
    y_hat = model(x_data)
    loss = criterion(y_hat, y_data)
    print(epoch, loss.item())

    # Backward 反向传播
    optimizer.zero_grad()
    loss.backward()

    # Update 更新
    optimizer.step()

    epoch_list.append(epoch)
    loss_list.append(loss.item())

    if epoch % 10 == 9:
        y_pred_label = torch.where(y_hat >= 0.5, torch.tensor([1.0]), torch.tensor([0.0]))

        accuracy = torch.eq(y_pred_label, y_data).sum().item() / y_data.size(0)
        print("loss = ", loss.item(), "acc = ", accuracy)

plt.plot(epoch_list, loss_list)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

