init:
	pip install pipenv
	pipenv install --dev --ignore-pipfile

test:
	pipenv run pytest --cov=mentorship --cov=mentorship_profile --pep8 --cov-branch --cov-report term-missing

ci:
	pipenv run pytest --pep8 --cov=mentorship --cov=mentorship_profile --cov-report term --cov-report html --cov-branch

coverage:
	pipenv run coveralls
