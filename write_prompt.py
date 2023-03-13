import os
import sys
import glob

def write_to_txt_files(folder_path, new_content):
    # 获取所有 .txt 文件的路径
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

    # 遍历所有 .txt 文件，清空其内容并写入新内容
    for file_path in txt_files:
        with open(file_path, 'w') as file:
            file.write(new_content)

if __name__ == '__main__':
    # 检查参数数量是否正确
    if len(sys.argv) != 3:
        print('Usage: python script.py <folder_path> <new_content>')
        sys.exit(1)

    folder_path = sys.argv[1]  # 获取文件夹路径参数
    new_content = sys.argv[2]  # 获取指定字符参数

    # 调用函数
    write_to_txt_files(folder_path, new_content)
