import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pyunique",
    version="0.0.11",
    packages=[
        "pyunique",
    ],
    # from here all is optional
    description="Pyunique helps you get rid of duplicate files",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "duplicates",
        "remove",
        "hash",
    ],
    url="https://veltzer.github.io/pyunique",
    download_url="https://github.com/veltzer/pyunique",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
        "pytconf",
        "pylogconf",
        "tqdm",
        "lmdb",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": [
        "pyunique=pyunique.main:main",
    ]},
)
