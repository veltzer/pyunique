import config.project

package_name = config.project.project_name

console_scripts = [
    'pyunique=pyunique.endpoints.main:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',  # for command line parsing
    'pylogconf',  # for logging configuration
    'tqdm',  # for progress reporting
    'lmdb',  # for archive
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pytest-cov',  # for testing
    'flake8',  # for linting
    'pymakehelper',  # for make
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
    'pyyaml',  # for yaml parsing
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
    #    ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
