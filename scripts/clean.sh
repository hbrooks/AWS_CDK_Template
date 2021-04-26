find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm -rf api_aws/zappa_package.zip
rm -rf infrastructure/cdk.out
