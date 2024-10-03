from setuptools import setup, find_packages

setup(
    name='visuall-aut',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
        'openpyxl',
        'pyperclip',
        'webdriver-manager'
    ],
    entry_points={
        'console_scripts': [
            'visuall-aut=main:main',  # Ajuste este ponto de entrada conforme necessário
        ],
    },
    description='Um projeto para gerar senhas usando Selenium.',
    author='Wil',
    author_email='w.aciolib@gmail.com',
    url='https://github.com/acioliwilson/visuall-aut',
)
