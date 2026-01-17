---
title: "Computer Vision: Seeing the World"
description: "CNNs, Object Detection, and Image Segmentation."
---

# Computer Vision

How do we process images? We can't just flatten them into a vector because we lose spatial structure.

## Convolutional Neural Networks (CNNs)

The workhorse of CV.
*   **Convolution**: A filter slides over the image to detect features (edges, textures).
*   **Pooling**: Reduces the size of the image (downsampling) to make computation efficient.

## Modern Architectures

*   **ResNet**: Uses skip connections to train very deep networks.
*   **YOLO (You Only Look Once)**: Real-time object detection.
*   **ViT (Vision Transformer)**: Applying Transformers to images.

See `code/cnn_mnist.py` (simulated structure) for a basic CNN example.
