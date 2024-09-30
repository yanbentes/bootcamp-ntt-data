from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requiriments.txt") as f:
    requiriments = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Karina",
    descripton="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiemi/image-processing-package",
    packages=find_packages(),
    install_requires=requiriments,
    python_requires=">=3.5"
)
