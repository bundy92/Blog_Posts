import numpy as np
import matplotlib.pyplot as plt

# Load generated fractal patterns (adjust file paths as needed)
num_samples = 10
generated_images = []
for i in range(num_samples):
    image = np.load(f'generated_fractal_{i}.npy')
    generated_images.append(image)

# Visualize generated fractal patterns
fig, axes = plt.subplots(1, num_samples, figsize=(15, 3))
for i, image in enumerate(generated_images):
    axes[i].imshow(image.transpose(1, 2, 0))
    axes[i].axis('off')
    axes[i].set_title(f'Fractal {i+1}')

plt.show()
