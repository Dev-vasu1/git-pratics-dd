name: My First Workflow

on:
  pull:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Print message
        run: echo "Hello DevOps Engineer"

      - name: Check Python version
        run: python --version
