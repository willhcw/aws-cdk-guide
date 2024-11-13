import uuid
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class HelloWorldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Generate a unique bucket name with a random UUID suffix
        bucket_name = f"my-hello-world-bucket-{uuid.uuid4().hex[:8]}"

        # Define an S3 bucket with the unique name
        s3.Bucket(
            self,
            "MyHelloWorldBucket",
            bucket_name=bucket_name,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY  # Ensures bucket deletion on `cdk destroy`
        )
