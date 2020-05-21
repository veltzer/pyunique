.PHONY: all

all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pyunique tests
	@pyflakes pyunique tests
	@pytest tests -qq > /dev/null
