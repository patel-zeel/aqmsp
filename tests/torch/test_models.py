import torch
import torch.nn as nn
from aqmsp.torch.models import MLP, SIREN


def test_mlp():
    model = MLP(2, 1, [10, 10], nn.ReLU())
    assert model(torch.randn(10, 2)).shape == torch.Size([10, 1])


def test_siren():
    model = SIREN(2, 1, [10, 10])
    assert model(torch.randn(10, 2)).shape == torch.Size([10, 1])
