from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='gendbox',
    version='0.1.2',
    description='Açıklama',
    author='Candaş Koru',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
)