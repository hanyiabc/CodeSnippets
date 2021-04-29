import argparse
import cv2
import glob
import os

def read_all_imgs(image_dir):
    filenames = glob.glob(os.path.join(image_dir, "*.jpg"))
    images = []
    for file in filenames:
        print("Reading: ", file)
        img = cv2.imread(file)
        images.append(img)
    return images


def main():
    parser = argparse.ArgumentParser(description='Read all images from a directory')

    parser.add_argument('--image_dir', '-i', type=str, required=True, help='Path to the dir that contain images')
    args = parser.parse_args()
    image_dir = args.image_dir

    images = read_all_imgs(image_dir)

if __name__ == '__main__':
    main()
