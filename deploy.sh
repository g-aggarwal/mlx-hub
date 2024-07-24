# Determine the repository based on the argument
if [ -n "$1" ] && [ "$1" = "--prod" ]; then
    deployment_environment="prod"
    repo="pypi"
else
    repo="testpypi"


fi

echo "Environment: $deployment_environment"
echo "Using repository: $repo"

# Clean up old build artifacts
echo "Cleaning up old build artifacts..."
rm -rf build dist src/*.egg-info $venv_dir

# Set up virtual environment
python3.10 -m venv "$venv_dir"
check_command "Virtual environment creation"

# Activate the virtual environment
source "$venv_dir/bin/activate"
echo "Virtual environment activated."

# Install dependencies
pip install build twine pytest
check_command "Dependencies installation"

# Build
echo "Building the package..."
python -m build
check_command "Build"

# Upload to the specified repository
echo "Uploading to $repo..."
if [ "$deployment_environment" = "prod" ]; then
    twine upload dist/*
else
    repo_url="https://test.pypi.org/legacy/"
    twine upload --repository-url "$repo_url" dist/*
fi
check_command "Upload to $repo"

# Waiting for package to be available on the repository
echo "Waiting for package to be available on $repo..."
sleep 30

# Install the package from the specified repository
echo "Installing the package from $repo..."
if [ "$deployment_environment" = "prod" ]; then
    pip install mlx-hub
else
    index_url="https://test.pypi.org/simple/"
    extra_index_url="https://pypi.org/simple/"
    pip install --index-url "$index_url" --extra-index-url "$extra_index_url" mlx-hub
fi
check_command "Package installation"

# Run unit tests
echo "Running unit tests..."
pytest tests
check_command "Unit tests"

# Deactivate the virtual environment
deactivate
echo "Virtual environment deactivated."

# Remove the virtual environment
rm -rf "$venv_dir"
echo "Virtual environment removed."

echo "Script completed successfully!"