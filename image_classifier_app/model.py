from PIL import Image, ImageOps, ImageEnhance
import numpy as np
import tensorflow as tf

def load_model():
    """Load the pre-trained EfficientNetB7 model."""
    try:
        # Load EfficientNetB7 pre-trained on ImageNet
        return tf.keras.applications.EfficientNetB7(weights='imagenet')
    except Exception as e:
        raise RuntimeError("Error loading model. Ensure TensorFlow is installed correctly.") from e

def preprocess_image(image_path):
    """Preprocess the image for classification."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    # Convert to RGB if necessary
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    elif image.mode == 'L':
        image = image.convert('RGB')
    elif image.mode not in ['RGB', 'RGBA']:
        image = image.convert('RGB')

    # Enhance image quality before resizing
    image = enhance_image(image)

    # Center-crop if the image is not square, then resize to 600x600 for EfficientNetB7
    if image.size[0] != image.size[1]:
        image = ImageOps.fit(image, (600, 600), Image.ANTIALIAS, centering=(0.5, 0.5))
    else:
        image = image.resize((600, 600))

    # Convert the image to a numpy array
    image = np.array(image)

    # Check if the image has the right shape after conversion
    if image.shape[-1] != 3:
        print(f"Unexpected number of channels: {image.shape[-1]}. Converting to RGB.")
        image = image[..., :3]

    # Expand dimensions to match the input shape expected by the model (1, 600, 600, 3)
    image = np.expand_dims(image, axis=0)

    # Preprocess the image using the same method as the model
    return tf.keras.applications.efficientnet.preprocess_input(image)

def enhance_image(image):
    """Enhances the image quality by adjusting sharpness, contrast, and brightness."""
    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(1.5)  # Adjust contrast factor as needed

    # Enhance sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    image = sharpness_enhancer.enhance(2.0)  # Adjust sharpness factor as needed

    # Enhance brightness
    brightness_enhancer = ImageEnhance.Brightness(image)
    image = brightness_enhancer.enhance(1.2)  # Adjust brightness factor as needed

    return image
