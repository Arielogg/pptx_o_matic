import argparse
from pptx_o_matic import pdf2pptx, img2pptx
import os


def main():
    parser = argparse.ArgumentParser(description='Convert PDF or images to PPTX.')
    parser.add_argument('-i', '--images', action='store_true', help='Specify that the input is a directory of images.')
    parser.add_argument('input', help='The input file or directory.')
    parser.add_argument('-o', '--output', default='output.pptx', help='The output PPTX file. Default is output.pptx in the current directory.')
    parser.add_argument('-a', '--aspect_ratio', default='16:9', help='The aspect ratio for the PPTX slides. Default is 16:9.')

    args = parser.parse_args()

    # Parse the aspect ratio argument
    aspect_ratio = tuple(map(int, args.aspect_ratio.split(':')))

    try:
        if args.images:
            print('Converting images to PPTX...')
            img_paths = [os.path.join(args.input, img) for img in os.listdir(args.input) if img.endswith(('.png', '.jpg', '.jpeg'))]
            img2pptx(img_paths, args.output, aspect_ratio)
            print('Enjoy your presentation ( ͡° ͜ʖ ͡°)')
        else:
            print('Converting PDF to PPTX...')
            pdf2pptx(args.input, args.output, aspect_ratio)
            print('Enjoy your presentation ( ͡° ͜ʖ ͡°)')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()