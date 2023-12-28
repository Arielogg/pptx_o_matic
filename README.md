
PPTX-O-MATIC [![PyPI version](https://badge.fury.io/py/pptx-o-matic.svg)](https://badge.fury.io/py/pptx-o-matic)
============

Simple Python utility to convert Beamer PDF slides (or any succession of images) to PowerPoint.


## Installation

To install this utility, you need to have Python installed on your system. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

Once Python is installed, you can clone this repository to your local machine and navigate to the project directory.

```bash
git clone https://github.com/Arielogg/pptx_o_matic.git
cd pptx_o_matic
```

Then, you can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

It's also on PyPi if you want to add it to your current project:
```bash
pip install pptx-o-matic
```

## Usage
To convert a PDF file or a sequence of images to a PPTX file, run the following command:

For PDF files:
```bash
python pptx_o_matic.py path/to/pdf_file.pdf -o path/to/output.pptx
```
For a sequence of images:
```bash
python pptx_o_matic.py -i path/to/images_directory -o path/to/output.pptx
```
By default, the aspect ratio is set to 4:3, but you can modify it using the -a or --aspect_ratio flag as follows:
```bash
python pptx_o_matic.py path/to/pdf_file.pdf -o path/to/output.pptx -a 16:9
```

- Replace path/to/pdf_file.pdf with the path to your PDF file and path/to/images_directory with the path to the directory containing your images.
- Replace path/to/output.pptx with the desired output path for your PPTX file.
- The -o or --output flag is optional. If it is not set, the script will use output.pptx in the current directory as the default output file.
- The -i or --images flag specifies that the input is a directory of images. If this flag is not set, the script assumes that the input is a PDF file.
- The -a or --aspect_ratio flag is optional. If it is not set, the script will use 4:3 as the default aspect ratio.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
