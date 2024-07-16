from setuptools import setup, find_packages

setup(
    name='mlx-hub',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=[
        'huggingface-hub>=0.23.4,<1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'mlx-hub-cli=mlx_hub_cli:main',
        ],
    },
    author='Gaurav Aggarwal',
    author_email='gauravaggarwal@mail.com',
    description='A CLI for downloading and managing MLX models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/g-aggarwal/mlx-hub',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
