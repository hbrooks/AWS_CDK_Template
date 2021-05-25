import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="infrastructure",
    version="0.0.3",

    description="Infrastructure created from https://github.com/hbrooks/python_backend_template",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "infrastructure"},
    packages=setuptools.find_packages(where="infrastructure"),

    install_requires=[
        "aws-cdk.core==1.98.0",
        "aws-cdk.aws-ecr==1.98.0",
        "aws-cdk.aws_iam==1.98.0",
        "aws-cdk.aws_sqs==1.98.0",
        "aws-cdk.aws_sns==1.98.0",
        "aws-cdk.aws_sns_subscriptions==1.98.0",
        "aws-cdk.aws_s3==1.98.0",
        "aws-cdk.aws-lambda==1.98.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
