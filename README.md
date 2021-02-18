### Inintial Task:
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

### Usage 
Add hostname:

    $ sudo sh -c "echo '127.0.0.1 app.local' >> /etc/hosts"

Build applicatiuon and [ngnix](https://nginx.org/) images: 

    $ docker-compose build

Now start with docker-compose: 

    $ docker-compose up


To check how it works you can run:

```sh
curl http://app.local/
curl -X POST -H "Content-Type: application/json" -d @terraform.tfstate http://app.local/
[
  "sg-23076c5e", 
  "sg-21fc3144", 
  "sg-d7e71aac", 
  "sg-6a016a17", 
  "sg-97de23ec"
]
```


> Note: This is a development server. Do not use it in a production deployment.

## Stress testing
Install apache2-utils

    $ sudo apt install apache2-utils

Now you can run test with 1000 requests with a concurrency of 100.
```sh
$ ab -n 1000 -c 100 http://app.local/
...
Complete requests:      1000
Failed requests:        0
...

```

Now, changing nginx configuration for [Basic Rate Limiting](https://www.nginx.com/blog/rate-limiting-nginx/#Configuring-Basic-Rate-Limiting) to
```sh
    limit_req_zone $binary_remote_addr zone=mylimit:10m rate=5r/s; 
```
Now limit is 5 requests per second per one IP. And test results for this configuration is:
```sh
$ ab -n 1000 http://app.local/
...
Concurrency Level:      1
Time taken for tests:   0.464 seconds
Complete requests:      1000
Failed requests:        997
...
```

### What was done:
- [x] RESTful API service which will allow you to upload file using curl
- [ ] Add parameter which allows to do filtering by attribute in sg rule.
- [x] Create Dockerfile which will have service from task 1 
- [x] Create second docker which will be linked to the first container, proxing requests 
- [x] Create docker-compose file which will allow you to build dockers above and run containers
- [x] Create script for stress testing to check if rate limiting is working or some tool for it
- [x] Create documentation in markdown format

### What can be improved:       
- Task 2 needs to be completed
- Enable Https 
- All this can be deployed to AWS ECS with Terraform 

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
