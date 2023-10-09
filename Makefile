hello:
	echo "this is my first make command"
install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
lint:
	pylint --disable=R,C hello.py
test:
	python3 -m pytest -vv test_hello.py