---
title: "The Transformer Architecture"
description: "Attention is All You Need."
---

# The GenAI Revolution: Transformers

In 2017, the paper "Attention is All You Need" changed everything.

## The Problem with RNNs
Previous models (RNNs/LSTMs) processed text sequentially (word by word). This was slow and hard to parallelize. They also forgot long-term context.

## The Solution: Attention
The Transformer looks at the *entire* sentence at once. The "Self-Attention" mechanism allows the model to weigh the importance of each word relative to every other word.

## GPT (Generative Pre-trained Transformer)
*   **Decoder-only** architecture.
*   Predicts the next token based on previous tokens.

## BERT (Bidirectional Encoder Representations from Transformers)
*   **Encoder-only** architecture.
*   Good for understanding/classification, not generation.

See `code/huggingface_inference.py` to run a Transformer locally.
