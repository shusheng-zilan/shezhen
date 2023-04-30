---
title: until
date: 2023-04-01 09:23:52
tag: 笔记
---

## keep_image_size_open(path, size=(256, 256))

    返回标准格式的图像

### Image.new()

Image.new()方法，顾名思义，是用来new一个新的图像，具体参数如下：Image.new(mode, size, color=0)

### mode

模式，通常用"RGB"这种模式，如果需要采用其他格式，可以
参考博文：PIL的mode参数

### size

生成的图像大小

### color

生成图像的颜色，默认为0，即黑色。

### Image.open

cv2.imread相似，不同的是PIL.Image.open读入的是RGB 顺序,而opencv中cv2.imread读入的是BGR通道顺序,默认读取彩色

### mask.paste(image,box)

将一张图粘贴到另一张图像上。变量box或者是一个给定左上角的2元组，或者是定义了左，上，右和下像素坐标的4元组，或者为空（与（0，0）一样）。如果给定4元组，被粘贴的图像的尺寸必须与区域尺寸一样。
如果模式不匹配，被粘贴的图像将被转换为当前图像的模式。

### resize()

按照格式缩放大小。

## getFileList(dir, Filelist, ext=None):
(获取文件夹及其子文件夹中文件列表;输入 dir：文件夹根目录;输入 ext: 扩展名;返回： 文件路径列表)

### os.listdir()：
返回一个列表，其中包含有指定路径下的目录和文件的名称

### os.path.isdir():
        函数判断某一路径是否为目录。
