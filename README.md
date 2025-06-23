# Image Enhancement Project

## Overview
This project implements a deep learning-based image enhancement system that converts low-light, noisy images into high-quality, well-lit images. The system uses a Convolutional Neural Network (CNN) to learn the mapping between low-light, noisy images and their high-light versions. The code is organized into modular Python files for preprocessing, model building, utility functions, evaluation, and execution.

## Functionality
The code performs the following tasks:
- **Preprocessing**: Loads high-light images, reduces their brightness, and adds salt-and-pepper noise to create low-light, noisy versions for training.
- **Model Training**: Trains a CNN to enhance low-light images back to their high-light versions.
- **Evaluation**: Tests the model on a sample image, displaying the original high-light, low-light, and enhanced images, and computes quality metrics (PSNR and SSIM).
- **Visualization**: Displays results for visual comparison.

### Input Image Requirements
- **High-Light Images**: The program expects high-light (well-lit, high-quality) images as input. It artificially creates a low-light, noisy version by reducing brightness and adding noise, then enhances this version back to a high-light image.
- **Low-Light Images**: If you want to enhance a naturally low-light image, modify the `extractTestInput` function in `utils.py` to skip brightness reduction and noise addition (see "Customization" below). Note that the model was trained on low-light images generated from high-light images, so results on naturally low-light images may vary unless the model is retrained.

## Model Architecture
The model is a custom CNN built using Keras with TensorFlow backend. Key features include:
- **Input**: RGB images of size 500x500 pixels.
- **Architecture**: Multiple convolutional branches with ReLU activation, merged using addition layers to combine features.
- **Layers**: Conv2D layers with filter sizes (3x3 and 2x2) and filter counts (16, 32, 64).
- **Output**: Enhanced RGB image of the same size as the input.
- **Loss Function**: Mean Squared Error (MSE) for pixel-wise comparison.
- **Optimizer**: Adam optimizer for efficient training.

## PSNR and SSIM
- **PSNR (Peak Signal-to-Noise Ratio)**: Measures the ratio between the maximum possible power of a signal and the power of corrupting noise. Higher PSNR values (in decibels) indicate better image quality, typically ranging from 20 to 40 dB for good quality.
- **SSIM (Structural Similarity Index)**: Assesses similarity between two images based on luminance, contrast, and structure. SSIM ranges from 0 to 1, where 1 indicates perfect similarity. It aligns better with human visual perception than PSNR.

## Project Structure
The codebase is split into five Python files for modularity:
- `main.py`: Entry point to run the pipeline.
- `preprocess.py`: Handles data loading and preprocessing.
- `model.py`: Defines and builds the CNN model.
- `utils.py`: Contains utility functions (e.g., adding noise, generating inputs).
- `evaluate.py`: Manages model evaluation and metric calculations.

## Installation and Setup
Follow these steps to install dependencies and set up the project environment:

### Prerequisites
- Python 3.8 or higher
- A GPU (optional but recommended for faster training)
- Google Drive access (if using Colab or loading data from Google Drive)
- A directory containing high-light images (e.g., PNG or JPG format)

### Dependencies
Install the required Python packages using pip. Open a terminal and run:

```bash
pip install numpy opencv-python tensorflow keras scikit-image matplotlib tqdm
```