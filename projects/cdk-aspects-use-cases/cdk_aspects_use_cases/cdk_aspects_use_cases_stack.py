import uuid
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
    aws_sns as sns,
    aws_s3_notifications as s3_notifications,
    RemovalPolicy
)
from constructs import Construct

class CdkAspectsUseCasesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Manually create IAM role
        iam_role = iam.Role(
            self,
            "ManualRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            role_name="ManualRoleForExample"
        )

        # S3 bucket with event notification, which creates roles internally
        # Generate a unique bucket name with a random UUID suffix
        bucket_name = f"my-bucket-{uuid.uuid4().hex[:8]}"

        bucket = s3.Bucket(
            self,
            "BucketWithEventNotification",
            bucket_name=bucket_name,
            removal_policy=RemovalPolicy.DESTROY  # Ensures bucket deletion on `cdk destroy`
        )

        # Create an SNS topic for bucket notifications
        topic = sns.Topic(
            self,
            "BucketNotificationTopic",
        )

        # Add event notification to the bucket
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.SnsDestination(topic)
        )