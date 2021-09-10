# Rock-Paper-scissors-spock-lizard

A simple and fun game from the big bang theory.

1) get_images: A code that uses opencv to extract images from your webcam. stores thwm in the respective directories with just a few clicks.
2) Converting images to data points: A code to convert the images to arrays and store them as pickle files.
3) Model Training: Build a simple convolutional neural network and train it on the data.
4) Designing the game: Use open cv for real time prediciton. we get a random move from the computer and the code recognizes our move. The winner is then based on the below algorithm.

![image](https://user-images.githubusercontent.com/44200352/132858058-9f67a7e9-61c4-4233-bd94-a7683aef251a.png)

Note: A simple convnet. used only for demonstrative purposes.


CONV-NET Summary:
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 298, 298, 64)      1792      
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 149, 149, 64)      0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 147, 147, 64)      36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 73, 73, 64)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 71, 71, 128)       73856     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 35, 35, 128)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 33, 33, 128)       147584    
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 16, 16, 128)       0         
_________________________________________________________________
flatten (Flatten)            (None, 32768)             0         
_________________________________________________________________
dropout (Dropout)            (None, 32768)             0         
_________________________________________________________________
dense (Dense)                (None, 512)               16777728  
_________________________________________________________________
dense_1 (Dense)              (None, 3)                 1539      
=================================================================
Total params: 17,039,427
Trainable params: 17,039,427
Non-trainable params: 0
