## OBJECTIVE:
1. This is a template for AppEngine Microservices
2. This aims to run a local application that can access different microservices with different ports. 

## REQUIREMENTS:
1. Google AppEngine SDK
2. This is developed using Linux environment

## HOW TO USE:
1. Sync localservices.config to your actual microservices
2. run `sh run.sh` to run the application locally

## LOCAL SERVICES CONFIG
- file = localservices.config
- format: microservice_name<space>port
- note: the first port defined will be the reference port; example: firstport=9090, nextms=9091, next=9092 and so on.


## IF PORTS DOES NOT EXIT AFTER USAGE:
run `kill -9 `ps aux | grep dev_appserver`
