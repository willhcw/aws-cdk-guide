
# AWS CDK Guide with Python

Welcome to the **AWS CDK Guide with Python**! This repository is a hands-on guide to using the [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/), focusing on practical examples and project structures that will help you get started with Infrastructure as Code (IaC) on AWS.

## Table of Contents

1. [Introduction to AWS CDK](#introduction-to-aws-cdk)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Suggested Development Environment](#suggested-development-environment)
4. [Repository Structure](#repository-structure)
5. [Basic Examples](#basic-examples)
6. [Advanced Projects](#advanced-projects)
7. [CDK Commands Overview](#cdk-commands-overview)
8. [AWS CloudFormation vs. CDK](#aws-cloudformation-vs-cdk)
9. [Legal and Licensing](#legal-and-licensing)

---

## Introduction to AWS CDK

The AWS CDK is a software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. With CDK, you can use familiar programming languages to model your infrastructure, making it easier to reuse code, apply best practices, and automate deployments.

**Why Use AWS CDK?**
- Write infrastructure code in your preferred language (in this case, Python).
- Create reusable components for different projects.
- Leverage the power of your IDE for development, testing, and collaboration.

## Setting Up Your Environment

To get started with AWS CDK, you’ll need:
- **Node.js** (CDK CLI requires it)
- **Python 3.7+**
- **AWS CLI** configured with your AWS account credentials

### Installation

1. **Install AWS CDK**:
   ```bash
   npm install -g aws-cdk
   ```

2. **Set Up a Virtual Environment** (optional but recommended for managing dependencies):
   ```bash
   python3 -m venv .env
   source .env/bin/activate  # or .env\Scripts\activate for Windows
   ```

3. **Install Project Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Suggested Development Environment

For a smooth experience, we recommend using **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**. It provides powerful extensions for Python development, integrates well with AWS (with the AWS Toolkit), and supports syntax highlighting and debugging for CDK.

To set up VS Code for CDK development:

1. Install the **Python** extension to enhance Python coding.
2. Use the **AWS Toolkit** extension to connect directly to your AWS account, allowing you to interact with your CDK stacks more effectively.

## Repository Structure

This repository is organized to help you understand and practice different levels of AWS CDK:

- **`basics/`**: Foundational knowledge and simple examples to get you started.
  - `README.md` explains basic concepts, including what AWS CDK is, how to install it, and how to create a basic resource.
  - `hello_world/` contains a "Hello, World" project to demonstrate creating a simple S3 bucket using CDK.

- **`projects/`**: Example projects organized by use case to demonstrate real-world applications.
  - `cdk-aspects-use-cases/` shows how to Aspects to enforce configurations on resources across your stack.
  - `iam-role/` focuses on a iam setup with CDK tool.

## Basic Examples

For those new to CDK, start with the `basics/` folder. It includes a "Hello, World" example where you'll learn to create an S3 bucket, deploy it to AWS, and see how CDK translates Python code into AWS infrastructure.

Navigate to [basics/README.md](basics/README.md) for a full introduction.

## Advanced Projects

For more advanced use cases, explore the `projects/` folder. Each project includes:
- **A defined app with separate stack files** for organizing resources.
- **Modular components** that can be extended or reused.
- **Guidance on deploying each project** with `cdk synth` and `cdk deploy` commands.

## CDK Commands Overview

AWS CDK relies on a few essential commands that you'll use frequently as you develop and deploy infrastructure:

- **`cdk synth`**: This command synthesizes your CDK app and generates the AWS CloudFormation template. It’s a great way to see what will be deployed without actually creating any resources.

- **`cdk deploy`**: Deploys the resources defined in your CDK app to your AWS account. This command creates or updates the resources based on your code.

- **`cdk destroy`**: Safely removes the resources created by `cdk deploy`. This command is useful for cleaning up resources you no longer need, which helps control costs.

- **`cdk diff`**: Compares the current stack state with your code to show changes that would be made if you ran `cdk deploy`.

For a hands-on introduction, navigate to the [basics/README.md](basics/README.md) and follow along with the "Hello, World" example. This section explains these commands in action and guides you through each step to see how CDK code becomes AWS infrastructure.

## AWS CloudFormation vs. CDK

While **CloudFormation** uses YAML/JSON templates, **AWS CDK** allows you to write infrastructure as code in a programming language like Python, offering several advantages:

- **Simplicity**: CDK abstracts repetitive code, making complex setups easier to read and maintain.
- **Reusability**: CDK allows you to reuse components (constructs) and organize your code.
- **IDE Support**: With CDK, you can leverage IDE features like autocompletion, syntax checking, and code navigation.

CDK generates CloudFormation templates under the hood, so you're still deploying through CloudFormation but with the added power of a real programming language.

## Legal and Licensing

This project is open-source and licensed under the [MIT License](LICENSE). All code and content are independently created and intended to be used as learning resources. **AWS CDK** is a product of **Amazon Web Services, Inc.** and this repository is in no way affiliated with or endorsed by Amazon.

---

Happy coding and happy deploying with AWS CDK! 🎉

For questions, contributions, or feedback, feel free to open an issue or submit a pull request.
