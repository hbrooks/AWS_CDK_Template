import os
import aws_cdk.core as core
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_qldb as aws_qldb
import aws_cdk.aws_iam as aws_iam


class ApiAwsStack(core.Stack):

    STACK_NAME_PREFIX = "ApiAwsStack"

    def __init__(self, scope: core.Construct, disambiguator: str, **kwargs) -> None:
        super().__init__(
            scope, '-'.join([self.STACK_NAME_PREFIX, disambiguator]), **kwargs)

        api_aws_lambda = aws_lambda.Function(
            self,
            '-'.join([self.STACK_NAME_PREFIX, disambiguator, 'api_aws']),
            description="Created by CDK.  Don't modify manually!",
            runtime=aws_lambda.Runtime.PYTHON_3_6,
            code=aws_lambda.Code.asset('../api_aws/zappa_package.zip'),
            handler='src.lambda_handler',
            environment={
            },
            function_name='-'.join([self.STACK_NAME_PREFIX,
                                    disambiguator, 'api_aws']),
            memory_size=128,
            reserved_concurrent_executions=10,
            timeout=core.Duration.seconds(10),
        )
        api_aws_rest_api = self.create_API_GW_integration(disambiguator, api_aws_lambda, 'api_aws')
       


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
