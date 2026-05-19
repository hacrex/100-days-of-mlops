#!/bin/bash
# install.sh — Install dependencies for a specific day or all days

set -euo pipefail

usage() {
    echo "Usage: $0 [day-folder]"
    echo ""
    echo "Examples:"
    echo "  $0                          # Install deps for all days"
    echo "  $0 day-001-python-venv      # Install deps for a specific day"
    exit 1
}

install_day() {
    local day_dir="$1"
    local req_file="$day_dir/requirements.txt"

    if [ -f "$req_file" ]; then
        # Skip if requirements.txt only contains a comment
        if grep -qv '^#' "$req_file" 2>/dev/null; then
            echo "==> Installing dependencies for $day_dir..."
            pip install -r "$req_file" --quiet
        else
            echo "    Skipping $day_dir (no real dependencies listed)"
        fi
    fi
}

# Activate venv if it exists
if [ -f ".venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    # shellcheck disable=SC1091
    source venv/bin/activate
fi

if [ $# -eq 0 ]; then
    echo "==> Installing dependencies for all days..."
    for day_dir in days/day-*/; do
        install_day "$day_dir"
    done
    echo "✅ All dependencies installed."
elif [ $# -eq 1 ]; then
    target="days/$1"
    if [ -d "$target" ]; then
        install_day "$target"
        echo "✅ Done."
    else
        echo "Error: Directory '$target' not found."
        usage
    fi
else
    usage
fi
