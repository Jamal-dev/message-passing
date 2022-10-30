MOUDULE_CONNECTION := modules/connection_service
MOUDULE_LOCATION_ADD := modules/location_service/location_service_add
MOUDULE_LOCATION_LISTEN := modules/location_service/location_service_listen
MOUDULE_PERSON := modules/person_service

.PHONY = all clean kc loc res restart
all:
	@echo "Building $(MOUDULE_CONNECTION) "
	make -C $(MOUDULE_CONNECTION)
	@echo "Building $(MOUDULE_LOCATION_ADD) "
	make -C $(MOUDULE_LOCATION_ADD)
	@echo "Building $(MOUDULE_LOCATION_LISTEN) "
	make -C $(MOUDULE_LOCATION_LISTEN)
	@echo "Building $(MOUDULE_PERSON) "
	make -C $(MOUDULE_PERSON)

clean:
	kubectl delete all --all

loc:
	@echo "Building $(MOUDULE_LOCATION_ADD) "
	make -C $(MOUDULE_LOCATION_ADD)
	@echo "Building $(MOUDULE_LOCATION_LISTEN) "
	make -C $(MOUDULE_LOCATION_LISTEN)

kc:
	@echo "Starting zookeeper and kafka"
	kubectl apply -f kafka
	@echo "Starting deployments"
	kubectl apply -f deployment

restart:
	@echo "Restarting all services and pods"
	kubectl -n default rollout restart deploy
res:
	@echo "Restarting all services and pods"
	kubectl -n default rollout restart deploy
