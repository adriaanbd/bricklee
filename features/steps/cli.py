from behave import *
import subprocess

@when('the user runs the clicbrik hello command with no parameters: {text}')
def step_impl(context, text):
    args = ['poetry', 'run', 'bricklee', 'hello']
    context.response = subprocess.run(args, capture_output=True)

@then('the CLI returns {text}')
def step_impl(context, text):
    bytes_output = context.response.stdout
    expected = "Hello Panama City, Panama."
    assert expected in bytes_output.decode()