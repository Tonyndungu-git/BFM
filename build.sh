#!/usr/bin/env bash
set -o errexit

# Install Python dependencies
pip install -r budget_friendly_movers/requirements.txt

# Collect static files
python budget_friendly_movers/manage.py collectstatic --no-input

# Apply database migrations
python budget_friendly_movers/manage.py migrate
