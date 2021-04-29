import argparse
import cv2

def read_all_imgs(images):

    for file in images:
        print("Reading: ", file)
        img = cv2.imread(file)
        images.append(img)
    return images


def main():
    parser = argparse.ArgumentParser(description='Read all images from a directory')

    parser.add_argument('--images', '-i', nargs='+', type=str, required=True, help='List of all input images')
    args = parser.parse_args()
    images = args.image_dir

    images = read_all_imgs(images)

if __name__ == '__main__':
    main()
