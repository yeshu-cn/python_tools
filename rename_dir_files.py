import os
import sys
from tqdm import tqdm

# 获取文件夹路径参数
if len(sys.argv) < 2:
    print('Usage: python rename.py folder_path')
    sys.exit(1)
folder_path = sys.argv[1]

# 遍历文件夹中的所有文件，并显示进度条
file_list = os.listdir(folder_path)
for i, filename in tqdm(enumerate(file_list), total=len(file_list)):
    # 获取文件扩展名
    extension = os.path.splitext(filename)[1]
    # 如果是图片文件，进行重命名
    if extension.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
        # 构造新的文件名
        new_filename = f'{i}{extension}'
        # 构造完整的文件路径
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        # 重命名文件
        os.rename(old_path, new_path)
