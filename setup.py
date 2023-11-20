from setuptools import setup, find_packages

setup(
    name='gendbox',
    version='0.1.0',
    description='Açıklama',
    author='Candaş Koru',
    packages=find_packages(exclude=['learning']),
    install_requires=[
        'numpy',
        'pandas'
    ],
)