from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    print("Setting up regxon README.md")
    long_description = fh.read()

setup(
    name="regxon",
    version="0.0.8",
    description="RegXon is a powerful validator, sanitizer and content parser that you're searching for decades.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bishwas-py/regxon",
    author="Bishwas Bhandari",
    author_email="bishwasbh@gmail.com",
    py_modules=["regxon"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "beautifulsoup4 == 4.11.1"
    ]
)
