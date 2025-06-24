<<<<<<< HEAD
import numpy as np
import cv2 as cv
import os
from tqdm import tqdm
from utils import addNoise

def preprocessData(highPath):
    """Load and preprocess images from the specified directory."""
    imagesLow = []
    imagesHigh = []
    
    for imageName in tqdm(os.listdir(highPath)):
        imagePath = os.path.join(highPath, imageName)
        highImage = cv.imread(imagePath)
        
        if highImage is not None:
            highImage = cv.cvtColor(highImage, cv.COLOR_BGR2RGB)
            highImage = cv.resize(highImage, (500, 500))
            
            hsv = cv.cvtColor(highImage, cv.COLOR_BGR2HSV)
            hsv[..., 2] = hsv[..., 2] * 0.2
            lowImage = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
            noisyImage = addNoise(lowImage)
            
            imagesLow.append(noisyImage)
            imagesHigh.append(highImage)
        else:
            print(f"Failed to load image: {imagePath}")
            
=======
import numpy as np
import cv2 as cv
import os
from tqdm import tqdm
from utils import addNoise

def preprocessData(highPath):
    """Load and preprocess images from the specified directory."""
    imagesLow = []
    imagesHigh = []
    
    for imageName in tqdm(os.listdir(highPath)):
        imagePath = os.path.join(highPath, imageName)
        highImage = cv.imread(imagePath)
        
        if highImage is not None:
            highImage = cv.cvtColor(highImage, cv.COLOR_BGR2RGB)
            highImage = cv.resize(highImage, (500, 500))
            
            hsv = cv.cvtColor(highImage, cv.COLOR_BGR2HSV)
            hsv[..., 2] = hsv[..., 2] * 0.2
            lowImage = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
            noisyImage = addNoise(lowImage)
            
            imagesLow.append(noisyImage)
            imagesHigh.append(highImage)
        else:
            print(f"Failed to load image: {imagePath}")
            
>>>>>>> ccfd08bd8a18241085436d95e8b5b9c291750d03
    return np.array(imagesLow), np.array(imagesHigh)