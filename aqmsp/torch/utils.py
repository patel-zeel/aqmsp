import torch
from tqdm import tqdm


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def train(model, inputs, output, loss_fn, lr, n_epochs):
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    losses = []
    pbar = tqdm(range(n_epochs))
    for _ in pbar:
        optimizer.zero_grad()
        pred = model(inputs)
        loss = loss_fn(pred, output)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        pbar.set_description(f"Loss: {loss.item():.4f}")

    return losses
