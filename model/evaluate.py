import cv2 as cv
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from utils import extractTestInput

def evaluateImage(highImagePath, model):
    """Evaluate the model on a test image and display results."""
    highImage = cv.imread(highImagePath)
    highImage = cv.cvtColor(highImage, cv.COLOR_BGR2RGB)
    highImage = cv.resize(highImage, (500, 500))
    
    testInput = extractTestInput(highImagePath)
    prediction = model.predict(testInput)
    prediction = prediction.reshape(500, 500, 3)
    
    # Display images
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title("High Light Image")
    plt.imshow(highImage)
    
    plt.subplot(1, 3, 2)
    plt.title("Low Light Image")
    plt.imshow(testInput.reshape(500, 500, 3))
    
    plt.subplot(1, 3, 3)
    plt.title("Enhanced Image")
    plt.imshow(prediction)
    plt.show()
    
    # Calculate metrics
    psnrValue = psnr(highImage, prediction, data_range=255)
    ssimValue = ssim(highImage, prediction, win_size=7, multichannel=True, data_range=255, channel_axis=2)
    
    print(f"PSNR: {psnrValue}")
    print(f"SSIM: {ssimValue}")