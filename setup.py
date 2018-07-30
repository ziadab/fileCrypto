import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fileCrypto",
    version="3.2",
    author="Ziad Abouelfarah",
    author_email="zain.work02@gmail.com",
    description="Protecting File Was Never Easier Than Before",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ziadab/fileCrypto",
    packages=(setuptools.find_packages()),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)