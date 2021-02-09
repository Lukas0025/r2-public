build:
	docker build . -t lukasplevac/r2cloud-public:latest

push: build
	docker login
	docker push lukasplevac/r2cloud-public:latest
