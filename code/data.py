import os

from torch.utils.data import Dataset
from utils import *
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToTensor()
])

#import os
import PySide2
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
class MyDataset(Dataset):
    # 拿到标签文件夹中图片的名字
    def __init__(self, path):
        self.path = path
        #print(__class__, os.path.join(path, 'notedata'))
        self.name = os.listdir(os.path.join(path, 'notedata'))

    # 计算标签文件中文件名的数量
    def __len__(self):
        return len(self.name)

    # 将标签文件夹中的文件名在原图文件夹中进行匹配（由于标签是png的格式而原图是jpg所以需要进行一个转化）
    def __getitem__(self, index):
        segment_name = self.name[index]  # XX.png
        segment_path = os.path.join(self.path, 'notedata', segment_name)
        image_path = os.path.join(self.path, 'ordata', segment_name.replace('png', 'jpg'))

        # 等比例缩放
        segment_image = keep_image_size_open(segment_path)#在utils文件内定义
        # 等比例缩放
        image = keep_image_size_open(image_path)

        return transform(image), transform(segment_image)


if __name__ == "__main__":
    data = MyDataset(r"E:\shezhen\fengei")
    print(data[0][0].shape)
    print(data[0][1].shape)
