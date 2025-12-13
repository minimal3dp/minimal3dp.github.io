#!/bin/bash

# Configuration
SOURCE_DIR="m3dp-bridge"
TARGET_DIR="../m3dp-bridge"

# 1. Validation
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Directory '$SOURCE_DIR' not found in current location."
    echo "Please run this script from the root of the minimal3dp.github.io repository."
    exit 1
fi

if [ -d "$TARGET_DIR" ]; then
    echo "Warning: Target directory '$TARGET_DIR' already exists."
    read -p "Do you want to overwrite it? (y/N) " confirm
    if [[ $confirm != [yY] && $confirm != [yY][eE][sS] ]]; then
        echo "Aborting."
        exit 1
    fi
    rm -rf "$TARGET_DIR"
fi

# 2. Extract
echo "📦 Extracting $SOURCE_DIR to $TARGET_DIR..."
cp -r "$SOURCE_DIR" "$TARGET_DIR"

# 3. Initialize New Repository
echo "✨ Initializing new Git repository in $TARGET_DIR..."
cd "$TARGET_DIR" || exit

git init -b main

# Create proper .gitignore for Python/FastAPI
cat > .gitignore << EOL
__pycache__/
*.py[cod]
*$py.class
.env
.venv
env/
venv/
*.db
.DS_Store
.idea/
.vscode/
EOL

# Initial Commit
git add .
git commit -m "feat: Initial commit of M3DP-BRIDGE (extracted from monorepo)"

echo ""
echo "✅ Extraction Complete!"
echo ""
echo "Next Steps:"
echo "1. Verify the new repo:  cd $TARGET_DIR"
echo "2. Create a new repo on GitHub named 'm3dp-bridge'"
echo "3. Link it:  git remote add origin https://github.com/YOUR_USERNAME/m3dp-bridge.git"
echo "4. Push:     git push -u origin main"
echo ""
echo "Once verified, you can delete the 'm3dp-bridge' folder from this repository."
