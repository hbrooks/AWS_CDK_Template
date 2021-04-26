create_lambda_deployment_artifact () {
    # Accepts the name of a service as the first and only argument.  
    rm -rf $1/zappa_package.zip
    docker exec -it $1 bash -c "source /usr/src/scripts/create_zappa_package.sh source say.sh; create_zappa_package ms_main"
    docker cp $1:/usr/src/$1/zappa_package.zip ./$1/zappa_package.zip
}
