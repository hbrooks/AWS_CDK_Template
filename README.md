## Template for building FastAPI Services on AWS
- Use `./scripts/build_images.sh` to create a Docker image of a Python service (running FastAPI)
- Use `./scripts/start_containers.sh` to start the service on your local (using docker-compose)
- CDK creates a Lambda function + API GateWay integration, but can created any other resources.  An example using QLDB is included.
  - Includes wirings to package Python service and spawn an AWS Lambda function from it using [Zappa](https://github.com/Miserlou/Zappa).  Lambda gets connected to AWS API GateWay and returns an endpoint you can call.
  - You can `curl` the endpoint's `/internal/ping` to check it's health.


### To Run Locally
1. `chmod 777 scripts/*.sh`
2.  Start the services via `./scripts/start.sh`.  
    1.  `localhost:8000/docs` should show the API schema.
    2. `curl localhost:8000/internal/ping` to check health.

### How to Deploy Lambda (and other Infrastructure) to AWS
From root of repo:
1.  `./scripts/build_images.sh`
3.  `./scripts/start_containers.sh`
4.  `./scripts/deploy.sh`
