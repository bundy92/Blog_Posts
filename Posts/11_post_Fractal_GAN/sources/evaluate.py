import numpy as np
import torch
from torchvision.models import inception_v3
from scipy.stats import entropy

# Load the pre-trained Inception model
inception_model = inception_v3(pretrained=True, transform_input=True)
inception_model.eval()

def calculate_inception_score(images, num_splits=10):
    scores = []
    for images_batch in np.array_split(images, num_splits):
        with torch.no_grad():
            preds = inception_model(images_batch)
        preds = torch.nn.functional.softmax(preds, dim=1).cpu().numpy()
        p_y = np.mean(preds, axis=0)
        scores.append(entropy(p_y, base=2))
    return np.exp(np.mean(scores)), np.std(scores)

# Load generated fractal patterns (adjust file paths as needed)
num_samples = 100
generated_images = []
for i in range(num_samples):
    image = np.load(f'generated_fractal_{i}.npy')
    generated_images.append(image)

# Convert to PyTorch tensor and preprocess
generated_images = torch.tensor(generated_images, dtype=torch.float32)
generated_images = generated_images.permute(0, 3, 1, 2)

# Calculate Inception Score
is_mean, is_std = calculate_inception_score(generated_images)
print(f'Inception Score: {is_mean} ± {is_std}')
