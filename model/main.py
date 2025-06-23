import os
from preprocess import preprocessData
from model import buildModel
from evaluate import evaluateImage
from utils import generateInputs
from keras import backend as K
import tensorflow as tf

def main():
    """
    Main function to run the image enhancement pipeline.
    
    """
    
    
    highPath = "/content/drive/MyDrive/LOW TO HIGH light image/our485/high"
    testImagePath = os.path.join(highPath, "96.png")
    imagesLow, imagesHigh = preprocessData(highPath)

    K.clear_session()
    

    model = buildModel()
    dataset = tf.data.Dataset.from_generator(
        lambda: generateInputs(imagesLow, imagesHigh),
        output_types=(tf.float32, tf.float32),
        output_shapes=((1, 500, 500, 3), (1, 500, 500, 3))
    )
    model.fit(dataset, epochs=40, verbose=1, steps_per_epoch=10)
    evaluateImage(testImagePath, model)

if __name__ == "__main__":
    main()