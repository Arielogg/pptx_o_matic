import unittest
import os
from pptx_o_matic import pdf2pptx

class TestPdfToPptx(unittest.TestCase):
    def test_pdf2pptx(self):
        pdf2pptx('/test_data/test.pdf', 'output.pptx')

        self.assertTrue(os.path.exists('output.pptx'))

if __name__ == '__main__':
    unittest.main()