# tests/test_fractal_gan/test_utils.py
import pytest
import numpy as np
from sources.utils import preprocess_data

@pytest.fixture
def mock_dataset():
    # Mock dataset (replace with actual dataset loading)
    return np.random.randn(1000, 256, 256, 3)

def test_preprocess_data(mock_dataset):
    # Preprocess the mock dataset
    preprocessed_data = preprocess_data(mock_dataset)

    # Assertions
    assert isinstance(preprocessed_data, np.ndarray)
    assert preprocessed_data.shape == (1000, 3, 256, 256)
    assert np.allclose(preprocessed_data.mean(), 0.0, atol=1e-6)
    assert np.allclose(preprocessed_data.std(), 1.0, atol=1e-6)
