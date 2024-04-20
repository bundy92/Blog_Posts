import torch
import torch.nn as nn

class Generator(nn.Module):
    """Class for generating fractal patterns using a neural network."""

    def __init__(self, latent_dim: int) -> None:
        """
        Initialize the Generator object.

        Parameters:
        - latent_dim (int): Dimensionality of the latent space.
        """
        super(Generator, self).__init__()
        self.latent_dim = latent_dim

        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 256 * 256 * 3),
            nn.Sigmoid(),
            nn.Unflatten(1, (3, 256, 256))
        )

    def forward(self, noise: torch.Tensor) -> torch.Tensor:
        """
        Generate fractal patterns from latent vectors.

        Parameters:
        - noise (torch.Tensor): Tensor of latent vectors with shape (batch_size, latent_dim).

        Returns:
        - torch.Tensor: Tensor of generated fractal patterns with shape (batch_size, 3, 256, 256).
        """
        return self.model(noise)
