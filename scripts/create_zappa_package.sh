create_zappa_package () {
    rm -rf /usr/src/$1/zappa_venv/
    cd /usr/src/$1/
    pip3 install virtualenv
    python3 -m venv zappa_venv
    source ./zappa_venv/bin/activate
    pip install --upgrade pip
    pip3 install zappa
    pip3 install -r /usr/src/$1/requirements.txt
    zappa package -s ./zappa_settings.json --output /usr/src/$1/zappa_package.zip
    exit 0
}
