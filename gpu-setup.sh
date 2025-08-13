#!/bin/bash
# System updates
sudo apt update && sudo apt upgrade -y

# Install Python + Pip
sudo apt install -y python3-pip python3-venv git

# Install Docker
sudo apt install -y docker.io
sudo usermod -aG docker $USER

# Install NVIDIA GPU drivers & CUDA toolkit (provider-specific)
# Example for Ubuntu 22.04:
sudo apt install -y nvidia-driver-535 nvidia-cuda-toolkit

# Install ML dependencies
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
pip install mlflow dvc-s3 bentoML kubernetes prometheus_client

# Login to Git (for pulling code)
git config --global user.name "FarerABR"
git config --global user.email "a.baghaee81@outlook.com"
