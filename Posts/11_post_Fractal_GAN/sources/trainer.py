import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class Trainer:
    """Class for training the GAN model."""

    def __init__(self, generator: nn.Module, discriminator: nn.Module, dataset: np.ndarray, device: str = 'cpu') -> None:
        """
        Initialize the Trainer object.

        Parameters:
        - generator (nn.Module): Generator model.
        - discriminator (nn.Module): Discriminator model.
        - dataset (np.ndarray): Array of training images with shape (num_samples, 256, 256, 3).
        - device (str): Device to perform computations ('cpu' or 'cuda').
        """
        self.generator = generator.to(device)
        self.discriminator = discriminator.to(device)
        self.dataset = torch.tensor(dataset, dtype=torch.float32).permute(0, 3, 1, 2).to(device)
        self.device = device

        # Define loss function and optimizer
        self.criterion = nn.BCELoss()
        self.optimizer_G = optim.Adam(self.generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
        self.optimizer_D = optim.Adam(self.discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

    def train(self, num_epochs: int, batch_size: int) -> None:
        """
        Train the GAN model.

        Parameters:
        - num_epochs (int): Number of training epochs.
        - batch_size (int): Batch size for training.
        """
        dataloader = DataLoader(TensorDataset(self.dataset), batch_size=batch_size, shuffle=True)

        for epoch in range(num_epochs):
            for i, real_images in enumerate(dataloader):
                # Adversarial ground truths
                real_labels = torch.full((batch_size,), 1.0, device=self.device)
                fake_labels = torch.full((batch_size,), 0.0, device=self.device)

                # Generate fake images
                noise = torch.randn(batch_size, self.generator.latent_dim, 1, 1, device=self.device)
                generated_images = self.generator(noise)

                # Train discriminator
                self.optimizer_D.zero_grad()
                d_loss_real = self.criterion(self.discriminator(real_images.to(self.device)), real_labels)
                d_loss_fake = self.criterion(self.discriminator(generated_images.detach()), fake_labels)
                d_loss = 0.5 * (d_loss_real + d_loss_fake)
                d_loss.backward()
                self.optimizer_D.step()

                # Train generator
                self.optimizer_G.zero_grad()
                g_loss = self.criterion(self.discriminator(generated_images), real_labels)
                g_loss.backward()
                self.optimizer_G.step()

                # Print progress
                print(f"Epoch [{epoch+1}/{num_epochs}], Batch [{i+1}/{len(dataloader)}], D Loss: {d_loss.item()}, G Loss: {g_loss.item()}")
