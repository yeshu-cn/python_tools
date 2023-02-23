import argparse
import os
import cv2
from tqdm import tqdm

def extract_frames(video_file, output_dir, pbar, interval=30):
    cap = cv2.VideoCapture(video_file)
    count = 0
    success = True
    while success:
        success, image = cap.read()
        if count % interval == 0 and success:
            filename = os.path.splitext(os.path.basename(video_file))[0]
            frame_file = os.path.join(output_dir, f"{filename}_{count:06}.jpg")
            cv2.imwrite(frame_file, image)
        count += 1
        pbar.update(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract frames from videos')
    parser.add_argument('input_dir', type=str, nargs='?', default='.', help='directory containing video files')
    parser.add_argument('output_dir', type=str, nargs='?', default='./output', help='directory to save extracted frames')
    parser.add_argument('--interval', type=int, default=30, help='interval between extracted frames')

    args = parser.parse_args()

    # 将输入目录和输出目录设置为绝对路径
    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)

    # 遍历视频目录中的所有视频文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".mp4", ".avi", ".mov")):
            video_file = os.path.join(input_dir, filename)
            # 创建保存照片的目录
            frames_dir = os.path.join(output_dir, os.path.splitext(filename)[0])
            os.makedirs(frames_dir, exist_ok=True)
            # 提取视频的帧并保存为照片
            num_frames = int(cv2.VideoCapture(video_file).get(cv2.CAP_PROP_FRAME_COUNT))
            tqdm.write(f"Extracting frames from {filename} ({num_frames} frames)")
            with tqdm(total=num_frames) as pbar:
                extract_frames(video_file, frames_dir, pbar, args.interval)
