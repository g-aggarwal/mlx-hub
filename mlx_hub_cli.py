import argparse
from mlx_hub import suggest, find, scan, download, delete
from cli_utils import print_string_list, print_model_list

def main():
    parser = argparse.ArgumentParser(description='MLX Model Manager')
    parser.add_argument('--suggest', action='store_true', help='Suggest some available models to download')
    parser.add_argument('--scan', action='store_true', help='Scan for downloaded models')
    parser.add_argument('--find', type=str, metavar='model_id', help='Check for a specific model')
    parser.add_argument('--download', type=str, metavar='model_id', help='Download a specific model')
    parser.add_argument('--delete', type=str, metavar='model_id', help='Delete a specific model')
    
    args = parser.parse_args()
    
    if args.suggest:
        print("Suggested models")
        print_string_list(suggest())
        
    elif args.scan:
        print("Downloaded models")
        print_model_list(scan())
        
    elif args.find:
        print("Checking for model: " + args.find)
        if find(args.find) is not None:
            print(f"Model found.")
        else:
            print(f"Model not found.")
            
    elif args.download:
        print("Downloding model: " + args.download)
        if download(args.download):
            print(f"Model 'downloaded successfully.")
        else:
            print(f"Model not found.")
            
    elif args.delete:
        print("Deleting model: " + args.delete)
        if delete(args.delete):
            print(f"Model deleted successfully.")
        else:
            print(f"Model not found.")
            
    else:
        print("Invalid option.")
        print("Use --help, --suggest, --scan, --find <model_name>, --download <model_name>, or --delete <model_name>")


if __name__ == "__main__":
    main()