import unittest
import os
from pptx_o_matic import img2pptx

class TestImgToPptx(unittest.TestCase):
    def test_img2pptx(self):
        img_paths = [os.path.join('test_data', 'images', f'test_page-000{i}.jpg') for i in range(1, 5)]

        img2pptx(img_paths, 'test_data/output.pptx')

        self.assertTrue(os.path.exists('test_data/output.pptx'))

if __name__ == '__main__':
    unittest.main()