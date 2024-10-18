import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
from model import load_model, preprocess_image, enhance_image
from utils import log_action, handle_errors
import tensorflow as tf

class ImageClassifierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Classifier App")
        self.geometry("500x500")
        self.configure(bg='lightblue')

        # Load model
        self.model = load_model()

        self.__image_label = None
        self.__file_path = None
        self.create_widgets()

    def create_widgets(self):
        """Create buttons and image display label."""
        self.__create_upload_button()
        self.__create_classify_button()
        self.__create_image_display()

    def __create_upload_button(self):
        """Private method for upload button."""
        upload_btn = Button(self, text="Upload Image", command=self.upload_image)
        upload_btn.pack(pady=10)

    def __create_classify_button(self):
        """Private method for classify button."""
        classify_btn = Button(self, text="Classify Image", command=self.classify_image)
        classify_btn.pack(pady=10)

    def __create_image_display(self):
        """Private method for image display."""
        self.__image_label = Label(self)
        self.__image_label.pack(pady=10)

    @log_action
    def upload_image(self):
        """Handles image upload functionality."""
        self.__file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.__file_path:
            img = Image.open(self.__file_path)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.__image_label.configure(image=img_tk)
            self.__image_label.image = img_tk

             # Clear any previous result when a new image is uploaded
            if self.__result_label is not None:
                self.__result_label.destroy()
                self.__result_label = None

    @log_action
    @handle_errors
    def classify_image(self):
        """Handles image classification."""
        if self.__file_path:
            preprocessed_image = preprocess_image(self.__file_path)
            predictions = self.model.predict(preprocessed_image)
            decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
            label = decoded_predictions[0][1]
            confidence = decoded_predictions[0][2]
            self.display_result(label, confidence)
        else:
            self.display_result("No image selected", 0)

    def display_result(self, label, confidence):
        """Displays classification result."""
        result_text = f"Prediction: {label}\nConfidence: {confidence:.2f}"
        result_label = Label(self, text=result_text, bg="lightblue")
        result_label.pack(pady=20)

