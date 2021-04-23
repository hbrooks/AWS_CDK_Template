## Baton Backend APIs

### First Things to Do
1. `chmod 777 scripts/*.sh`
2. `pip install autopep8`
3.  Start the services via `./scripts/start.sh`.  `localhost:8000/docs` should show the API schema.

### How to Deploy
From root of repo:
2.  `./scripts/build_images.sh`
3.  `./scripts/start_containers.sh`
4.  `./scripts/deploy.sh`

