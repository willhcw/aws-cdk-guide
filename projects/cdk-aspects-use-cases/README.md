
# AWS CDK Aspects: Use Cases and Examples

This project demonstrates the power of AWS CDK Aspects by showcasing real-world use cases. **CDK Aspects** allow you to enforce consistent configurations, apply security policies, and ensure compliance across resources in your CDK stack.

## Table of Contents

1. [What are CDK Aspects?](#what-are-cdk-aspects)
2. [Why Use CDK Aspects?](#why-use-cdk-aspects)
3. [How CDK Aspects Work](#how-cdk-aspects-work)
4. [Use Case: Enforcing Permission Boundaries](#use-case-enforcing-permission-boundaries)
   - [Introduction to Permission Boundaries](#introduction-to-permission-boundaries)
   - [Creating a Permission Boundary Policy](#creating-a-permission-boundary-policy)
   - [Applying Permission Boundaries with CDK Aspects](#applying-permission-boundaries-with-cdk-aspects)
5. [Project Structure](#project-structure)
6. [Additional Resources](#additional-resources)

## What are CDK Aspects?

AWS CDK Aspects allow you to programmatically enforce configurations on resources across your stack. With Aspects, you can:
- Apply settings to multiple resources without duplicating code.
- Ensure compliance with organizational standards.
- Handle resources created internally by CDK functions.

## Why Use CDK Aspects?

CDK Aspects are particularly useful when:
- Resources are created indirectly by CDK helper functions (e.g., `bucket.add_event_notification`).
- You want to apply configurations like tagging, encryption, logging, or security policies globally.
- Your organization enforces strict standards, such as attaching permission boundaries to IAM roles.

## How CDK Aspects Work

CDK Aspects work by traversing the construct tree in your stack and applying a specified behavior to resources that match certain criteria. You define an Aspect class with a `visit` method to apply the behavior, and then attach the Aspect to your stack.

## Use Case: Enforcing Permission Boundaries

### Introduction to Permission Boundaries

A **Permission Boundary** is an advanced IAM feature that restricts the maximum permissions a role can have. It acts as a guardrail, ensuring that even if a role’s policy grants excessive permissions, the boundary will limit its scope.

In environments where IAM users or roles are restricted to creating resources with specific permission boundaries, CDK Aspects can enforce this boundary on all IAM roles in a stack—whether created directly in the code or indirectly by CDK functions.

### Creating a Permission Boundary Policy

Follow these steps to create a permission boundary policy in the AWS Management Console:

1. **Log in to the AWS Console**:
   - Navigate to the **IAM Dashboard** in the AWS Management Console.

2. **Create a New Policy**:
   - In the IAM Dashboard, select **Policies** from the left-hand navigation menu.
   - Click the **Create policy** button.

3. **Define the Policy**:
   - Under the **Visual editor** tab, click **JSON** to switch to JSON mode.
   - Copy and paste the following JSON policy document:
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "s3:*",
                     "dynamodb:*"
                 ],
                 "Resource": "*"
             }
         ]
     }
     ```

4. **Review and Name the Policy**:
   - Click **Next: Tags** (optional).
   - Click **Next: Review**.
   - Provide a name for the policy, such as `MyPermissionBoundary`.
   - Add a description to explain its purpose, e.g., "Restricts permissions for roles to specific actions."

5. **Save the Policy**:
   - Click **Create policy** to finalize the policy.

### Applying Permission Boundaries with CDK Aspects

#### Define the Aspect

Create a file `permission_boundary_aspect.py` with the following code:

```python
import jsii
from aws_cdk import IAspect, Aws
from aws_cdk.aws_iam import CfnRole
from constructs import IConstruct

@jsii.implements(IAspect)
class PermissionBoundaryAspect:
    def __init__(self, permission_boundary_arn: str) -> None:
        self.permission_boundary_arn = permission_boundary_arn

    def visit(self, node: IConstruct) -> None:
        # Apply only to IAM Roles
        if isinstance(node, CfnRole) and not node.permissions_boundary:
            # Attach the permission boundary during synthesis
            if self.permission_boundary_arn:
                node.add_property_override("PermissionsBoundary", self.permission_boundary_arn)
```

#### Apply the Aspect Dynamically

Modify `app.py` to dynamically fetch the account ID and apply the Aspect:

```python
from aws_cdk import App, Aws, Aspects
from cdk_aspects_use_cases.cdk_aspects_use_cases_stack import CdkAspectsUseCasesStack
from permission_boundary_aspect import PermissionBoundaryAspect

app = App()
stack = CdkAspectsUseCasesStack(app, "CdkAspectsUseCasesStack")

# Dynamically construct the ARN for the permission boundary
boundary_arn = f"arn:aws:iam::{Aws.ACCOUNT_ID}:policy/MyPermissionBoundary"

# Apply the permission boundary Aspect to the stack
Aspects.of(app).add(PermissionBoundaryAspect(permission_boundary_arn=boundary_arn))

app.synth()
```

#### Define the Stack

In `cdk_aspects_use_cases_stack.py`, define a stack that includes:
- A manually created IAM role.
- An S3 bucket with an event notification, which generates roles internally.

```python
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
```

## Project Structure

To follow this use case, create the following structure:

```plaintext
cdk-aspects-use-cases/
├── app.py                          # Main app file where the stack is defined
├── cdk.json                        # CDK configuration file
├── README.md                       # Documentation (this file)
├── requirements.txt                # Project dependencies
├── permission_boundary_aspect.py   # Defines the PermissionBoundaryAspect class
└── cdk_aspects_use_cases/
    ├── __init__.py                 # Marks the directory as a package
    └── cdk_aspects_use_cases_stack.py # Stack definition with manual and internal role examples
```

To set up the CDK environment, refer to [aws-cdk-guide/basics/README.md](../basics/README.md).

## Additional Resources

For more insights into CDK Aspects and their use cases, you can check out this excellent article by Matt Martz: [Breaking Bad Practices with CDK Aspects](https://matt.martz.codes/breaking-bad-practices-with-cdk-aspects).

This article explores additional scenarios where CDK Aspects can enforce best practices, complementing the use case demonstrated in this project.

---

This project provides a reusable pattern for using AWS CDK Aspects to enforce compliance. You can extend this approach to other use cases, such as tagging, encryption, and monitoring.
