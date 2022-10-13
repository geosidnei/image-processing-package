from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img-process",
    version="0.0.1r",
    author="Rafael Toramaru",
    author_email="rafaeltoramaru@gmail.com",https://github.com/geosidnei/image-processing-package/edit/main/setup.pyhttps://github.com/geosidnei/image-processing-package/edit/main/setup.py
    revisor='sidnei lopes ribeiro',
    revisor_email='geosidnei@gmail.com',
    description="Test version: Image processing.This project belongs to Karina Tiemi Kato. The Author is Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp developer full stack Python (2022, October). E-mail:karinatkato@gmail.com",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RToramaru/image-processing-package",
    fork='https://github.com/geosidnei/image-processing-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
