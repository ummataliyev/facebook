#!/bin/bash

# Install git
apt-get update && apt-get install -y git

# Run Django migrations
python3 manage.py migrate

# Start the Django server
python3 manage.py runserver 0.0.0.0:8000

# Execute additional commands if needed
exec "$@"
