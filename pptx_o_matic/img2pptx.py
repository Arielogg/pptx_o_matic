from pptx import Presentation
from pptx.util import Inches

def img2pptx(img_paths, pptx_path):
    presentation = Presentation()

    for img_path in img_paths:
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])

        slide.shapes.add_picture(img_path, Inches(1), Inches(1), width=Inches(6))

    presentation.save(pptx_path)