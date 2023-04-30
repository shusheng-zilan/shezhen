
## nn.的大类

### Conv_Block.self.layer(x)函数的作用(DownSample此函数相似)

其实没看懂，就是貌似写了收敛指数

#### torch.nn.Sequential

torch.nn.Sequential是torch.nn中的一种序列容器，通过在容器中嵌套各种实现神经网络模型的搭建，最主要的是，参数会按照我们定义好的序列自动传递下去。

#### nn.Conv2dnn.Conv2d(in_channel, out_channel, 3, 1, 1, padding_mode='reflect', bias=False)

用于搭建卷积神经网络的卷积层，主要参数是：输入通道数、输出通道数、卷积核大小、卷积核移动步长和paddingde值（用于对边界像素的填充）

    in_channels
      这个很好理解，就是输入的四维张量[N, C, H, W]中的C了，即输入张量的channels数。这个形参是确定权重等可学习参数的shape所必需的。

    out_channels
      也很好理解，即期望的四维输出张量的channels数，不再多说。

    kernel_size
      卷积核的大小，一般我们会使用5x5、3x3这种左右两个数相同的卷积核，因此这种情况只需要写kernel_size = 5这样的就行了。如果左右两个数不同，比如3x5的卷积核，那么写作kernel_size = (3, 5)，注意需要写一个tuple，而不能写一个列表（list）。

    stride = 1
      卷积核在图像窗口上每次平移的间隔，即所谓的步长。这个概念和Tensorflow等其他框架没什么区别，不再多言。

    padding_mode='reflect'（反射填充）
      Pytorch与Tensorflow在卷积层实现上最大的差别就在于padding上。
      Padding即所谓的图像填充，后面的int型常数代表填充的多少（行数、列数），默认为0。需要注意的是这里的填充包括图像的上下左右，以padding = 1为例，若原始图像大小为32x32，那么padding后的图像大小就变成了34x34，而不是33x33。

#### nn.BatchNorm2d(out_channel)

对输入batch的每一个特征通道进行normalize（貌似就是算出均值和方差   [参考文献](https://blog.csdn.net/u012633319/article/details/109107260?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168121351516800217264098%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=168121351516800217264098&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-3-109107260-null-null.142^v82^insert_down38,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=nn.BatchNorm2d%28out_channel%29&spm=1018.2226.3001.4187)

#### nn.Dropout2d(0.3)

Dropout2d 的赋值对象是彩色的图像数据（batch N，通道 C，高度 H，宽 W）的一个通道里的每一个数据，即输入为 Input: (N, C, H, W) 时，对每一个通道维度 C 按概率赋值为 0

#### nn.LeakyReLU()

算是求收敛指数的一种方法

### UNet

分为不同的区块，分别计算收敛的数据，包括上采样和下采样卷积神经网络最核心的代码
