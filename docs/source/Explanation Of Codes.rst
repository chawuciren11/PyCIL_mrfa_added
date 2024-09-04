.. _Explanation Of Main Codes:

Explanation Of Main Codes
==========================

base.py
----------

This script defines a Python class named BaseLearner,
designed for incremental learning scenarios in machine learning.
The BaseLearner class serves as a foundational framework
to manage and update the model's knowledge base as new tasks are introduced,
which can be easily used by all other methods.

* **\_\_init\_\_(self, args)** The constructor method that initializes an instance of the **BaseLearner** class.It sets up the learner with configuration parameters provided in the **args** dictionary,such as memory size, device placement (CPU or GPU),and initializes properties like the current task index, known classes, and total classes.

* **@property exemplar\_size** A property decorator that returns the number of samples in the memory.It checks the length of **\_data\_memory** and **\_targets\_memory** to ensure they are equal.

* **@property samples\_per\_class** Another property decorator that returns the number of samples per class.If a fixed memory is used (**\_fixed\_memory** is True),it returns **\_memory\_per\_class**;otherwise, it divides the total memory size **\_memory\_size**by the total number of classes **\_total\_classes**.

* **@property feature\_dim** Returns the feature dimension of the network model.If the model uses **DataParallel** (for multi-GPU training),it accesses the feature dimension through the **module** attribute;otherwise, it accesses it directly.

* **build\_rehearsal\_memory(self, data\_manager, per\_class)** A method that constructs or reduces the memory samples based on whether a fixed memory is used.The **data\_manager** manages the data, and **per\_class** specifies the number of samples per class.

* **save\_checkpoint(self, filename)** Saves the model's state to a file after completing a task.The model is first moved to the CPU,and then the model state dictionary and the current task index are saved.

* **after\_task(self)** A method called after completing a task,which is currently empty and can be usedto perform any necessary operations after task completion.

* **\_evaluate(self, y\_pred, y\_true)** Calculates the accuracy of the model based on given predictions and true labels.It computes grouped accuracy, top-1 accuracy, and top-k accuracy.It will be used in the next function(**eval\_task(self, save\_conf=False)**)

* **eval\_task(self, save\_conf=False)** Evaluates the performance of the current task.It calls **\_eval\_cnn**(use **\_eval\_cnn(self, loader)** function) and**\_eval\_nme**(use **\_eval\_nme(self, loader, class\_means)** function) methodsto evaluate the CNN model and the Nearest Mean Encoding (NME) model's performance.If **save\_conf** is True, it also saves the predictions and true labels and generates a confusion matrix.

* **incremental\_train(self)** A method intended for training the model on new tasks, which is currently empty.

* **\_train(self)** A method for training the model, which is also currently empty.

* **\_get\_memory(self)** Returns the current memory samples and labels.If the memory is empty, it returns None.

* **\_compute\_accuracy(self, model, loader)** This function is used in the validation phase of the training.It calculates the accuracy of a given model and data loader.The model runs in evaluation mode without updating gradients.

* **\_eval\_cnn(self, loader)** Uses the CNN model to evaluate samples from the data loader and returns predictions and true labels.

* **\_eval\_nme(self, loader, class\_means)** Uses Nearest Mean Encoding (NME) to evaluate samples and returns predictions and true labels.It calculates the mean for each class and then finds the samples closest to these means.

* **\_extract\_vectors(self, loader)** Extracts feature vectors from the samples in the data loader.

* **\_reduce\_exemplar(self, data\_manager, m)** Reduces the number of samples per class to a specified number **m**.It selects the most representative samples for each class to reduce the size of the memory.

* **\_construct\_exemplar(self, data\_manager, m)** Constructs samples for new classes.It selects the most representative samples for each class to construct the memory.

* **\_construct\_exemplar\_unified(self, data\_manager, m)** Constructs samples for new classes and updates the means of known classes.

main.py
-------------

These functions collectively prepare the environment for training a model
by handling configurations and command line inputs and initiating the training process.

* **main()** It serves as the entry point of the application.It creates an argument parser and parse command line arguments,loads a JSON configuration file specified by the config argumentand starts the training process.

* **load_json(settings_path)** It loads a JSON configuration file,which is used in the main function.

* **setup_parser()** It sets up and configures the command line argument parser,which is also used in the main function

trainer.py
--------------

This python script manages the setup, execution, and logging of the training process,
ensuring that experiments are reproducible and well-documented.

* **train(args)** This function is responsible for initiating the training processacross various configurations defined by different seeds and devices.

* **\_train(args)** This function manages the detailed setup and execution of the training process.It begins by initializing the number of initial classes, setting up the log directoryand configuring the logging.The data manager and model are initialized based on the provided arguments.The function then enters a loop over the tasks,where it performs incremental training, evaluates the model and logs the results.

* **\_set\_device(args)** This function configures the device settings for the training process.It determines whether to use CPU or GPU based on the device type specified in the arguments.

* **\_set\_random** This function sets random seeds for PyTorch to ensure reproducibility of experiments.

* **print\_args(args)** This function logs all the arguments used for the training process.It iterates through the arguments and logs each key-value pair.

autoaugment.py
----------------

The provided code defines several classes for image augmentation policies,
specifically tailored for datasets like ImageNet, CIFAR10, and SVHN.
These policies are designed to randomly select one of the best-performing sub-policies,
which are combinations of augmentation techniques with specific parameters.
The augmentations include operations such as rotation, color adjustment,
and contrast enhancement among others.
These policies can be directly used on images or integrated into a PyTorch transform pipeline
for batch processing.

data.py
------------

The code defines a hierarchy of classes for handling image data transformations
and downloading procedures specific to different datasets like CIFAR10, CIFAR100, and ImageNet.
Each class in the hierarchy (**iCIFAR10**, **iCIFAR100**, **iImageNet1000**, **iImageNet100**)
inherits from a base class **iData** and specifies dataset-specific transformations for training and testing.
These classes facilitate the preparation of data for machine learning models,
streamlining the process of data augmentation and normalization.

data_manager.py
-------------------------

The code defines a series of classes for image augmentation and dataset management in machine learning. 
The **GaussianBlur** and **Solarization** classes are used to apply blur and solarization effects to images,
respectively. The **cifar\_transform** and **imagenet\_transform**
are composed of multiple image preprocessing steps like cropping and color adjustment.
The **DataManager** class handles various dataset operations
such as data downloading, transformation application, and splitting datasets into training and testing sets.
It also supports incremental learning by managing class orders and task sizes.
The **DummyDataset**, **AugmentMemoryDataset**, and **DualAugmentDataset** classes
are custom PyTorch dataset wrappers that apply transformations and provide data
for model training and evaluation.
Lastly, the loader functions are utilities for loading images
from file paths in a format suitable for processing with PyTorch.

inc_net.py
-------------

* **BaseNet(nn.Module)** This a base class for constructing neural networks,inheriting from PyTorch's nn.Module.It initializes a convolutional network through a get_convnet functionand reserves a spot for a fully connected layer.This class provides methods for obtaining feature dimensions, extracting feature vectors,forward propagation, freezing parameters, and loading checkpoints.The update_fc and generate_fc methods are meant to be implemented in subclasses for updatingand generating the fully connected layer.

* **IncrementalNet(BaseNet)** This class inherits from BaseNetand is designed for incremental learning scenarios.It optionally integrates Grad-CAM(a visualization technique) during initialization.The update_fc method is used to update the fully connected layerto accommodate new classes during the incremental learning process.

* **CosineIncrementalNet(BaseNet)** This class is a subclass of BaseNet,designed for a specific incremental learning method involving cosine annealing.It initializes with arguments, a pretrained flag, and an additional nb_proxy parameter.The update_fc method also updates the fully connected layer based on the new task and number of classes.The generate_fc method creates a new fully connected layer,initializing weights using a cosine annealing strategy.

ops.py
-----------

The code defines a series of image augmentation techniques as callable classes in Python,
designed to apply various transformations to images for purposes
such as data augmentation in machine learning training.
These classes include operations like random cropping (Cutout), shearing (ShearX, ShearY),
translation (TranslateX, TranslateY), rotation (Rotate),
and adjustments to color, posterization, solarization, contrast, sharpness, brightness, auto-contrast,
and equalization.

toolkit.py
--------------
The provided code consists of utility functions and classes
designed to support various operations in machine learning and deep learning workflows,
particularly in the context of model training and evaluation.

* **ConfigEncoder Class** A custom JSON encoderthat handles serialization of complex data types like classes, enums, and functions,making them JSON-serializable.

* **count\_parameters Function** Counts the number of trainable or all parameters in a model,which is useful for monitoring model complexity.

* **tensor2numpy Function** Converts a PyTorch tensor to a NumPy array,facilitating interoperability between PyTorch and NumPy.

* **target2onehot Function** Converts target labels to one-hot encoded vectors.

* **makedirs Function** Ensures that a directory exists,creating it if it doesn't already exist, which is helpful for file management.

* **accuracy Function** Computes the accuracy of predictions,differentiating between 'old' and 'new' classes, and providing a total accuracy measure.

* **split_images_labels Function** Utility to split image data and their corresponding labels,often needed during data preprocessing part.

* **save_fc Function** Saves the fully connected layer weights of a model,which can be critical for tasks like feature extraction.

* **save_model Function** Saves the entire model or specific parts of it,ensuring that the trained model can be reused or further analyzed.