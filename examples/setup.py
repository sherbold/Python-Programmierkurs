import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="course-sample-package",
    version="0.0.1",
    author="Steffen Herbold",
    author_email="herbold@cs.uni-goettingen.de",
    description="A small example package for a programming course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sherbold/Python-Programmierkurs/tree/master/examples",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
