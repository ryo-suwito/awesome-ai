import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # 1 input channel (grayscale), 32 output channels, 3x3 kernel
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        # 9216 = 64 * 12 * 12 (calculated from input dims)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10) # 10 classes for MNIST digits

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

def run_cnn_stub():
    print("--- Simple CNN Architecture ---")
    model = SimpleCNN()
    print(model)

    # Dummy input: Batch size 1, 1 Channel, 28x28 Image
    dummy_input = torch.randn(1, 1, 28, 28)
    output = model(dummy_input)
    print(f"Output shape: {output.shape} (Expected 1x10)")

if __name__ == "__main__":
    run_cnn_stub()
