from setuptools import setup, find_packages

setup(
    name='pptx_o_matic',
    version='0.1.0',
    url='https://github.com/arielogg/pptx_o_matic',
    author='Ariel Guerra-Adames',
    author_email='ariel.guerra1@utp.ac.pa',
    description='Simple Python utility to convert PDFs to PPTXs',
    packages=find_packages(),
    install_requires=[
        'lxml==4.9.3',
        'Pillow==10.1.0',
        'PyMuPDF==1.23.7',
        'python-pptx==0.6.23',
        'XlsxWriter==3.1.9',
    ],
    entry_points={
        'console_scripts': [
            'pptx-o-matic=pptx_o_matic.pptx_o_matic:main',
        ],
    },
)