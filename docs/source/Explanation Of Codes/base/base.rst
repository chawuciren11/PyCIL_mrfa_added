Base.py
========


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
