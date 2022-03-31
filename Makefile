DESTDIR=server

all: start
	@echo "Done"

docker-all: docker-build docker-start
	@echo "Done"

docker-build: 
	@echo "building the image from the docker file..."
	docker build --no-cache --pull -t svmiris .
	@echo "image Done"

docker-start:
	@echo "starting the NEW service in container..."
	docker run -p 8080:8080 svmiris

docker-iter:
	@echo "starting service interactively..."
	docker run -p 8080 -it svmiris

service:
	@echo "creating service"
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	@echo "starting the NEW service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-stop:
	@echo "stopping the service..."
	docker stop $$(docker ps -al
