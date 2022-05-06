import config.project

package_name = config.project.project_name

console_scripts = [
    "pyunique=pyunique.main:main",
]

run_requires = [
    "pytconf",
    "pylogconf",
    "tqdm",
    "lmdb",
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
    "pyyaml",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
