from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, BatchNormalization

# 为了加快收敛, 将每个卷积层的filter减半, 全连接减为1024
def AlexNet(input_shape = (224,224,3), output_shape = 2): # 输出只有 0 和 1
    model = Sequential() 
    model.add(
        Conv2D(filters=48, kernel_size = (11,11), strides = (4,4),   # 96减半为48
            padding= 'valid', input_shape = input_shape, activation = 'relu')
    )
    model.add(BatchNormalization())
    model.add(
        MaxPool2D(pool_size=(3,3), strides=(2,2), padding='valid')
    )

    model.add(
        Conv2D(filters=128, kernel_size = (5,5), strides = (1,1),   # 256减半为128
            padding= 'same', activation = 'relu')
    )
    model.add(BatchNormalization())
    model.add(
        MaxPool2D(pool_size=(3,3), strides=(2,2), padding='valid')
    )

    model.add(
        Conv2D(filters=192, kernel_size = (3,3), strides = (1,1),   # 384减半为192
            padding= 'same', activation = 'relu')
    )
    model.add(
        Conv2D(filters=192, kernel_size = (3,3), strides = (1,1),   # 384减半为192
            padding= 'same', activation = 'relu')
    )
    model.add(
        Conv2D(filters=128, kernel_size = (3,3), strides = (1,1),   # 256减半为128
            padding= 'same', activation = 'relu')
    )
    model.add(
        MaxPool2D(pool_size=(3,3), strides=(2,2), padding='valid')
    )
    # 两个全连接层
    model.add(Flatten())

    model.add(Dense(1024, activation='relu')) # 4096 缩为 1024
    model.add(Dropout(0.25))

    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.25))

    model.add(Dense(output_shape, activation='softmax'))
    return model