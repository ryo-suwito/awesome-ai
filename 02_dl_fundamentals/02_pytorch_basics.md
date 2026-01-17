---
title: "PyTorch Basics: The Framework of Choice"
description: "Why research loves PyTorch and how to use it."
---

# PyTorch Basics

PyTorch is dynamic and pythonic. It uses **Tensors** which are like NumPy arrays but run on GPUs.

## Tensors

```python
import torch

# Create a tensor
x = torch.tensor([1, 2, 3])

# Move to GPU (if available)
if torch.cuda.is_available():
    x = x.to('cuda')
```

## Autograd

PyTorch's superpower. It tracks every operation on tensors to automatically calculate gradients (derivatives) for backpropagation.

```python
x = torch.tensor(1.0, requires_grad=True)
y = 2 * x**2
y.backward()
print(x.grad) # Output: 4.0 (derivative of 2x^2 at x=1 is 4x -> 4)
```

See `code/simple_mlp.py` for a full training loop example.
