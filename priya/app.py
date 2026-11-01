name: My First Workflow

on:
  pull:
    branches:
      - mani

jobs:
  build:
    runs-on: linux-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Print message
        run: echo "Hello DevOps Engineer"

      - name: Check Python version
        run: python --version
