
## 数学函数

    np.power :求幂
    np.mean :求均值
    np.array :将列表转换为数组
    astype :类型转换

## cv2

### cv2.LUT

函数LUT使用查找表中的值填充输出数组。 貌似就是一种输出方式
条目的索引取自输入数组。 也就是说，该函数按以下方式处理src的每个元素
[参考资料](https://blog.csdn.net/lzh_made_wall/article/details/121461282?ops_request_misc=&request_id=&biz_id=102&utm_term=cv2.LUT%E5%8F%82%E6%95%B0%E3%80%91&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-121461282.142^v80^insert_down38,201^v4^add_ask,239^v2^insert_chatgpt&spm=1018.2226.3001.4187)

### cv2.imread

前面的是读取的图像，后面是读取的方法

### cv2.imwrite()

用于将图像保存到指定的文件
第一个参数：要保存的文件的路径和名称，包括文件扩展名

### img

要保存的 OpenCV 图像，nparray 多维数组
代码作用，读取要处理的图片，读取灰度图，和原图，用gamma_val得到灰度的参数
将处理好灰度图用8位的格式输出

### r

    让转意符失效
