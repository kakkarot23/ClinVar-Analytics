#!/usr/bin/env bash
set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}================================================================================${NC}"
echo -e "${BLUE}EXECUTING MASTER PHASE 01 (ENVIRONMENT & DATASET CHARACTERIZATION) ON UBUNTU${NC}"
echo -e "${BLUE}================================================================================${NC}"

# Activate virtual environment if present
if [ -d ".venv" ]; then
    source .venv/bin/activate
elif [ -f "/home/hp/kind/Excel/sun/bin/activate" ]; then
    source /home/hp/kind/Excel/sun/bin/activate
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

echo -e "${GREEN}[RUNNING] python master_phase_01.py${NC}"
python master_phase_01.py

echo -e "${GREEN}[SUCCESS] Phase_01_Environment_Setup completed cleanly on Ubuntu!${NC}"
