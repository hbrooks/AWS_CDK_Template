./scripts/clean.sh
source ./scripts/create_lambda_deployment_artifact.sh; create_lambda_deployment_artifact api_aws
./scripts/deploy_infra.sh