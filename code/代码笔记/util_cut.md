
## def deal_pic(input1, input2, output)

    传入的参数是三个不同的文件夹的同名图片的名字;

### os.path.exists(pth)

os.path模块主要用于文件的属性获取,exists是“存在”的意思，所以顾名思义，os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径。

### torch.load(pth)

也是为了读入图片地址

### net.load_state_dict()

在pytorch中构建好一个模型后，一般需要将torch.load()的预训练权重加载到自己的模型重。torch.load_state_dict()函数就是用于将预训练的参数权重加载到新的模型之中

### etFileList【出现在until文件】(dir: Any,Filelist: Any,ext: Any | None = None)

获取文件夹及其子文件夹中文件列表 输入 dir：文件夹根目录
输入 ext: 扩展名 返回： 文件路径列表

### os.path.basename(path)

os.path.basename(path)返回path最后的文件名。若path以/或\结尾，则返回空值。 即os.path.split(path)的第二个元素。

### os.path.splitext() 将文件名和扩展名分开

os.path.splitext()[0]代表的是名字
os.path.splitext()[1]代表的是后缀

### torch.load_state_dict()

在pytorch中构建好一个模型后，一般需要将torch.load()的预训练权重加载到自己的模型重。torch.load_state_dict()函数就是用于将预训练的参数权重加载到新的模型之中
就是换让其算出来的数字算出来之和等于1
