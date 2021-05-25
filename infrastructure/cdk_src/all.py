import os

import aws_cdk.core as core
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_lambda as aws_lambda


class ExampleAwsStack(core.Stack):
    """
    Creates a Lambda hooked up to an API GW.
    """

    STACK_NAME_PREFIX = "ExampleAwsStack"

    def __init__(self, scope: core.Construct, disambiguator: str, **kwargs) -> None:
        super().__init__(
            scope, '-'.join([self.STACK_NAME_PREFIX, disambiguator]), **kwargs)

        ecr_image = aws_lambda.EcrImageCode.from_asset_image(
             directory = os.path.join(os.getcwd(), "..", "python_lambda_code")
         )

        lambda_function = aws_lambda.Function(self, 
             id = "TestPythonLambdaFromContainer",
             description = "A Python Lambda built from a Container.",
             code = ecr_image,
             handler = aws_lambda.Handler.FROM_IMAGE,
             runtime = aws_lambda.Runtime.FROM_IMAGE,
             environment = {"hello":"world"},
             function_name = "TestPythonLambdaFromContainer",
             memory_size = 128,
             reserved_concurrent_executions = 1,
             timeout = core.Duration.seconds(10),
        )
        lambda_function_name = 'PythonService'


        lambda_integration = apigateway.LambdaIntegration(lambda_function)  
        api_gw_rest_api = apigateway.RestApi(
            self,
            '-'.join([self.STACK_NAME_PREFIX,
                      disambiguator, 'ApiGw', lambda_function_name]),
            rest_api_name='-'.join([self.STACK_NAME_PREFIX,
                                    disambiguator, lambda_function_name]),
            description="This API handles all requests to " +
                self.STACK_NAME_PREFIX+lambda_function_name +".",
        )
        api_gw_rest_api.root.add_method('ANY', lambda_integration)

        api_gw_proxy = apigateway.Resource(
            self,
            '-'.join([self.STACK_NAME_PREFIX,
                      disambiguator, lambda_function_name, 'root']),
            parent=api_gw_rest_api.root,
            path_part='{proxy+}'
        )
        api_gw_proxy.add_method('ANY', lambda_integration)

