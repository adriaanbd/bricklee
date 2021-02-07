from behave import *
import subprocess

@given('the user runs the bricklee hello command with no parameters')
def step_impl(context):
    args = ['poetry', 'run', 'bricklee', 'hello']
    context.response = subprocess.run(args, capture_output=True)

@then('the CLI returns a generic response')
def step_impl(context):
    bytes_output = context.response.stdout
    expected = "Hello Panama City, Panama."
    assert expected in bytes_output.decode()

@given('the user runs the bricklee hello command with the --name flag and 1 parameter')
def step_impl(context):
    args = ['poetry', 'run', 'bricklee', 'hello', '--name', 'Adriaan']
    context.response = subprocess.run(args, capture_output=True)

@then('the CLI returns a customized response')
def step_impl(context):
    bytes_output = context.response.stdout
    expected = "Hello Adriaan."
    assert expected in bytes_output.decode()