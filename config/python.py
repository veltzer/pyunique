from typing import List


console_scripts: List[str] = [
    "pyunique=pyunique.main:main",
]
config_requires: List[str] = [
    "pyyaml",
]
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "tqdm",
    "lmdb",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pydmt",
    "sphinx",
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
requires = config_requires + install_requires + make_requires + test_requires
