## Inintial Task:
1. You will be prowided with terraform state file. You should develop a simple web service
with a RESTful API service which will allow you to upload this file using curl, parse it and
respond with all security groups in this file. Use an language (not bash) and libs by your
choice.
2. Add parameter which allows to do filtering by attribute in sg rule. For example show all
sg which have sg-21fc3144 in the source (attribute source_security_group_id)
3. Create Dockerfile which will have service from task 1 and will be ran without ports
exposing so it's not available from other hosts
4. Create second docker which will be linked to the first container, proxing requests to it
and do flood prevention/rate limiting by source ip address. This container should expose
8080 port for requests from other hosts.
5. Create docker-compose file which will allow you to build dockers above and run containers
6. Create script for stress testing to check if rate limiting is working or some tool for it
7. Create documentation in markdown format


![Alt text](communications.jpg?raw=true "Communications")



https://github.com/nginx-proxy/nginx-proxy

sudo sh -c "echo '127.0.0.1 app.local' >> /etc/hosts"

docker build -t app:latest flask_app/.
docker build -t my-nginx:latest nginx/.

docker-compose up

curl http://app.local/
curl -X POST -H "Content-Type: application/json" -d @terraform.tfstate http://app.local/



