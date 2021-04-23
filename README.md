## Template for building FastAPI Services on AWS
- Creates 2 FastAPI Docker services
- Creates a QLDB DB via CDK
- Includes scripts to deploy to AWS Lambda

### First Things to Do
1. `chmod 777 scripts/*.sh`
2. `pip install autopep8`
3.  Start the services via `./scripts/start.sh`.  `localhost:8000/docs` should show the API schema.

### How to Deploy
From root of repo:
1.  `./scripts/build_images.sh`
3.  `./scripts/start_containers.sh`
4.  `./scripts/deploy.sh`
