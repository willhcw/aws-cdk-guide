from aws_cdk import (
    # Duration,
    Stack,
    aws_iam as iam
    # aws_sqs as sqs,
)
from constructs import Construct

class IamRoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        test_role = iam.Role(
            self, "TestRole",
            assumed_by=iam.ServicePrincipal("s3.amazonaws.com"),
            description="Allows S3 to access the bucket",
            role_name="TestRole"
        )

        test_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))
