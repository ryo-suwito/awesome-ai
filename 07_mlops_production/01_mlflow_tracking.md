---
title: "MLOps: Productionizing AI"
description: "Tracking, Deploying, and Monitoring."
---

# MLOps: Productionizing AI

Writing code in a notebook is easy. Running it in production at scale is hard.

## Experiment Tracking

You will run hundreds of experiments. Which hyperparameter set was best?
*   **MLflow**: Logs parameters, metrics, and artifacts (models).

## Model Registry

Versioning your models. `v1` is in production, `v2` is in staging.

## Serving

Exposing your model as an API.
*   **FastAPI**: Python standard.
*   **TensorFlow Serving / TorchServe**: Optimized for deep learning.

See `code/train_with_tracking.py` (Mock MLflow).
