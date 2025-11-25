import os

# Define workflow content
workflow_content = """name: CI Pipeline

on:
  push:
    branches:
      - main
      - task-1
      - task-2
      - task-3
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run tests
        run: |
          if [ -f pytest.ini ] or [ -d tests ]; then pytest; else echo "No tests found"; fi

      - name: Lint code with flake8
        run: |
          if [ -f requirements.txt ]; then pip install flake8; fi
          flake8 .
"""

# Ensure directory exists
os.makedirs(".github/workflows", exist_ok=True)

# Write the YAML file
with open(".github/workflows/ci.yml", "w") as f:
    f.write(workflow_content)

print("✅ .github/workflows/ci.yml has been generated!")
