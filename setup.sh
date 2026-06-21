#!/bin/bash
# Maestro Full-Stack Prototype Setup Script
# Configures the Python virtual environment using an express copy from the sibling environment,
# falling back to pip installation if unavailable.

set -e # Exit immediately if a command exits with a non-zero status

echo "============================================================="
echo "⚙️  INITIALIZING MAESTRO ENVIRONMENT SETUP"
echo "============================================================="

# Resolve absolute workspace directory
WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$WORKSPACE_DIR"

# 1. Create Python Virtual Environment
echo "Creating Python virtual environment in .venv..."
python3 -m venv .venv

# 2. Check and copy packages from sibling environment (Express Mode)
SIBLING_SITE_PACKAGES="/Users/nitinagga/Documents/pharma-rwe-ge/.venv/lib/python3.14/site-packages"
TARGET_SITE_PACKAGES="$WORKSPACE_DIR/.venv/lib/python3.14/site-packages"

if [ -d "$SIBLING_SITE_PACKAGES" ]; then
    echo "⚡ Sibling virtual environment detected!"
    echo "⚡ Replicating pre-resolved package ledger (Express Copy Mode)..."
    cp -R "$SIBLING_SITE_PACKAGES"/* "$TARGET_SITE_PACKAGES/"
    echo "✅ Replicated site-packages successfully (Saved 10+ minutes of compilation!)."
else
    echo "⚠️ Sibling site-packages not found at $SIBLING_SITE_PACKAGES."
    echo "Falling back to standard network pip installation..."
    
    # Upgrade pip
    echo "Upgrading pip..."
    .venv/bin/python3 -m pip install --upgrade pip

    # Install Python Dependencies from requirements
    echo "Installing package versions from requirements..."
    .venv/bin/pip install -r requirements_pinned.txt --extra-index-url https://pypi.org/simple
fi

# 3. Initialize Local Environment Files
echo "Initializing local environment configuration (.env)..."
cat > .env << EOL
GOOGLE_CLOUD_PROJECT="nitinagga-ge-2"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_USE_VERTEXAI=true
EOL

echo "✅ Environment configuration saved to .env"

# 4. Run Sub-Agent Registration Script
echo "Registering sub-agents..."
chmod +x backend/register_agents.py
.venv/bin/python3 backend/register_agents.py

echo "============================================================="
echo "🎉 SETUP COMPLETED SUCCESSFULLY!"
echo "To launch both backend and frontend servers, run:"
echo "  ./start.sh"
echo "============================================================="
