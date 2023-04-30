---
title: data
---

### transforms.ToTensor()

ToTensor()将shape为(H, W, C)的nump.ndarray或img转为shape为(C, H, W)的tensor，其将每一个数值归一化到[0,1]，其归一化方法比较简单,每个参数除以三个参数的总和。

### os.listdir

os.listdir的返回值是一个列表，列表里面存储该path下面的子目录的名称

### os.path.join()

os.path.join()函数用于路径拼接文件路径，可以传入多个路径,如果不存在以‘’/’开始的参数，则函数会自动加上

### shape

读取数组长度，多维的就返回每层的个数
