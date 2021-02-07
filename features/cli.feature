Feature: Greeting
    Scenario: Generic Greeting
        When the user runs the clicbrik hello command with no parameters: "bricklee hello"
        Then the CLI returns "Hello Panama City, Panama."
    Scenario: Customized Greeting
        When the user runs the clicbrik hello command with the --name flag and 1 parameter: "bricklee hello --name Adriaan"
        Then the CLI returns "Hello Adriaan."
