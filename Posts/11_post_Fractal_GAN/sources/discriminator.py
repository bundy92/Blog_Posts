import torch
import torch.nn as nn

class Discriminator(nn.Module):
    """Class for discriminating between real and generated fractal patterns."""

    def __init__(self) -> None:
        """Initialize the Discriminator object."""
        super(Discriminator, self).__init__()

        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.4),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.4),
            nn.Flatten(),
            nn.Linear(128 * 64 * 64, 1),
            nn.Sigmoid()
        )

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        """
        Discriminate between real and generated fractal patterns.

        Parameters:
        - images (torch.Tensor): Tensor of fractal patterns with shape (batch_size, 3, 256, 256).

        Returns:
        - torch.Tensor: Tensor of discrimination scores with shape (batch_size,).
        """
        return self.model(images)
