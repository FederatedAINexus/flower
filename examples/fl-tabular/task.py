import torch.nn as nn
from flwr_datasets import FederatedDataset
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.optim as optim
from collections import OrderedDict


def load_data(partition_id: int, fds: FederatedDataset):
    train_split = fds.load_split("train").with_format("pandas")[:]
    cat_features = train_split.select_dtypes(include=["object"]).columns.values
    categories = [pd.unique(train_split[cat]).tolist() for cat in cat_features]

    dataset = fds.load_partition(partition_id, "train").with_format("pandas")[:]
    dataset["income"] = dataset["income"].apply(lambda x: 1 if x == ">50K" else 0)

    X = dataset.drop("income", axis=1)
    y = dataset["income"]

    # One-hot Encoding
    categorical_cols = X.select_dtypes(include=["object"]).columns
    categories_for_encoder = []
    for cat_col in categorical_cols:
        # Find the index of the categorical column in cat_features
        cat_index = list(cat_features).index(cat_col)
        categories_for_encoder.append(categories[cat_index])

    encoder = OneHotEncoder(
        sparse_output=False, handle_unknown="ignore", categories=categories_for_encoder
    )
    X_encoded = pd.DataFrame(encoder.fit_transform(X[categorical_cols]))
    X_encoded.columns = encoder.get_feature_names_out(categorical_cols)
    X = pd.concat([X.drop(categorical_cols, axis=1), X_encoded], axis=1)

    split_index = int(0.8 * len(X))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).unsqueeze(1)
    X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).unsqueeze(1)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    return train_loader, test_loader


class IncomeClassifier(nn.Module):
    def __init__(self):
        super(IncomeClassifier, self).__init__()
        self.layer1 = None
        self.layer2 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        if self.layer1 is None:
            self.initialize_model(x.size(1))
        x = self.relu(self.layer1(x))
        x = self.dropout(x)
        x = self.relu(self.layer2(x))
        x = self.dropout(x)
        x = self.sigmoid(self.output(x))
        return x

    def initialize_model(self, input_dim):
        self.layer1 = nn.Linear(input_dim, 128)


def train(model, train_loader, num_epochs=1):
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0001)
    model.train()
    for epoch in range(num_epochs):
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()


def evaluate(model, test_loader):
    model.eval()
    criterion = nn.BCELoss()
    loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            outputs = model(X_batch)
            batch_loss = criterion(outputs, y_batch)
            loss += batch_loss.item()
            predicted = (outputs > 0.5).float()
            total += y_batch.size(0)
            correct += (predicted == y_batch).sum().item()
    accuracy = correct / total
    loss = loss / len(test_loader)
    return loss, accuracy


def set_weights(net, parameters):
    params_dict = zip(net.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
    net.load_state_dict(state_dict, strict=True)


def get_weights(net):
    ndarrays = [val.cpu().numpy() for _, val in net.state_dict().items()]
    return ndarrays
