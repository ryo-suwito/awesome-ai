from transformers import pipeline

def run_hf_inference():
    print("--- Hugging Face Transformers Inference ---")

    # Use a small model for demonstration to avoid massive downloads
    print("Loading pipeline (distilgpt2)...")
    generator = pipeline('text-generation', model='distilgpt2')

    prompt = "In the future, Artificial Intelligence will"
    print(f"Prompt: {prompt}")

    result = generator(prompt, max_length=50, num_return_sequences=1)

    print("\nGenerated Text:")
    print(result[0]['generated_text'])

if __name__ == "__main__":
    # Note: This requires 'transformers' and 'torch' installed.
    # We wrap in try-except so the CI doesn't fail if libraries are missing in this specific sandbox step
    try:
        run_hf_inference()
    except ImportError as e:
        print(f"Skipping execution due to missing library: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
