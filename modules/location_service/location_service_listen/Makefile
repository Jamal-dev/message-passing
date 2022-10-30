SERVICE_NAME := udaconnect-location-service-listen
DOCKER_ID := hobbeslucretius
TAG_NAME := latest

IMAGE_NAME := $(DOCKER_ID)/$(SERVICE_NAME):$(TAG_NAME)

.PHONY = all
all:
	@echo "Building $(SERVICE_NAME) image"
	docker build -t $(IMAGE_NAME) .
	@echo "Pusing $(SERVICE_NAME) to Docker Hub at $(IMAGE_NAME)"
	docker push $(IMAGE_NAME)
