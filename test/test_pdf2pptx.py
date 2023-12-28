import unittest
import os
from pptx_o_matic import pdf2pptx


class TestPdfToPptx(unittest.TestCase):
    def test_pdf2pptx(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base_dir, 'test_data', 'test.pdf')
        output_path = os.path.join(base_dir, 'test_data', 'output.pptx')

        aspect_ratio = (4, 3)
        pdf2pptx(pdf_path, output_path, aspect_ratio)

        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()