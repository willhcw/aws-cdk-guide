#!/usr/bin/env python3
from aws_cdk import App
from hello_world.hello_world_stack import HelloWorldStack


app = App()
HelloWorldStack(app, "HelloWorldStack")

app.synth()
