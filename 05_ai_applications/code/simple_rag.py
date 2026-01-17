# Pseudocode / Simplified Python implementation of RAG logic

class SimpleVectorDB:
    def __init__(self):
        self.data = [] # List of (vector, text) tuples

    def add(self, text, vector):
        self.data.append((vector, text))

    def search(self, query_vector):
        # Basic cosine similarity search
        best_score = -1
        best_text = ""
        for vec, text in self.data:
            # Dot product as similarity proxy
            score = sum(a*b for a, b in zip(vec, query_vector))
            if score > best_score:
                best_score = score
                best_text = text
        return best_text

def run_simple_rag():
    print("--- Simple RAG Simulation ---")

    db = SimpleVectorDB()

    # Mock Embeddings (2 dimensions for simplicity)
    # "Cat" -> [1, 0]
    # "Dog" -> [0, 1]

    print("Indexing data...")
    db.add("Cats are independent animals.", [1.0, 0.1])
    db.add("Dogs are loyal companions.", [0.1, 1.0])

    query = "Tell me about felines."
    query_vec = [0.9, 0.2] # Close to "Cat"

    print(f"Querying: '{query}'")
    retrieved_context = db.search(query_vec)

    print(f"Retrieved Context: {retrieved_context}")

    print("Next Step: Pass this context to an LLM for final answer generation.")

if __name__ == "__main__":
    run_simple_rag()
