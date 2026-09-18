import torch
import torch.nn as nn


training_data = [
    ([1, 0, 0], 0),
    ([0, 1, 0], 0),
    ([0, 0, 1], 1),
    ([1, 1, 0], 0),
    ([0, 0, 1], 1),
    ([1, 0, 1], 1),
]

X = torch.tensor(
    [item[0] for item in training_data],
    dtype=torch.float32
)

y = torch.tensor(
    [item[1] for item in training_data],
    dtype=torch.float32
).reshape(-1, 1)


class UrgencyModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)


model = UrgencyModel()

loss_function = nn.BCELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)


for epoch in range(500):

    predictions = model(X)

    loss = loss_function(predictions, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()


def predict_urgency(features):

    input_tensor = torch.tensor(
        [features],
        dtype=torch.float32
    )

    prediction = model(input_tensor).item()

    return "urgent" if prediction > 0.5 else "normal"