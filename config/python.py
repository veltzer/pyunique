""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "tqdm",
    "lmdb",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
types_requires: list[str] = [
    "types-tqdm",
]
requires = install_requires + build_requires + test_requires + types_requires

scripts: dict[str, str] = {
    "pyunique": "pyunique.main:main",
}
