import numpy as np
import torchvision.transforms as transforms
import PIL.Image as PILImage

"""
Метрика
"""
def calc_rgb_psnr(pred: np.ndarray, target: np.ndarray) -> float:
    mse = ((pred - target) ** 2).mean()
    return 20 * (np.log10(255) - 0.5 * np.log10(mse))


"""
Масштабирование изображений
"""
def scale_image(
        img: PILImage.Image,
        new_size: int=256
) -> PILImage.Image:
    width, height = img.size
    max_dim = max(width, height)
    scale = new_size / max_dim
    new_width, new_height = int(width * scale), int(height * scale)

    resize_transform = transforms.Resize((new_height, new_width))

    padding_right = max(new_size - new_width, 0)  # padding for the right
    padding_bottom = max(new_size - new_height, 0)  # padding for the bottom
    pad_transform = transforms.Pad(padding=(0, 0, padding_right, padding_bottom), fill=0, padding_mode='constant')

    transform = transforms.Compose([resize_transform, pad_transform])
    resized_image = transform(img)
    return resized_image