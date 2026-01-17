import random

# Mocking MLflow for standalone execution without server
class MockMLflow:
    def start_run(self):
        print("MLflow Run Started.")
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MLflow Run Ended.")

    def log_param(self, key, value):
        print(f"Logged Param: {key} = {value}")

    def log_metric(self, key, value):
        print(f"Logged Metric: {key} = {value}")

mlflow = MockMLflow()

def train():
    print("--- Training with Mock Experiment Tracking ---")

    # Hyperparams
    epochs = 5
    lr = 0.01

    with mlflow.start_run():
        mlflow.log_param("epochs", epochs)
        mlflow.log_param("learning_rate", lr)

        for epoch in range(epochs):
            # Simulate training loss
            loss = 1.0 / (epoch + 1) + random.random() * 0.1
            print(f"Epoch {epoch}: Loss {loss:.4f}")
            mlflow.log_metric("loss", loss)

if __name__ == "__main__":
    train()
