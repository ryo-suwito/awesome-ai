---
title: "Math for Machine Learning: The Essentials"
description: "A crash course in the Linear Algebra and Calculus you actually need."
---

# Math for Machine Learning: The Essentials

Don't panic. You don't need a PhD in Mathematics. You just need to understand the "why" behind the algorithms.

## 1. Linear Algebra: The Engine of AI

Everything in AI is a number. An image is a grid of numbers. Text is converted into vectors of numbers.

*   **Scalar**: A single number ($x$).
*   **Vector**: A list of numbers ($\mathbf{v}$).
*   **Matrix**: A 2D grid of numbers ($\mathbf{A}$).
*   **Tensor**: N-dimensional grid (e.g., a batch of color images is 4D: Batch x Height x Width x Channels).

### Dot Product
The measure of similarity between two vectors. This is the core of "Attention" mechanisms in Transformers.

$$ \mathbf{a} \cdot \mathbf{b} = \sum a_i b_i $$

## 2. Calculus: How Machines Learn

Machine learning is basically optimization: minimizing error.

*   **Loss Function**: How wrong is the model?
*   **Derivative**: Which direction should we nudge parameters to reduce error?
*   **Gradient Descent**: The algorithm that iteratively updates parameters.

## 3. Probability: Handling Uncertainty

Real-world data is noisy.

*   **Conditional Probability $P(A|B)$**: The probability of A given B has happened.
*   **Bayes' Theorem**: Updating beliefs based on new evidence.
