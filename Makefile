dev:
	docker build -t pachicourse/mode-py:dev .
	docker run -ti -v $(PWD):/work pachicourse/mode-py:dev bash
