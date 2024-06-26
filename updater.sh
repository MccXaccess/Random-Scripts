#!/bin/bash

# Define paths and commands
APP_DIR="/path/to/dir"  # Change this to the directory where your app is located
DEPLOY_KEY="~/.ssh/KEYNAME.PUB"  # Change this to the path of your deploy key file
GIT_CMD="git -C $APP_DIR"  # Run Git commands in the app directory
NPM_CMD="npm"  # Use npm to install dependencies
NODE_CMD="node"  # Use node to start the server
BRANCH_NAME="production"

cd $APP_DIR  # Navigate to the app directory

echo "Stopping running instance of node app..."
pkill node  # Stop any running instances of the node app

# Step 2: Fetch changes from the production branch using deploy key
echo "Fetching changes from production branch..."
eval "$(ssh-agent -s)"  # Start SSH agent
ssh-add $DEPLOY_KEY  # Add deploy key to SSH agent
$GIT_CMD fetch origin $BRANCH_NAME  # Fetch changes from production branch
$GIT_CMD checkout $BRANCH_NAME  # Switch to production branch
$GIT_CMD pull # Apply changes

# Step 3: Install dependencies
echo "Installing npm dependencies..."
$NPM_CMD install --prefix $APP_DIR  # Install dependencies in the app directory

# Step 4: Start the server
echo "Starting node server..."

$NODE_CMD server.js  # Start the server
