# Image Classifier App

This is a Python-based desktop application that uses a pre-trained deep learning model (EfficientNetB7) to classify images. The app allows users to upload images, processes them using the model, and displays the predicted class along with its confidence score.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Explanation of the Code](#explanation-of-the-code)

## Installation

Before you get started, make sure you have Python 3.8+ installed on your system. The application also requires some Python packages which can be installed using `pip`.

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/kedharreddy66/HIT137-Assignment-3.git
cd (path)/HIT137-Assignment-3/image_classifier_app
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to isolate dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install the Required Packages

Make sure you have `pip` installed and run:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Once the dependencies are installed, you can run the application:
```bash
python main.py
```

## Usage

1. **Upload an Image**: Click on the **Upload Image** button to select an image file from your system. Supported formats are JPG, PNG, and JPEG.
2. **Classify Image**: Once the image is uploaded, click on the **Classify Image** button. The app will process the image and display the predicted label and confidence score.
3. **Clear Previous Results**: Uploading a new image will automatically clear previous results.

## How It Works

### Step-by-Step Functionality
1. **Load the Model**:
   - The app loads the pre-trained EfficientNetB7 model from TensorFlow’s `keras.applications` module.
2. **Upload an Image**:
   - The user selects an image, which is displayed in the GUI using `PIL` (Pillow) for thumbnail generation and Tkinter for display.
3. **Preprocess the Image**:
   - The uploaded image is processed: it is resized, converted to RGB (if necessary), and enhanced (contrast, brightness, and sharpness).
   - The image is then reshaped and normalized to match the input format expected by EfficientNetB7.
4. **Classify the Image**:
   - The processed image is passed through the model, which outputs the predicted label and confidence score.
   - The result is displayed in the GUI.
5. **Clear Previous Results**:
   - When a new image is uploaded, any previous results are cleared from the GUI to keep it clean and up-to-date.

## Explanation of the Code

### Code Structure
- **`main.py`**: The entry point of the application. It initializes the GUI and starts the main loop.
- **`gui.py`**: Manages the user interface using Tkinter. It handles image uploads, displays images, and shows classification results. It also manages user interactions and updates the screen when new images are uploaded.
- **`model.py`**: Contains the functions to load the model and preprocess images. It handles:
  - Loading the EfficientNetB7 model pre-trained on ImageNet.
  - Enhancing and resizing images to match the model's requirements.
  - Preparing the image data for classification.
- **`utils.py`**: Contains utility functions, such as decorators for logging and error handling.

### How the Code Works
1. **Model Loading** (`load_model` function in `model.py`):
   - The EfficientNetB7 model is loaded using TensorFlow's Keras API. It is pre-trained on the ImageNet dataset and used for inference.
2. **Image Preprocessing** (`preprocess_image` function in `model.py`):
   - This function handles image resizing, color conversion, and enhancement. It ensures the image matches the model's expected input shape of `(600, 600, 3)` for EfficientNetB7.
   - It includes filters for brightness, contrast, and sharpness to improve the image quality before feeding it into the model.
3. **User Interface** (`ImageClassifierApp` class in `gui.py`):
   - The GUI is built using Tkinter and allows the user to upload an image, classify it, and view the results. It maintains a clean interface by clearing previous results when a new image is uploaded.
4. **Classification** (`classify_image` method in `gui.py`):
   - The selected image is preprocessed, passed through the model, and the top prediction is decoded and displayed with the confidence score.

The app integrates image processing, model inference, and GUI management seamlessly to provide an interactive image classification experience.
