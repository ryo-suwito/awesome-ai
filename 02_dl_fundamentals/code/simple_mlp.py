import torch
import torch.nn as nn
import torch.optim as optim

# Define the Model
class SimpleMLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleMLP, self).__init__()
        # Layer 1: Linear transformation
        self.fc1 = nn.Linear(input_size, hidden_size)
        # Activation: ReLU
        self.relu = nn.ReLU()
        # Layer 2: Output
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def run_pytorch_example():
    print("--- PyTorch Simple MLP Example ---")

    # Hyperparameters
    input_size = 10
    hidden_size = 20
    output_size = 1
    learning_rate = 0.01

    # Initialize Model, Loss, Optimizer
    model = SimpleMLP(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    # Dummy Data
    inputs = torch.randn(5, input_size)
    targets = torch.randn(5, output_size)

    # Training Step
    print("Training step...")

    # 1. Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)

    # 2. Backward pass
    optimizer.zero_grad()
    loss.backward()

    # 3. Update weights
    optimizer.step()

    print(f"Loss: {loss.item():.4f}")
    print("Model updated successfully.")

if __name__ == "__main__":
    run_pytorch_example()
