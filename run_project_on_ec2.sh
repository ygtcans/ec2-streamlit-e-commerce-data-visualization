#!/bin/bash

# Update and install required packages
echo "Updating system and installing required packages..."
sudo apt update && sudo apt-get update
sudo apt install -y git curl unzip tar make sudo vim wget python3-pip python3-venv

# Clone the repository
REPO_URL="https://github.com/ygtcans/E-Commerce-Data-Visualization"  # Replace this with your repository URL
echo "Cloning the repository from $REPO_URL..."
git clone "$REPO_URL"

# Navigate to the project directory (replace with your project folder name)
PROJECT_DIR="E-Commerce-Data-Visualization"  # Replace with your actual folder name
cd "$PROJECT_DIR" || { echo "Failed to navigate to project directory."; exit 1; }

# Create and activate a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies in the virtual environment
echo "Installing Python dependencies in the virtual environment..."
pip install --upgrade pip
pip install -r requirements.txt

# Ask user whether to run temporarily or permanently
echo "How would you like to run the project?"
echo "1. Temporary running (will stop when you close the terminal)"
echo "2. Permanent running (will continue running in the background)"
read -p "Choose an option (1/2): " RUN_OPTION

if [ "$RUN_OPTION" -eq 1 ]; then
    echo "Starting the Streamlit app temporarily..."
    python -m streamlit run app.py
elif [ "$RUN_OPTION" -eq 2 ]; then
    echo "Starting the Streamlit app permanently in the background..."
    nohup python -m streamlit run app.py &
    echo "App is now running in the background. Use 'ps aux | grep streamlit' to find the process."
else
    echo "Invalid option. Exiting."
    deactivate  # Deactivate the virtual environment
    exit 1
fi

# Deactivate the virtual environment after execution
deactivate
