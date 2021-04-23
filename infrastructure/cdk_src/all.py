import os
import aws_cdk.core as core
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_qldb as aws_qldb
import aws_cdk.aws_iam as aws_iam


class BatonStack(core.Stack):

    STACK_NAME_PREFIX = "Baton"

    def __init__(self, scope: core.Construct, disambiguator: str, **kwargs) -> None:
        super().__init__(
            scope, '-'.join([self.STACK_NAME_PREFIX, disambiguator]), **kwargs)

        qldb = aws_qldb.CfnLedger(
            self,
            '-'.join([self.STACK_NAME_PREFIX, disambiguator, 'db']),
            permissions_mode="ALLOW_ALL",
            deletion_protection=False, # TODO: Use `isProd`-like functionality here.
            name = '-'.join([self.STACK_NAME_PREFIX, disambiguator, 'db']),
        )

        ms_organizations = aws_lambda.Function(
            self,
            '-'.join([self.STACK_NAME_PREFIX, disambiguator, 'ms_organizations']),
            description="Created by CDK.  Don't modify manually!",
            runtime=aws_lambda.Runtime.PYTHON_3_6,
            code=aws_lambda.Code.asset('../ms_organizations/zappa_package.zip'),
            handler='src.lambda_handler',
            environment={
                'QLDB_NAME': qldb.name
            },
            function_name='-'.join([self.STACK_NAME_PREFIX,
                                    disambiguator, 'ms_organizations']),
            memory_size=128,
            reserved_concurrent_executions=10,
            timeout=core.Duration.seconds(10),
        )
        ms_organizations_rest_api = self.create_API_GW_integration(disambiguator, ms_organizations, 'ms_organizations')
        ms_organizations.role.add_to_policy(aws_iam.PolicyStatement(
            resources=[f"arn:aws:qldb:{self.region}:{self.account}:ledger/{qldb.name}"],
            actions=["qldb:SendCommand"]
        ))

        ms_main = aws_lambda.Function(
            self,
            '-'.join([self.STACK_NAME_PREFIX, disambiguator, 'ms_main']),
            description="Created by CDK.  Don't modify manually!",
            runtime=aws_lambda.Runtime.PYTHON_3_6,
            code=aws_lambda.Code.asset('../ms_main/zappa_package.zip'),
            handler='src.lambda_handler',
            environment={
                'MS_ORGANIZATIONS_API': ms_organizations_rest_api.url
            },
            function_name='-'.join([self.STACK_NAME_PREFIX,
                                    disambiguator, 'ms_main']),
            memory_size=128,
            reserved_concurrent_executions=10,
            timeout=core.Duration.seconds(10),
        )
        self.create_API_GW_integration(disambiguator, ms_main, 'ms_main')
        

    def create_API_GW_integration(self, disambiguator: str, lambda_function: aws_lambda.Function, function_name: str) -> apigateway.RestApi:
        lambda_integration = apigateway.LambdaIntegration(lambda_function)

        # The fields in this construct can't be tokens, for example, references to the lambda function name:
        # jsii.errors.JSIIError: Cannot use tokens in construct ID: DocumentGuardian-beta-ApiGw-${Token[TOKEN.87]}
        # Which is why this function has the `function_name` arg.
        api_gw_rest_api = apigateway.RestApi(
            self,
            '-'.join([self.STACK_NAME_PREFIX,
                      disambiguator, 'ApiGw', function_name]),
            rest_api_name='-'.join([self.STACK_NAME_PREFIX,
                                    disambiguator, function_name]),
            description="This API handles all requests to " +
                self.STACK_NAME_PREFIX+function_name +".",
        )
        api_gw_rest_api.root.add_method('ANY', lambda_integration)

        api_gw_proxy = apigateway.Resource(
            self,
            '-'.join([self.STACK_NAME_PREFIX,
                      disambiguator, function_name, 'root']),
            parent=api_gw_rest_api.root,
            path_part='{proxy+}'
        )
        api_gw_proxy.add_method('ANY', lambda_integration)
        return api_gw_rest_api
