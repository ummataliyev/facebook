docker-up:
	sudo docker-compose -f docker-compose.yml up

docker-build:
	sudo docker build -t fb_parsing .

docker-exsist:
	sudo docker compose ls --all


docker-run:
	sudo docker run 8b593bb1dc322eb59ad60140444a8b3191b90108268431c81593cec15f6e2803 # image id should be different

docker-create-network:
	docker network create mynetwork

docker-create-network-with-db:
	docker run --network=mynetwork --name=mydb -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=postgres -h=mydbhost -p 5431:5432 -d postgres
