import numpy as np
import torch
from generator import Generator

# Load the trained Generator model (replace 'generator.pth' with the actual path)
generator = Generator(latent_dim=100)
generator.load_state_dict(torch.load('generator.pth'))
generator.eval()

# Generate latent vectors
num_samples = 10
latent_dim = generator.latent_dim
latent_vectors = torch.randn(num_samples, latent_dim, 1, 1)

# Generate fractal patterns
with torch.no_grad():
    generated_images = generator(latent_vectors)

# Convert generated images to numpy arrays
generated_images = generated_images.cpu().numpy()

# Save generated fractal patterns (adjust file path as needed)
for i, image in enumerate(generated_images):
    np.save(f'generated_fractal_{i}.npy', image)
