root=$(shell pwd)

build:
	docker build . -t lukasplevac/r2cloud-public:latest

run: build
	docker-compose -f docker-stack-example.xml up

stop:
	docker-compose -f docker-stack-example.xml down

push: build
	docker login
	docker push lukasplevac/r2cloud-public:latest

clean:
	docker-compose -f docker-stack-example.xml rm
