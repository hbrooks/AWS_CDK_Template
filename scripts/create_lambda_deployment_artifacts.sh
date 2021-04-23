rm -rf ms_main/zappa_package.zip
rm -rf ms_organizations/zappa_package.zip
docker exec -it ms_main bash -c "source /usr/src/scripts/create_zappa_package.sh source say.sh; create_zappa_package ms_main"
docker cp ms_main:/usr/src/ms_main/zappa_package.zip ./ms_main/zappa_package.zip
docker exec -it ms_organizations bash -c "source /usr/src/scripts/create_zappa_package.sh source say.sh; create_zappa_package ms_organizations"
docker cp ms_organizations:/usr/src/ms_organizations/zappa_package.zip ./ms_organizations/zappa_package.zip

