<<<<<<< HEAD
from keras.layers import Input, Conv2D, add
from keras.models import Model

def buildModel(inputShape=(500, 500, 3)):
    """Create the CNN model for image enhancement."""
    inputLayer = Input(shape=inputShape)
    
    # Branch 1
    conv1 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(inputLayer)
    conv1 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(conv1)
    conv1 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv1)
    
    # Branch 2
    conv2 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(inputLayer)
    conv2 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv2)
    conv2 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv2)
    
    # Merge branches
    merged = add([conv1, conv2])
    
    # Branch 3
    conv3 = Conv2D(64, (3, 3), activation='relu', padding='same', strides=1)(merged)
    conv3 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(conv3)
    conv3 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv3)
    
    # Additional branches
    conv3_1 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(merged)
    conv3_1 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv3_1)
    
    conv3_2 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(merged)
    
    merged2 = add([conv3, conv3_1, conv3_2])
    
    # Final layers
    conv4 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged2)
    conv4_1 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged)
    
    merged3 = add([conv4, conv4_1, merged2])
    
    conv5 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged3)
    conv5 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv5)
    outputLayer = Conv2D(3, (3, 3), activation='relu', padding='same', strides=1)(conv5)
    
    model = Model(inputs=inputLayer, outputs=outputLayer)
    model.compile(optimizer='adam', loss='mean_squared_error')
=======
from keras.layers import Input, Conv2D, add
from keras.models import Model

def buildModel(inputShape=(500, 500, 3)):
    """Create the CNN model for image enhancement."""
    inputLayer = Input(shape=inputShape)
    
    # Branch 1
    conv1 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(inputLayer)
    conv1 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(conv1)
    conv1 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv1)
    
    # Branch 2
    conv2 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(inputLayer)
    conv2 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv2)
    conv2 = Conv2D(64, (2, 2), activation='relu', padding='same', strides=1)(conv2)
    
    # Merge branches
    merged = add([conv1, conv2])
    
    # Branch 3
    conv3 = Conv2D(64, (3, 3), activation='relu', padding='same', strides=1)(merged)
    conv3 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(conv3)
    conv3 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv3)
    
    # Additional branches
    conv3_1 = Conv2D(32, (3, 3), activation='relu', padding='same', strides=1)(merged)
    conv3_1 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv3_1)
    
    conv3_2 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(merged)
    
    merged2 = add([conv3, conv3_1, conv3_2])
    
    # Final layers
    conv4 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged2)
    conv4_1 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged)
    
    merged3 = add([conv4, conv4_1, merged2])
    
    conv5 = Conv2D(16, (3, 3), activation='relu', padding='same', strides=1)(merged3)
    conv5 = Conv2D(16, (2, 2), activation='relu', padding='same', strides=1)(conv5)
    outputLayer = Conv2D(3, (3, 3), activation='relu', padding='same', strides=1)(conv5)
    
    model = Model(inputs=inputLayer, outputs=outputLayer)
    model.compile(optimizer='adam', loss='mean_squared_error')
>>>>>>> ccfd08bd8a18241085436d95e8b5b9c291750d03
    return model