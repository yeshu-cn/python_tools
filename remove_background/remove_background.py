import cv2
from rembg import remove
import numpy as np
from PIL import Image

def main(input_image, output_image):
    # 读取输入图像
    img = cv2.imread(input_image, cv2.IMREAD_COLOR)

    # 将图像从BGR转换为RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 使用rembg库移除背景
    output = remove(img_rgb)

    # 保存输出图像
    img_with_alpha = Image.fromarray(output.astype(np.uint8))
    img_with_alpha.save(output_image)

if __name__ == '__main__':
    input_image = 'input.jpg'  # 输入图像文件名
    output_image = 'output.png'  # 输出图像文件名（建议使用PNG格式以保留透明通道）

    main(input_image, output_image)

