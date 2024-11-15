from aws_cdk import App, Aws, Aspects
from cdk_aspects_use_cases.cdk_aspects_use_cases_stack import CdkAspectsUseCasesStack
from permission_boundary_aspect import PermissionBoundaryAspect

app = App()
stack = CdkAspectsUseCasesStack(app, "CdkAspectsUseCasesStack")

# Dynamically construct the ARN for the permission boundary
boundary_arn = f"arn:aws:iam::{Aws.ACCOUNT_ID}:policy/MyPermissionBoundary"

# Apply the permission boundary Aspect to the stack
Aspects.of(app).add(PermissionBoundaryAspect(permission_boundary_arn = boundary_arn))

app.synth()