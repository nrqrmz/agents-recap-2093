"""My Personal Agent
"""

import os
from datetime import datetime
from dotenv import load_dotenv

## Import necessary libraries
pass  # YOUR CODE HERE

## Configurations
ABORT_VALUES = ("quit", "exit", "quit()", "exit()")
load_dotenv()  # Load environment variables (API keys)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

## Instantiate all the tools

# Get the current date
pass  # YOUR CODE HERE

# Polygon API
pass  # YOUR CODE HERE

# Requests tool
pass  # YOUR CODE HERE

# Wikipedia tool
pass  # YOUR CODE HERE

## Instantiate the Model
pass  # YOUR CODE HERE

## Instantiate the agent
pass  # YOUR CODE HERE


def use_agent(user_message, thread_id="abc123"):
    """Use the agent to get a response.
    Returns the response from the agent.
    """
    pass  # YOUR CODE HERE


def main():
    """Main loop of the program
    """
    print("\nWelcome! Type your questions below. Use `quit` or `exit` to stop.")
    print("\n> ", end="")

    while (query := input()).lower() not in ABORT_VALUES:
        print(use_agent(query))
        print("\n> ", end="")


if __name__ == "__main__":
    main()
