import jsii
from aws_cdk import IAspect, Aws
from aws_cdk.aws_iam import CfnRole
from constructs import IConstruct
from typing import Any

@jsii.implements(IAspect)
class PermissionBoundaryAspect:
    def __init__(
        self, 
        permission_boundary_arn: str,
    ) -> None:
        self.permission_boundary_arn = permission_boundary_arn

    def visit(self, node: IConstruct) -> None:
        # Apply only to IAM Roles
        if isinstance(node, CfnRole) and not node.permissions_boundary:
            # Attach the permission boundary during synthesis
            if self.permission_boundary_arn:
                node.add_property_override("PermissionsBoundary", self.permission_boundary_arn)