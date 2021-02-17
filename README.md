## Inintial Task:
1. You ill be pro ided ith terraform state file. You should de elop a simple eb ser ice
ith a RESTful API ser ice hich ill allo ou to upload this file using curl, parse it and
respond ith all securit groups in this file. Use an language (not bash) and libs b our
choice.
2. Add parameter hich allo s to do filtering b attribute in sg rule. For e ample sho all
sg hich ha e sg-21fc3144 in the source (attribute source_securit _group_id)
3. Create Dockerfile hich ill ha e ser ice from task 1 and ill be ran ithout ports
e posing so it s not a ailable from other hosts
4. Create second docker hich ill be linked to the first container, pro ing requests to it
and do flood pre ention/rate limiting b source ip address. This container should e pose
8080 port for requests from other hosts.
5. Create docker-compose file hich ill allo ou to build dockers abo e and run
containers
6. Create script for stress testing to check if rate limiting is orking or some tool for it
7. Create documentation in markdo n format


![Alt text](communications.jpg?raw=true "Communications")