import numpy as np
import torch
from generator import Generator
from discriminator import Discriminator
from trainer import Trainer

def main() -> None:

    # Load the dataset (replace this with your actual data loading process)
    # Example: dataset = np.load('fractal_dataset.npy')
    dataset = np.random.randn(1000, 256, 256, 3)

    # Define hyperparameters
    latent_dim = 100
    num_epochs = 100
    batch_size = 32
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Create Generator and Discriminator instances
    generator = Generator(latent_dim).to(device)
    discriminator = Discriminator().to(device)

    # Initialize Trainer
    trainer = Trainer(generator, discriminator, dataset, device)

    # Train the GAN model
    trainer.train(num_epochs, batch_size)


if __name__ == "__main__":
    main()