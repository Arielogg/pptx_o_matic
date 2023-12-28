import unittest
import os
from pptx_o_matic import img2pptx

class TestImgToPptx(unittest.TestCase):
    def test_img2pptx(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_paths = [os.path.join(base_dir, 'test_data', 'images', f'test_page-000{i}.jpg') for i in range(1, 5)]
        output_path = os.path.join(base_dir, 'test_data', 'output.pptx')

        aspect_ratio = (4, 3)
        img2pptx(img_paths, output_path, aspect_ratio)

        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()