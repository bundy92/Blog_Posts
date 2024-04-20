# tests/test_fractal_gan/test_generator.py
import pytest
import numpy as np
import torch
from sources.generator import Generator

@pytest.fixture
def generator():
    return Generator(latent_dim=100)

def test_generate(generator):
    # Generate fractal patterns from random latent vectors
    num_samples = 10
    latent_vectors = torch.randn(num_samples, generator.latent_dim, 1, 1)
    generated_images = generator.generate(latent_vectors)

    # Assertions
    assert isinstance(generated_images, torch.Tensor)
    assert generated_images.shape == (num_samples, 3, 256, 256)
    assert torch.all(generated_images >= 0.0) and torch.all(generated_images <= 1.0)
