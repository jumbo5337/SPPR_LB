# import plaidml.keras
# plaidml.keras.install_backend()
from datetime import datetime

import matplotlib.pyplot as plt
from tensorflow.keras import layers
# from keras import models
# from keras import layers
# from keras.datasets import mnist
# from keras.utils import to_categorical
# from keras import optimizers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

n_hidden_neurons = 5
epochs = 100
lr=0.01


network = models.Sequential()
network.add(layers.Dense(n_hidden_neurons, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(n_hidden_neurons, activation= 'relu'))
network.add(layers.Dense(10, activation='softmax'))
ADAM = optimizers.Adam(lr=lr)

network.compile(optimizer=ADAM,
                loss = 'categorical_crossentropy',
                metrics=['accuracy'])

batch_size = 128


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000,28 * 28))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000,28 * 28))
test_images = test_images.astype('float32')/255

test_labels = to_categorical(test_labels)
train_labels = to_categorical(train_labels)

start_time = datetime.now()

history = network.fit(train_images, train_labels, epochs=epochs, batch_size=batch_size)
test_loss, test_acc = network.evaluate(test_images, test_labels)



print(datetime.now()-start_time)



# plt.plot(history.history['accuracy'], color ='r', label ='train-accuracy')
# plt.hlines(test_acc,0,int(epochs-1),colors = 'b', ls = '--', label='test-accuracy')
# plt.legend(loc = 4)
# plt.title("Accuracy")
# plt.savefig("accuracy.png")
# plt.show()
# plt.close()
#
# plt.plot(history.history['loss'], color ='r', label ='train-loss')
# plt.hlines(test_loss,0,int(epochs-1),colors = 'b', ls = '--', label='test-loss')
# plt.legend(loc = 3)
# plt.title("Losses")
# plt.savefig("loss.png")
# plt.show()
# plt.close()
# print(test_loss)
# print(test_acc)