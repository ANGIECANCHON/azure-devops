hello:
	echo "this is my first make command"
install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
test:
	python3 -m pytest -vv test_hello.py