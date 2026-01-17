---
title: "Neural Networks: The Brain of AI"
description: "From biological neurons to digital perceptrons."
---

# Neural Networks: Intro

Deep Learning is based on Artificial Neural Networks (ANNs), loosely inspired by the human brain.

## The Perceptron

The simplest unit.
1.  Takes inputs ($x$).
2.  Multiplies by weights ($w$).
3.  Adds a bias ($b$).
4.  Passes through an activation function (e.g., Sigmoid).

$$ y = \sigma(Wx + b) $$

## The Multi-Layer Perceptron (MLP)

Stacking layers of perceptrons allows the model to learn non-linear relationships. This is "Deep" Learning.

## Activation Functions

*   **ReLU (Rectified Linear Unit)**: $f(x) = max(0, x)$. Most common.
*   **Sigmoid**: S-shaped, squashes between 0 and 1. Used for probability.
*   **Softmax**: Used for multi-class classification output.
