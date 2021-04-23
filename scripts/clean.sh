find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm -rf ms_main/zappa_package.zip
rm -rf infrastructure/cdk.out
