import argparse
import mlx_hub
from enum import Enum
from cli_utils import print_string_list, print_repo_list, print_model_list

class Action(Enum):
    HELP = ("help", "Show this help message")
    START = ("start", "Start interactive mode", False)
    SCAN = ("scan", "Scan for downloaded MLX models")
    SEARCH = ("search", "Search for MLX models using a search term")
    SUGGEST = ("suggest", "Suggest MLX models to download")
    DOWNLOAD = ("download", "Download a specific model")
    DELETE = ("delete", "Delete a specific model")
    EXIT = ("exit", "Exit the application")
    INVALID = ("invalid", "Invalid action", False)
    
    def __new__(cls, value, description, is_interactive=True):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.option = "--" + value
        obj.description = description
        obj.interactive = is_interactive
        return obj

def print_action_help():
    """Prints available actions for the interactive mode."""
    print("Available Actions:")
    for action in Action:
        if action.interactive:
            print(f"    {action.value:<15} {action.description}")

def execute_action(action, args=None):
    """Executes the given action with optional arguments."""
    print()
    
    if action == Action.SCAN:
        repo_list = mlx_hub.scan()
        print(f"Downloaded models: {len(repo_list)}")
        print_repo_list(repo_list)
    
    elif action == Action.SEARCH:
        if args:
            models_list = mlx_hub.search(args)
            print(f"Models found: {len(models_list)}")
            print_model_list(models_list)
        else:
            print("Please provide a search term.")
    
    elif action == Action.SUGGEST:
        print("Suggested models:")
        print_string_list(mlx_hub.suggest())
                  
    elif action == Action.DOWNLOAD:
        if args:
            print(f"Downloading model: {args}")
            if mlx_hub.download(args):
                print("Model downloaded successfully.")
            else:
                print("Model not found.")
        else:
            print("Please provide a Repo ID.")
            
    elif action == Action.DELETE:
        if args:
            print(f"Deleting model: {args}")
            if mlx_hub.delete(args):
                print("Model deleted successfully.")
            else:
                print("Model not found.")
        else:
            print("Please provide a Repo ID.")
    
    elif action == Action.START:
        print("Starting interactive mode.")
        execute_action(Action.HELP)
        start_interactive_mode()
        
    elif action == Action.EXIT:
        print("Goodbye!")
        return False
    
    elif action == Action.HELP:
        print_action_help()

    else:
        print("Invalid action.")
        print_action_help()

    print()
    return True

def start_interactive_mode():
    """Starts the interactive mode, prompting the user for actions."""
    running = True
    while running:
        # Get user input
        user_input = input("Enter Action > ").strip().split()
        if not user_input:
            continue
        
        # Validate action
        try:
            action = Action(user_input[0])
            if not action.interactive:
                action = Action.INVALID
            args = user_input[1] if len(user_input) > 1 else None
                   
        except ValueError:
            action = Action.INVALID

        # Execute action
        running = execute_action(action, args)

def main():
    """Main function to parse arguments and execute corresponding actions."""
    parser = argparse.ArgumentParser(description='MLX-Hub CLI')
    parser.add_argument(Action.START.option, action='store_true', help=Action.START.description)
    parser.add_argument(Action.SCAN.option, action='store_true', help=Action.SCAN.description)
    parser.add_argument(Action.SEARCH.option, type=str, metavar='search_term', help=Action.SEARCH.description)
    parser.add_argument(Action.SUGGEST.option, action='store_true', help=Action.SUGGEST.description)
    parser.add_argument(Action.DOWNLOAD.option, type=str, metavar='model_id', help=Action.DOWNLOAD.description)
    parser.add_argument(Action.DELETE.option, type=str, metavar='model_id', help=Action.DELETE.description)
    
    args = parser.parse_args()

    try:
        if args.start:
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
            execute_action(Action.HELP)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()