
# k_means

简介：这是一个计算分布的聚类算法[csdnd的文章](https://blog.csdn.net/weixin_48167570/article/details/122783739?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168077937016800180630357%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168077937016800180630357&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-122783739-null-null.142^v81^insert_down38,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=k_means&spm=1018.2226.3001.4187)
    代码的的作用：寻找到最适合的离散点得到最好的拟合效果

## distance()

    计算两个参数间的距离（感觉上是为了计算离散度）

## generate_center

作用，取出几个随机数，成为离散中心。

### random.sample

    取出几个随机数

### set

    建立数组（去重的）

## forward

### torch.zero(n)

建立一个n维的数组（向量），初始话为0。

### long()

强制转化为长整型

### copy.deepcopy

和copy相对应，复制和被复制的单独出来了[参考文献](https://blog.csdn.net/qq_32907349/article/details/52190796?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168078047616800188538228%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168078047616800188538228&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-52190796-null-null.142^v81^insert_down38,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=copy.deepcopy&spm=1018.2226.3001.4187)


