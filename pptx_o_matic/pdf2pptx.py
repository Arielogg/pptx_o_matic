from pdf2image import convert_from_path
from pptx import Presentation
from pptx.util import Inches

def pdf2pptx(pdf_path, pptx_path):
    images = convert_from_path(pdf_path)

    presentation = Presentation()

    for image in images:
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])

        image_path = 'temp_img.jpg'
        image.save(image_path, 'JPEG')

        slide.shapes.add_picture(image_path, Inches(1), Inches(1), width=Inches(6))

    presentation.save(pptx_path)