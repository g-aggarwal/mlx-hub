from setuptools import setup, find_packages


def get_version() -> str:
    rel_path = "src/mlx_hub/__init__.py"
    with open(rel_path, "r") as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                separator = '"' if '"' in line else "'"
                return line.split(separator)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name='mlx_hub',
    version='get_version()',
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'mlx_hub': ['suggested_models.txt', 'login_help.txt'],
    },
    install_requires=[
        'huggingface-hub>=0.23.4',
    ],
    entry_points={
        'console_scripts': [
            'mlx-hub-cli=mlx_hub.cli:main',
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
