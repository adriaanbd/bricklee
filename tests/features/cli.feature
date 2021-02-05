Feature: Greeting
    Scenario: Generic Greeting
        Given the user runs the clicbrik hello command, e.g. clicbrik hello
        When the user attaches no additional parameters to the command, e.g. "hello"
        Then the CLI answers "Hello Panama City, Panama."

    Scenario: Customized Greeting
        Given the user runs the clicbrik hello command with the --name flag
        When the user includes a string after the --name flag, e.g. "clicbrik hello --name Adriaan"
        Then the CLI answers "Hello Adriaan."