Feature: Greeting
    Scenario: Generic Greeting
        Given the user runs the clicbrik hello command with no parameters: "bricklee hello"
        Then the CLI returns "Hello Panama City, Panama."
    Scenario: Customized Greeting
        Given the user runs the clicbrik hello command with no parameters: "bricklee hello"
        Then the CLI returns "Hello Adriaan."
