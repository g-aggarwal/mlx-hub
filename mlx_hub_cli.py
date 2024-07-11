import argparse
from mlx_hub import list_models, scan_models, download_model, delete_model

def main():
    parser = argparse.ArgumentParser(description='MLX Model Manager')
    parser.add_argument('--list', action='store_true', help='List all models avilable to download')
    parser.add_argument('--scan', action='store_true', help='Scan for downloaded models')
    parser.add_argument('--download', type=str, metavar='model_name', help='Download a specific model')
    parser.add_argument('--delete', type=str, metavar='model_name', help='Delete a specific model')
    
    args = parser.parse_args()
    
    if args.list:
        list_models()
    elif args.scan:
        scan_models()
    elif args.download:
        download_model(args.download)
        print(f"Model '{args.download}' downloaded successfully.")
    elif args.delete:
        delete_model(args.delete)
        print(f"Model '{args.delete}' deleted successfully.")
    else:
        print("Invalid option. Use --list, --scan, --download <model_name>, or --delete <model_name>")

if __name__ == "__main__":
    main()