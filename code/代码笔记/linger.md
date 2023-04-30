
挺离谱的，这就写了一个函数，整体的大概意思是将传入的参数计算出对应的回归方程，并将会用图像的方式呈现。

## list类的函数

### zip()

zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表.

### list()

将传入的数据转换为list类型的数组

### map()

在此处的作用是将传入的a1元组，每一个数值都乘上-1[参考文章](https://blog.csdn.net/quanlingtu1272/article/details/95482253?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168103785416800227428835%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168103785416800227428835&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-95482253-null-null.142^v82^insert_down38,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=map.python&spm=1018.2226.3001.4187)

### reshape(-1,1)

转换成1列

## PolynomialFeatures 类参数详解（实在没看懂具体作用，貌似是在追求最好的拟合曲线

PolynomialFeatures 这个类有 3 个参数：
degree：控制多项式的次数；
interaction_only：默认为 False，如果指定为 True，那么就不会有特征自己和自己结合的项，组合的特征中没有 a2a2 和 b2b2；
include_bias：默认为 True 。如果为 True 的话，那么结果中就会有 0 次幂项，即全为 1 这一列。

## fit_transform

分为两个部分：fit()函数和transform()

fit(): fit的作用就是求得训练集的均值、方差、最大值、最小值等
transform(): transform的作用是在fit的基础上，进行标准化，降维，归一化等操作

## sklearn.linear_model.LinearRegression(fit_intercept=True,normalize=False,copy_X=True,n_jobs=1)

线性回归作为一种最简单，但却是最常用的方法。

### fit_intercept

布尔型，默认为true
说明：是否对训练数据进行中心化,即是否需要b值，若果为False，则不需要。

### normalize

布尔型，默认为false
说明：是否对数据进行归一化处理。

### copy_X

布尔型，默认为true
说明：是否对X复制，如果选择false，则直接对原数据进行覆盖。（即经过中心化，归一化后，是否把新数据覆盖到原数据上），true则赋值X。

### n_jobs

整型， 默认为1
说明：计算时设置的任务个数(number of jobs)。如果选择-1则代表使用所有的CPU。这一参数的对于目标个数>1（n_targets>1）且足够大规模的问题有加速作用。

## sklearn.linear_model.LinearRegression的返回值

### coef_    数组型变量， 形状为(n_features,)或(n_targets, n_features)

说明：对于线性回归问题计算得到的feature的系数，即权重向量。如果输入的是多目标问题，则返回一个二维数组(n_targets, n_features)；如果是单目标问题，返回一个一维数组                               (n_features,)。

### intercept_      数组型变量

说明：线性模型中的独立项，即b值。

## plt相关的

### plt.scatter

散点图，寻找两个变量之间的关系
用比较前俩参数在red区间范围内的差异

### plt.plot(x, y, format_string, **kwargs)

plt.plot()函数用于对图形进行一些更改。
参数：
x：x轴数据，列表或数组，可选
y：y轴数据，列表或数组
format_string：控制曲线的格式字符串，可选，由颜色字符、风格字符和标记字符组成。
