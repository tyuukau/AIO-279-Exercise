import torch
import torch.nn as nn

from typing import override


class Softmax(nn.Module):
    """
    A custom implementation of the Softmax activation function.
    """

    def __init__(self) -> None:
        super(Softmax, self).__init__()

    @override
    def forward(self, x):
        """
        Forward pass of the Softmax activation function.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The output tensor after applying the Softmax function.
        """
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    def __init__(self) -> None:
        super(SoftmaxStable, self).__init__()

    @override
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass of the numerically stable Softmax activation function.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The output tensor after applying the numerically stable Softmax function.
        """
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        return exp_x / torch.sum(exp_x)
