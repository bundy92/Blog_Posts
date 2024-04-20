# tests/test_fractal_gan/test_discriminator.py
import pytest
import torch
from sources.discriminator import Discriminator

@pytest.fixture
def discriminator():
    return Discriminator()

def test_discriminator_forward_pass(discriminator):
    # Generate fake image batch
    batch_size = 32
    fake_images = torch.randn(batch_size, 3, 256, 256)

    # Pass fake images through the discriminator
    outputs = discriminator(fake_images)

    # Assertions
    assert isinstance(outputs, torch.Tensor)
    assert outputs.shape == (batch_size, 1)
    assert torch.all(outputs >= 0.0) and torch.all(outputs <= 1.0)
