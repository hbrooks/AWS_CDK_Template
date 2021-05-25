#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { TStack } from '../lib/t-stack';

const app = new cdk.App();
new TStack(app, 'TStack');
