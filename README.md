# mlops-bullshitery

A small MLOps playground around CIFAR-10 image classification.

## What this repo is

This repository combines model experimentation, model artifacts, data versioning, and lightweight serving in one place:

- **Training / exploration notebooks** in `/notebooks` for CIFAR-10 work
- **Tracked dataset** using **DVC** (`data.dvc` with remote storage configured in `.dvc/config`)
- **Saved model artifacts** in `/models/cifar10` (PyTorch, TorchScript, and ONNX)
- **Inference service** in `service.py` using **BentoML** and an ONNX model

## Main files and folders

- `notebooks/explore-data.ipynb` – data exploration
- `notebooks/cifar10-classification.ipynb` – classification experimentation/training workflow
- `models/cifar10/` – exported model files
- `service.py` – BentoML service with a `predict` API
- `data.dvc` and `.dvc/config` – DVC tracking + remote config
- `requirements.txt` – Python dependencies
- `gpu-setup.sh` – helper script for setting up a GPU-ready environment

## Quick start

1. Create and activate a Python environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Pull versioned data (after configuring required DVC/S3 credentials):
   - `dvc pull`
4. Run or adapt notebooks in `/notebooks`.
5. Serve the model API with BentoML from `service.py`.

## Notes

- DVC remote credentials are expected via environment variables referenced in `.dvc/config`.
- This appears to be an experimental/personal project rather than a production-hardened service.
