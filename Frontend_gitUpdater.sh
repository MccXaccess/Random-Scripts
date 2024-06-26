#!/bin/bash

SERVER_FILE="nuxt"
APP_DIR="/home/unix/SERVERS/MindWave-Frontend-Client" 
DEPLOY_KEY="/home/unix/.ssh/fmw.pub"
GIT_CMD="git -C $APP_DIR" 
NPM_CMD="npm"  
NODE_CMD="node"  
BRANCH_NAME="production"
TIME_BETWEEN_CHECKS=900

echo "[+] Starting and deploying SSH KEY"
eval "$(ssh-agent -s)"  
ssh-add $DEPLOY_KEY 

if ! cd "$APP_DIR"; then
    echo "[!] UNABLE TO FIND APP_DIR!"
    exit 1
fi

echo "[~] Fetching latest updates from repo..."
$GIT_CMD fetch origin $BRANCH_NAME

echo "[+] Changing current branch"
git_checkout_output=$($GIT_CMD checkout $BRANCH_NAME)
echo "[+] $git_checkout_output"

echo "[+] Starting NODE server"
$NPM_CMD run dev &

check_and_update() {
    echo "[~] Fetching latest updates from repo..."
    $GIT_CMD fetch origin $BRANCH_NAME
    
    echo "[~] Pulling latest updates from repo..."
    git_pull_output=$($GIT_CMD pull)
    echo "[+] $git_pull_output"

    if [[ ! "$git_pull_output" =~ "Already up to date." ]]; then
        echo "[+] Killing current process"
        lsof -t -i :3000 | xargs kill

        echo "[~] Installing NPM dependencies..."
        $NPM_CMD install --prefix $APP_DIR

        echo "[+] Starting NODE server"
        $NPM_CMD run dev &
    fi
}

while true; do
    check_and_update
    sleep $TIME_BETWEEN_CHECKS
done
