#!/usr/bin/env python3

from aws_cdk import core

from cdk_src.all import BatonStack


app = core.App()
BatonStack(app, "beta", env={'region': 'us-east-1'})

app.synth()
