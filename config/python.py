""" python deps for this project """

scripts: dict[str, str] = {
    "pyunique": "pyunique.main:main",
}

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "tqdm",
    "lmdb",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    # types
    "types-tqdm",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
