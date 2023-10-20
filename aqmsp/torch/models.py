import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):
    """Multi-layer perceptron (MLP)

    Args:
        input_dim (int): Input dimension
        output_dim (int): Output dimension
        hidden_dims (list): List of hidden layer sizes
        activation (nn.Module): Activation function

    Examples:
        >>> model = MLP(2, 1, [10, 10], nn.ReLU())
        >>> model(torch.randn(10, 2)).shape
        torch.Size([10, 1])
    """

    def __init__(self, input_dim: int, output_dim: int, hidden_dims: list, activation: nn.Module):
        super().__init__()
        layers = []
        layers.append(nn.Linear(input_dim, hidden_dims[0]))
        layers.append(activation)
        for i in range(len(hidden_dims) - 1):
            layers.append(nn.Linear(hidden_dims[i], hidden_dims[i + 1]))
            layers.append(activation)
        layers.append(nn.Linear(hidden_dims[-1], output_dim))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)


class SIREN(nn.Module):
    """Sinusoidal Representation Network (SIREN). See https://arxiv.org/abs/2006.09661 (Implicit Neural Representations with Periodic Activation Functions by Sitzmann et al.)

    Args:
        input_dim (int): Input dimension
        output_dim (int): Output dimension
        hidden_dims (list): List of hidden layer sizes
        activation_scale (float, optional): Scale of the activation function. Defaults to 30.0.
        dropout (float, optional): Dropout rate. Defaults to 0.0.

    Examples:
        >>> model = SIREN(2, 1, [10, 10])
        >>> model(torch.randn(10, 2)).shape
        torch.Size([10, 1])
    """

    def __init__(
        self, input_dim: int, output_dim: int, hidden_dims: list, activation_scale: float = 30.0, dropout: float = 0.0
    ):
        super().__init__()

        self.activation_scale = activation_scale
        self.dropout = dropout

        self.input_layer = nn.Linear(input_dim, hidden_dims[0])
        self.hidden_layers = nn.ModuleList(
            [nn.Linear(hidden_dims[i], hidden_dims[i + 1]) for i in range(len(hidden_dims) - 1)]
        )
        self.output_layer = nn.Linear(hidden_dims[-1], output_dim)

        # Initialize weights
        self._initialize(activation_scale)

    def forward(self, x):
        out = self.input_layer(x)
        out = torch.sin(self.activation_scale * out)
        for layer in self.hidden_layers:
            out = layer(out)
            out = torch.sin(self.activation_scale * out)
            out = F.dropout(out, p=self.dropout, training=self.training)
        out = self.output_layer(out)
        return out

    def _initialize(self, activation_scale):
        def first_layer_init(m):
            if hasattr(m, "weight"):
                input_size = m.weight.size(-1)
                m.weight.uniform_(-1 / input_size, 1 / input_size)

        def other_layer_init(m):
            if hasattr(m, "weight"):
                input_size = m.weight.size(-1)
                m.weight.uniform_(
                    -np.sqrt(6 / input_size) / activation_scale, np.sqrt(6 / input_size) / activation_scale
                )

        with torch.no_grad():
            self.input_layer.apply(first_layer_init)
            self.hidden_layers.apply(other_layer_init)
            self.output_layer.apply(other_layer_init)
