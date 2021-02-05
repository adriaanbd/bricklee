from behave import *
from clicbrik import entrypoint
from pytest import capsys

@given('the user runs the clicbrik hello command')
def step_impl(context):
    pass

@when('the user attaches no additional parameters to the command')
def step_impl(context, text):
    pass

@then('the CLI answers "Hello Panama City, Panama."')
def step_impl(context, text, capsys):
    entrypoint.main(text)
    print(capsys)
    assert text in capsys