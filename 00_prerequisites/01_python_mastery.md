---
title: "Python Mastery for AI: Beyond the Basics"
description: "Master the Python concepts essential for Data Science and Machine Learning."
---

# Python Mastery for AI: Beyond the Basics

Welcome to the first step of your AI journey! You might already know Python, but "Data Science Python" hits differently. We need speed, efficiency, and vectorization.

## 1. List Comprehensions & Generators

Stop writing `for` loops for simple transformations.

```python
# The Old Way
squares = []
for x in range(10):
    squares.append(x**2)

# The AI Way
squares = [x**2 for x in range(10)]
```

For large datasets, use **Generators** to save memory. They yield items one by one instead of loading everything into RAM.

```python
def large_file_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

## 2. Decorators

You'll see `@torch.no_grad()` or `@app.route()` everywhere. Understand how they work.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Executed in {time.time() - start}s")
        return result
    return wrapper

@timer
def heavy_computation():
    time.sleep(1)

heavy_computation()
```

## 3. Vectorization with NumPy

This is the golden rule of AI programming: **Never iterate over rows if you can vectorize.**

```python
import numpy as np
import time

# Create large arrays
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Slow: Loop
start = time.time()
c = 0
for i in range(len(a)):
    c += a[i] * b[i]
print(f"Loop: {time.time() - start}s")

# Fast: Vectorized Dot Product
start = time.time()
c = np.dot(a, b)
print(f"Vectorized: {time.time() - start}s")
```

See the full example in `code/numpy_basics.py`.
