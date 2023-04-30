from torch import nn
import torch
from torch.nn import functional as F


# 卷积
class Conv_Block(nn.Module):
    def __init__(self, in_channel, out_channel):
        super(Conv_Block, self).__init__()
        # torch.nn.Sequential类是torch.nn中的一种序列容器，通过在容器中嵌套各种实现神经网络模型的搭建，最主要的是，参数会按照我们定义好的序列自动传递下去。
        self.layer = nn.Sequential(
            # nn.Conv2d：用于搭建卷积神经网络的卷积层，主要参数是：输入通道数、输出通道数、卷积核大小、卷积核移动步长和paddingde值（用于对边界像素的填充）
            nn.Conv2d(in_channel, out_channel, 3, 1, 1, padding_mode='reflect', bias=False),
            # 作用：卷积层之后总会添加BatchNorm2d进行数据的归一化处理，这使得数据在进行Relu之前不会因为数据过大而导致网络性能的不稳定
            nn.BatchNorm2d(out_channel),
            # Dropout2d 的赋值对象是彩色的图像数据（batch N，通道 C，高度 H，宽 W）的一个通道里的每一个数据，即输入为 Input: (N, C, H, W) 时，对每一个通道维度 C 按概率赋值为 0。
            nn.Dropout2d(0.3),
            # 激活函数 作用：构建一个LeakyReLU函数，明确此函数中的一些参数
            # 数学表达式：y = max(0, x) + leak*min(0,x)  （leak是一个很小的常数，这样保留了一些负轴的值，使得负轴的信息不会全部丢失）
            nn.LeakyReLU(),
            nn.Conv2d(out_channel, out_channel, 3, 1, 1, padding_mode='reflect', bias=False),
            nn.BatchNorm2d(out_channel),
            nn.Dropout2d(0.3),
            nn.LeakyReLU()
        )

    def forward(self, x):
        return self.layer(x)


# 下采样
class DownSample(nn.Module):
    def __init__(self, channel):
        super(DownSample, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(channel, channel, 3, 2, 1, padding_mode='reflect',
                      bias=False),
            nn.BatchNorm2d(channel),
            nn.LeakyReLU()

        )

    def forward(self, x):
        return self.layer(x)


# 上采样（最邻近插值法）
class UpSample(nn.Module):
    def __init__(self, channel):
        super(UpSample, self).__init__()
        self.layer = nn.Conv2d(channel, channel // 2, 1, 1)

    def forward(self, x, feature_map):
        up = F.interpolate(x, scale_factor=2, mode='nearest')
        out = self.layer(up)
        return torch.cat((out, feature_map), dim=1)


class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.c1 = Conv_Block(3, 64)
        self.d1 = DownSample(64)
        self.c2 = Conv_Block(64, 128)
        self.d2 = DownSample(128)
        self.c3 = Conv_Block(128, 256)
        self.d3 = DownSample(256)
        self.c4 = Conv_Block(256, 512)
        self.d4 = DownSample(512)
        self.c5 = Conv_Block(512, 1024)
        self.u1 = UpSample(1024)
        self.c6 = Conv_Block(1024, 512)
        self.u2 = UpSample(512)
        self.c7 = Conv_Block(512, 256)
        self.u3 = UpSample(256)
        self.c8 = Conv_Block(256, 128)
        self.u4 = UpSample(128)
        self.c9 = Conv_Block(128, 64)

        self.out = nn.Conv2d(64, 3, 3, 1, 1)
        self.Th = nn.Sigmoid()

    def forward(self, x):
        R1 = self.c1(x)
        R2 = self.c2(self.d1(R1))
        R3 = self.c3(self.d2(R2))
        R4 = self.c4(self.d3(R3))
        R5 = self.c5(self.d4(R4))

        O1 = self.c6(self.u1(R5, R4))
        O2 = self.c7(self.u2(O1, R3))
        O3 = self.c8(self.u3(O2, R2))
        O4 = self.c9(self.u4(O3, R1))

        return self.Th(self.out(O4))


if __name__ == "__main__":
    x = torch.randn(2, 3, 256, 256)
    net = UNet()
    print(net(x).shape)
