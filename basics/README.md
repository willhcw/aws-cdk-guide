
# AWS CDK Basics

Welcome to the AWS CDK basics! Here, you’ll learn foundational concepts and start building your first AWS resource using the AWS Cloud Development Kit (CDK) with Python.

## Table of Contents

1. [What is AWS CDK?](#what-is-aws-cdk)
2. [Setting Up](#setting-up)
3. [Project Structure](#project-structure)
4. [Your First CDK App - Hello, World](#your-first-cdk-app---hello-world)
5. [Exploring the Files](#exploring-the-files)
6. [Synthesizing and Deploying](#synthesizing-and-deploying)

## What is AWS CDK?

AWS CDK allows you to define cloud resources with real programming languages. You can use constructs (reusable building blocks) and organize your infrastructure with familiar coding patterns.

## Setting Up

To get started with the basics, follow these steps to create your first CDK project:

1. **Create a Project Folder**:
   - Start by creating a folder for this example. Open your terminal and run:
     ```bash
     mkdir hello_world
     cd hello_world
     ```

2. **Initialize a CDK App**:
   - With AWS CDK, each project begins by initializing an app. This will set up the necessary files and folders. Run:
     ```bash
     cdk init app --language python
     ```

3. **Set Up a Virtual Environment**:
   - It's a good practice to use a virtual environment to manage dependencies for each CDK project. To set it up, run:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate  # Use .venv\Scripts\activate for Windows
     ```

4. **Install CDK Python Dependencies**:
   - CDK projects require certain libraries. After setting up the environment, install dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

You’re now ready to start coding your first CDK stack!

## Project Structure

After running `cdk init app --language python` in your `hello_world` folder, you will see a structure like this:

```plaintext
hello_world/
├── .venv/                   # Virtual environment for managing dependencies (not detailed here)
├── app.py                   # Main app definition
├── cdk.json                 # Configures the entry point (app.py)
├── README.md                # Documentation for your CDK app
├── requirements.txt         # Lists Python dependencies for your CDK project
├── requirements-dev.txt     # Lists development dependencies (e.g., testing libraries)
├── source.bat               # Activates the virtual environment in Windows
├── source.sh                # Activates the virtual environment in Linux/Mac
├── hello_world/
│   ├── __init__.py          # Makes this directory a package
│   └── hello_world_stack.py # Stack definition where you define AWS resources
└── tests/                   # Folder for unit tests
    ├── __init__.py          # Marks tests directory as a package
    └── unit/
        └── test_hello_world_stack.py # Example unit test for your stack
```

### File Descriptions

- **`.venv/`**: This directory contains your virtual environment, helping manage dependencies independently of your global Python environment.
- **`app.py`**: The main entry point for your CDK app, where you initialize the application and specify the stack(s) to include.
- **`cdk.json`**: Configures the CDK CLI, specifying which file to run as the entry point (`app.py`).
- **`README.md`**: Contains documentation and guidance for your project.
- **`requirements.txt`**: Lists required Python libraries, such as `aws-cdk-lib`, used to define AWS resources.
- **`requirements-dev.txt`**: Lists additional dependencies needed for development, such as testing libraries.
- **`source.bat`** and **`source.sh`**: Scripts to activate the virtual environment. Run `source.bat` on Windows or `source.sh` on Linux/Mac.
- **`hello_world/`**: A subdirectory that contains your stack definitions and related files.
  - **`__init__.py`**: Marks this directory as a Python package, allowing imports within the project.
  - **`hello_world_stack.py`**: Defines your AWS resources as part of a stack (e.g., S3 buckets, Lambda functions).
- **`tests/`**: Contains unit tests for your CDK application.
  - **`__init__.py`**: Marks the tests directory as a Python package.
  - **`unit/test_hello_world_stack.py`**: A sample unit test for validating your stack.

---

## Your First CDK App - Hello, World

In this example, you'll create a simple "Hello, World" CDK app that defines an S3 bucket. The default code created by `cdk init` needs to be replaced, so please **copy the code snippets** in the linked files below into `app.py` and `hello_world_stack.py`:

### Code Walkthrough

1. **[app.py](app_details.md)**: The main entry point, initializing your CDK application and loading your stack.
2. **[hello_world_stack.py](hello_world_stack_details.md)**: Defines your S3 bucket using CDK constructs.

### Running the App

After setting up your files, you can now synthesize and deploy your stack.

## Synthesizing and Deploying

1. **Synthesize the CloudFormation Template**:
   - The `cdk synth` command will convert your CDK code into a CloudFormation template. This command lets you see what CDK is generating before deployment.
     ```bash
     cdk synth
     ```
   - The output will be a CloudFormation YAML template that shows the resources you defined in your stack.

2. **Deploy to AWS**:
   - To deploy the stack, run:
     ```bash
     cdk deploy
     ```
   - This command will prompt you to confirm the deployment and will then create the resources in your AWS account.

3. **Cleaning Up Resources**:
   - To avoid ongoing costs, you can remove the resources by running:
     ```bash
     cdk destroy
     ```
   - This command will delete everything created by the `cdk deploy` command.

## Exploring the Files

Refer to [app_details.md](app_details.md) and [hello_world_stack_details.md](hello_world_stack_details.md) for deeper insights into each file's purpose and code.

---

Enjoy building with CDK! For additional examples, check out the main project README or dive into the `projects/` folder.
