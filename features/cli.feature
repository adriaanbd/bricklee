Feature: Greeting
    Scenario: Generic Greeting
        Given the user runs the bricklee hello command with no parameters
        Then the CLI returns a generic response
    Scenario: Customized Greeting
        Given the user runs the bricklee hello command with the --name flag and 1 parameter
        Then the CLI returns a customized response
