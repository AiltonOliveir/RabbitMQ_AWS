# Rabbitmq-aws


## To-Do EC2 Config
Assume EC2 AWS linux

## RabbitMQ Container 
Install docker
``` bash
sudo yum update -y
sudo yum install docker
sudo service docker start
``` 

Create custom bridge network
``` bash
sudo docker network create mynet
sudo docker network inspect mynet
``` 

Create RabbitMQ nodes
``` bash
sudo docker run -d --hostname rabbit1 --name myrabbit1 -p 15672:15672 -p 5672:5672 --network mynet -e "RABBITMQ_ERLANG_COOKIE=rabbitcookie" -e "RABBITMQ_DEFAULT_USER=user" -e "RABBITMQ_DEFAULT_PASS=password" rabbitmq:3-management
sudo docker run -d --hostname rabbit2 --name myrabbit2 -p 5673:5672 --link myrabbit1:rabbit1 --network mynet -e "RABBITMQ_ERLANG_COOKIE=rabbitcookie" -e "RABBITMQ_DEFAULT_USER=user" -e "RABBITMQ_DEFAULT_PASS=password" rabbitmq:3-management
sudo docker run -d --hostname rabbit3 --name myrabbit3 -p 5674:5672 --link myrabbit1:rabbit1 --link myrabbit2:rabbit2 --network mynet -e "RABBITMQ_ERLANG_COOKIE=rabbitcookie" -e "RABBITMQ_DEFAULT_USER=user" -e "RABBITMQ_DEFAULT_PASS=password" rabbitmq:3-management
``` 
Start node 1
``` bash
docker exec -it myrabbit1 bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
``` 

Start node 2
``` bash
docker exec -it myrabbit2 bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster --ram rabbit@rabbit1
rabbitmqctl -n rabbit@rabbit1 forget_cluster_node rabbit@rabbit2
rabbitmqctl join_cluster --ram rabbit@rabbit1
rabbitmqctl start_app
``` 

Start node 3
``` bash
docker exec -it myrabbit3 bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster --ram rabbit@rabbit1
rabbitmqctl -n rabbit@rabbit1 forget_cluster_node rabbit@rabbit3
rabbitmqctl join_cluster --ram rabbit@rabbit1
rabbitmqctl start_app
``` 

Check cluster status
``` bash
docker exec -it myrabbit1 bash
rabbitmqctl cluster_status
``` 

Enter GUI
``` bash
IP_host@15672
``` 

