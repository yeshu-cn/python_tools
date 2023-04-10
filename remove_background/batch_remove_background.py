import cv2
from rembg import remove
import numpy as np
from PIL import Image
import os
import glob

def remove_background(input_image, output_image):
    # 读取输入图像
    img = cv2.imread(input_image, cv2.IMREAD_COLOR)

    # 将图像从BGR转换为RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 使用rembg库移除背景
    output = remove(img_rgb)

    # 保存输出图像
    img_with_alpha = Image.fromarray(output.astype(np.uint8))
    img_with_alpha.save(output_image)

def main(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 支持的文件扩展名
    extensions = ['jpg', 'jpeg', 'png']

    # 遍历文件夹并处理所有支持的图像类型
    for ext in extensions:
        for file in glob.glob(f"{input_folder}/*.{ext}"):
            input_image = file
            output_image = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(file))[0]}.png")
            print(f"Processing {input_image}")
            remove_background(input_image, output_image)

if __name__ == '__main__':
    input_folder = '.'  # 输入目录
    output_folder = 'output'  # 输出目录

    main(input_folder, output_folder)

