import numpy as np
from PIL import Image
import os

class Dataset:
    """Class for loading and preprocessing the fractal dataset."""

    def __init__(self, data_dir: str) -> None:
        """
        Initialize the Dataset object.

        Parameters:
        - data_dir (str): Directory containing the fractal dataset.
        """
        self.data_dir = data_dir
        self.images = None
        self.load_dataset()

    def load_dataset(self) -> None:
        """Load and preprocess the fractal dataset."""
        self.images = self.load_images()

    def load_images(self) -> np.ndarray:
        """Load fractal images from the specified directory."""
        images = []
        for filename in os.listdir(self.data_dir):
            img = Image.open(os.path.join(self.data_dir, filename))
            img = img.resize((256, 256))  # Resize images to 256x256 pixels
            img = np.array(img) / 255.0   # Normalize pixel values
            images.append(img)
        return np.array(images)

    def get_batch(self, batch_size: int) -> np.ndarray:
        """
        Get a batch of images from the dataset.

        Parameters:
        - batch_size (int): Number of images in the batch.

        Returns:
        - np.ndarray: Batch of images with shape (batch_size, height, width, channels).
        """
        indices = np.random.choice(len(self.images), batch_size, replace=False)
        return self.images[indices]
