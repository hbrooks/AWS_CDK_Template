
## To Create the CloudFormation
Be sure to `rm -rf .env/` before deploying so that you don't end up with a dependecy in your `venv` that doesn't exist in `setup.py`
```
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cdk synth
$ pytest # Skip this.
$ cdk deploy
```

## To See all Dependencies:
```
pip freeze
```

## To Add a New Dependency:
Edit `setup.py` with the package name.  Clean all `__pycache__` and `*.egg-info`.  Remove `cdk.out/`.  Recreate the `venv`/