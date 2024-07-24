# Copyright (c) 2024 Gaurav Aggarwal

import argparse
import mlx_hub.core as mlx_hub
import mlx_hub.utils as utils

from enum import Enum

LOGIN_HELP_FILE = "login_help.txt"


class Action(Enum):
    LOGIN = ("login", "", "Add Hugging Face access token", False)
    START = ("start", "", "Start Interactive Mode", False)
    SCAN = ("scan", "", "Scan for downloaded models in the Hugging Face cache")
    SEARCH = ("search", "phrase", "Search for MLX models using a search phrase")
    SUGGEST = ("suggest", "", "Suggest MLX models to download")
    DOWNLOAD = ("download", "model_id", "Download a specific model")
    DELETE = ("delete", "model_id", "Delete a specific model")
    EXIT = ("exit", "", "Exit Interactive Mode")
    HELP = ("help", "", "Show this help message")
    INVALID = ("invalid", "", "Invalid action", False)

    def __new__(cls, value: str, parameter: str, description: str, is_interactive: bool = True):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.option = "--" + value
        obj.parameter = parameter
        obj.description = description
        obj.interactive = is_interactive
        return obj


def print_action_login_help():
    utils.print_packaged_file(LOGIN_HELP_FILE)


def print_action_help():
    """Prints available actions for interactive mode."""
    print("Available Actions:")
    for action in Action:
        if action.interactive:
            print(f"    {action.value:<10} {action.parameter:<10} {action.description}")


def print_string_list(string_list):
    for item in string_list:
        print(item)


def execute_action(action, parameter=None):
    """Executes the given action with optional parameters."""
    print()

    if action == Action.SCAN:
        model_list = mlx_hub.scan()
        if len(model_list) == 0:
            print("No models found!")
        else:
            print(f"{len(model_list)} models found: ")
        print_string_list(model_list)

    elif action == Action.SEARCH:
        if parameter:
            models_list = mlx_hub.search(parameter)
            count = len(models_list)
            if count == 0:
                print("No models found!")
            elif count == mlx_hub.SEARCH_LIMIT:
                print(f"Showing top {mlx_hub.SEARCH_LIMIT} results:")
            else:
                print(f"{count} models found:")
            print_string_list(models_list)
        else:
            print("Please provide a search phrase.")

    elif action == Action.SUGGEST:
        print("Suggested models:")
        print_string_list(mlx_hub.suggest())

    elif action == Action.DOWNLOAD:
        if parameter:
            print(f"Downloading model: {parameter}")
            if mlx_hub.download(parameter):
                print("Model downloaded successfully.")
            else:
                print("Model not found.")
        else:
            print("Please provide a Model ID.")

    elif action == Action.DELETE:
        if parameter:
            print(f"Deleting model: {parameter}")
            if mlx_hub.delete(parameter):
                print("Model deleted successfully.")
            else:
                print("Model not found.")
        else:
            print("Please provide a Model ID.")

    elif action == Action.START:
        print("Starting interactive mode.")
        execute_action(Action.HELP)
        start_interactive_mode()

    elif action == Action.EXIT:
        print("Goodbye!")
        return False

    elif action == Action.LOGIN:
        print_action_login_help()

    elif action == Action.HELP:
        print_action_help()

    else:
        print("Invalid action!\n")
        print_action_help()

    print()
    return True


def start_interactive_mode():
    """Starts the interactive mode, prompting the user for actions."""

    running = True
    while running:
        # Get user input
        user_input = input("Enter Action > ").strip().split(sep=" ", maxsplit=1)
        if not user_input:
            continue

        # Validate action
        try:
            action = Action(user_input[0])
            if not action.interactive:
                action = Action.INVALID

        except ValueError:
            action = Action.INVALID

        # Execute action
        parameter = user_input[1] if len(user_input) > 1 else None
        running = execute_action(action, parameter)


def main():
    """Main function to parse arguments and execute corresponding actions."""
    parser = argparse.ArgumentParser(description='MLX-Hub CLI')
    parser.add_argument(
        Action.START.option,
        action='store_true',
        help=Action.START.description
    )
    parser.add_argument(
        Action.SCAN.option,
        action='store_true',
        help=Action.SCAN.description
    )
    parser.add_argument(
        Action.SEARCH.option,
        type=str,
        metavar=Action.SEARCH.parameter,
        help=Action.SEARCH.description
    )
    parser.add_argument(
        Action.SUGGEST.option,
        action='store_true',
        help=Action.SUGGEST.description
    )
    parser.add_argument(
        Action.DOWNLOAD.option,
        type=str,
        metavar=Action.DOWNLOAD.parameter,
        help=Action.DOWNLOAD.description
    )
    parser.add_argument(
        Action.DELETE.option,
        type=str,
        metavar=Action.DELETE.parameter,
        help=Action.DELETE.description
    )

    args = parser.parse_args()

    try:
        if not mlx_hub.has_token():
            execute_action(Action.LOGIN)
        elif args.start:
            execute_action(Action.START)
        elif args.scan:
            execute_action(Action.SCAN)
        elif args.search:
            execute_action(Action.SEARCH, args.search)
        elif args.suggest:
            execute_action(Action.SUGGEST)
        elif args.download:
            execute_action(Action.DOWNLOAD, args.download)
        elif args.delete:
            execute_action(Action.DELETE, args.delete)
        else:
            parser.print_help()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
