##OBJECTIVE:
1. This is a template for AppEngine Microservices
2. This aims to run a local application that can access different microservices with different ports. 

##REQUIREMENT:
1. Google AppEngine SDK
2. This is developed using Linux environment

##HOW TO USE:
1. Sync localservices.config to your actual microservices; ports always start at 8080.. 8081.. 8082 and so on.
2. run `sh run.sh` to run the application locally

##IF PORTS DOES NOT EXIT AFTER USAGE:
run `kill -9 `ps aux | grep dev_appserver`
