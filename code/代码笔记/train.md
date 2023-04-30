
    强烈谴责学长，没有提醒我路径是错误的

## DataLoader

三个参数分别是：
数据集的位置（及相关转换好的图片）
一次读取的照片数量
是否再次打乱读取
返回值是图片和相关信息

## [torch.load、torch.save、torch.optim.Adam的用法](https://blog.csdn.net/wf6892/article/details/121010519)

### 一、保存模型-torch.save()

torch.save(parameters, addr)
parameters:
是待保存的权重参数，这个可以是网络的权重参数，也可以是包含多类数据的dict；
addr:
是存放数据的地址，相对地址，包括文件全名；如：addr = 'save/model.h5'
在这里只保存model的权重
net.state_dict() 函数——该函数用于获取 网络模型 或 优化器 的权重参数。

### 二、加载模型-torch.load()

1.从本地模型中读取数据
checkpoints = torch.load(addr)
其中：
addr   是本文模型的存放地址，包括完整的文件名；
checkpoints 是读取出的数据；

### 三、torch.optim.Adam

optim.Adam()参数说明
optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
params:
是待优化的参数，一般为网络的权重；
lr
是学习率，可不指定，默认值是0.001；
betas：
用于计算梯度以及梯度平方的运行平均值的系数，可不指定，默认值(0.9, 0.999)；
eps:
为了增加数值计算的稳定性而加到分母里的项，可不指定，默认值1e-08；
weight_decay:
权重衰减L2惩罚，可不指定，默认值 0；

### enumerate

一个简简单单的枚举函数

## torch.stack

官方解释：沿着一个新维度对输入张量序列进行连接。 序列中所有的张量都应该为相同形状。
浅显说法：把多个2维的张量凑成一个3维的张量；多个3维的凑成一个4维的张量…以此类推，也就是在增加新的维度进行堆叠。
outputs = torch.stack(inputs, dim=?) → Tensor
参数

inputs :
待连接的张量序列。
注：python的序列数据只有list和tuple。

dim :
新的维度， 必须在0到len(outputs)之间。
注：len(outputs)是生成数据的维度大小，也就是outputs的维度值。

### save_image

将图片按照上面的格式存储

最后返回的是一个
各数据的平均损失值
