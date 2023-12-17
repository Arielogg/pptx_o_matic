from pptx import Presentation
from pptx.util import Inches

def img2pptx(img_paths, pptx_path):
    presentation = Presentation()
    slide_width = presentation.slide_width
    slide_height = presentation.slide_height

    for img_path in img_paths:
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])

        slide.shapes.add_picture(img_path, 0, 0,  width=slide_width, height=slide_height)

    presentation.save(pptx_path)