import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_src",
    version="0.0.2",

    description="Infrastructure for Baton backend.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk_src"},
    packages=setuptools.find_packages(where="cdk_src"),

    install_requires=[
        "aws-cdk.core==1.98.0",
        "aws-cdk.aws-dynamodb==1.98.0",
        "aws_cdk.aws_apigateway==1.98.0",
        "aws-cdk.aws_iam==1.98.0",
        "aws-cdk.aws_s3==1.98.0",
        "aws-cdk.aws-lambda==1.98.0",
        "aws-cdk.aws-cognito==1.98.0",
        'aws_cdk.aws_qldb==1.98.0',
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
