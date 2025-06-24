<<<<<<< HEAD
import numpy as np
import cv2 as cv

def addNoise(image):
    """Add salt and pepper noise to an image."""
    noiseAddedImage = np.copy(image)
    rows, cols, channels = image.shape
    numNoisePoints = int(np.ceil(image.size * 0.5))
    
    coordsX = np.random.randint(0, rows, numNoisePoints)
    coordsY = np.random.randint(0, cols, numNoisePoints)
    
    for channel in range(channels):
        noiseAddedImage[coordsX, coordsY, channel] = 1
        
    return noiseAddedImage

def generateInputs(imagesLow, imagesHigh):
    """Generator for training data."""
    for i in range(len(imagesLow)):
        xInput = imagesLow[i].reshape(1, 500, 500, 3)
        yInput = imagesHigh[i].reshape(1, 500, 500, 3)
        yield (xInput, yInput)

def extractTestInput(imagePath):
    """Prepare a test image for prediction."""
    image = cv.imread(imagePath)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = cv.resize(image, (500, 500))
    
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv[..., 2] = hsv[..., 2] * 0.2
    lowImage = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    noisyImage = addNoise(lowImage)
    
=======
import numpy as np
import cv2 as cv

def addNoise(image):
    """Add salt and pepper noise to an image."""
    noiseAddedImage = np.copy(image)
    rows, cols, channels = image.shape
    numNoisePoints = int(np.ceil(image.size * 0.5))
    
    coordsX = np.random.randint(0, rows, numNoisePoints)
    coordsY = np.random.randint(0, cols, numNoisePoints)
    
    for channel in range(channels):
        noiseAddedImage[coordsX, coordsY, channel] = 1
        
    return noiseAddedImage

def generateInputs(imagesLow, imagesHigh):
    """Generator for training data."""
    for i in range(len(imagesLow)):
        xInput = imagesLow[i].reshape(1, 500, 500, 3)
        yInput = imagesHigh[i].reshape(1, 500, 500, 3)
        yield (xInput, yInput)

def extractTestInput(imagePath):
    """Prepare a test image for prediction."""
    image = cv.imread(imagePath)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = cv.resize(image, (500, 500))
    
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv[..., 2] = hsv[..., 2] * 0.2
    lowImage = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    noisyImage = addNoise(lowImage)
    
>>>>>>> ccfd08bd8a18241085436d95e8b5b9c291750d03
    return noisyImage.reshape(1, 500, 500, 3)