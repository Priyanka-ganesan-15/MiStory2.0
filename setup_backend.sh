#!/bin/bash

echo "🚀 Creating MiStory backend structure..."

mkdir -p backend/app/core
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/app/services
mkdir -p backend/app/api/routes

# Core files
touch backend/app/main.py
touch backend/app/core/config.py

# Models
touch backend/app/models/patient.py
touch backend/app/models/entry.py

# Schemas
touch backend/app/schemas/entry.py

# Services
touch backend/app/services/extractor.py

# API routes
touch backend/app/api/routes/entry.py

echo "✅ Backend structure created successfully!"
echo "👉 Next: create venv + install dependencies"