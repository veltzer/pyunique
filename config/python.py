""" python depedencies for this project """
from typing import List


console_scripts: List[str] = [
    "pyunique=pyunique.main:main",
]
dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "tqdm",
    "lmdb",
]
build_requires: List[str] = [
    "pydmt",
    "pymakehelper",
    "types-tqdm",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
