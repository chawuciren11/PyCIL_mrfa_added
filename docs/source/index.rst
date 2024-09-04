.. diary documentation master file, created by
   sphinx-quickstart on Sat Oct 10 22:31:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyCIL: A Python Toolbox for Class-Incremental Learning
=================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   Welcome
   News
   Introduction
   Methods Reproduced
   Reproduced Results
   How To Use
   Awesome Papers Using PyCIL
   Explanation Of Main Codes
   Explanation Of Some Methods
   License
   Acknowledgements
   Contact
   Star History


.. figure:: ./resources/logo.png
   :scale: 50%
   :align: center

----

|LISENSE| |Python| |Pytorch| |Methods| |CIL| |visitors|

.. |LISENSE| image:: https://img.shields.io/badge/license-MIT-green?style=flat-square
   :target: https://github.com/yaoyao-liu/class-incremental-learning/blob/master/LICENSE

.. |Python| image:: https://img.shields.io/badge/python-3.8-blue.svg?style=flat-square&logo=python&color=3776AB&logoColor=3776AB
   :target: https://www.python.org/

.. |Pytorch| image:: https://img.shields.io/badge/pytorch-1.8-%237732a8?style=flat-square&logo=PyTorch&color=EE4C2C
   :target: https://pytorch.org/

.. |Methods| image:: https://img.shields.io/badge/Reproduced-20-success
   :target: https://github.com/G-U-N/PyCIL/tree/master

.. |CIL| image:: https://img.shields.io/badge/ClassIncrementalLearning-SOTA-success??style=for-the-badge&logo=appveyor
   :target: https://paperswithcode.com/task/incremental-learning

.. |visitors| image:: https://visitor-badge.laobi.icu/badge?page_id=LAMDA.PyCIL&left_color=green&right_color=red

----

Introduction
==============

Traditional machine learning systems are deployed under the closed-world setting,
which requires the entire training data before the offline training process.
However, real-world applications often face the incoming new classes, and a model should incorporate them continually.
The learning paradigm is called Class-Incremental Learning (CIL).
We propose a Python toolbox that implements several key algorithms for class-incremental learning
to ease the burden of researchers in the machine learning community.
The toolbox contains implementations of a number of founding works of CIL,
such as EWC and iCaRL, but also provides current state-of-the-art algorithms that can be used for conducting novel fundamental research.
This toolbox, named PyCIL for Python Class-Incremental Learning, is open source with an MIT license.

For more information about incremental learning, you can refer to these reading materials:

* A brief introduction (in Chinese) about CIL is available `here <https://zhuanlan.zhihu.com/p/490308909>`_.
* A PyTorch Tutorial to Class-Incremental Learning (with explicit codes and detailed explanations) is available `here <https://github.com/G-U-N/a-PyTorch-Tutorial-to-Class-Incremental-Learning>`_.

----

How To Use
==================

Clone this GitHub repository:

.. code-block:: python

   git clone https://github.com/G-U-N/PyCIL.git
   cd PyCIL

Dependencies
-------------------

- `torch 1.8.1 <https://github.com/pytorch/pytorch>`_
- `torchvision 0.9.0 <https://github.com/pytorch/vision>`_
- `tqdm <https://github.com/tqdm/tqdm>`_
- `numpy <https://github.com/numpy/numpy>`_
- `scipy <https://github.com/scipy/scipy>`_
- `quadprog <https://github.com/quadprog/quadprog>`_
- `POT <https://github.com/PythonOT/POT>`_

Running Experiments
-------------------------

1. Edit the ``[MODEL NAME].json`` file for global settings.
2. Edit the hyperparameters in the corresponding ``[MODEL NAME].py`` file (e.g., ``models/icarl.py``).
3. Run:

.. code-block:: python

   python main.py --config=./exps/[MODEL NAME].json

where ``[MODEL NAME]`` should be chosen from ``finetune``, ``ewc``, ``lwf``, ``replay``, ``gem``,  ``icarl``, ``bic``, ``wa``, ``podnet``, ``der``, etc.

4. Hyperparameters

When using PyCIL, you can edit the global parameters and algorithm-specific hyper-parameter in the corresponding json file.

These parameters include:

- **memory-size**: The total exemplar number in the incremental learning process. Assuming there are :math:`K` classes at the current stage, the model will preserve :math:`\left[\frac{memory-size}{K}\right]` exemplar per class.
- **init-cls**: The number of classes in the first incremental stage. Since there are different settings in CIL with a different number of classes in the first stage, our framework enables different choices to define the initial stage.
- **increment**: The number of classes in each incremental stage :math:`i`, :math:`i` > 1. By default, the number of classes per incremental stage is equivalent per stage.
- **convnet-type**: The backbone network for the incremental model. According to the benchmark setting, ``ResNet32`` is utilized for ``CIFAR100``, and ``ResNet18`` is used for ``ImageNet``.
- **seed**: The random seed adopted for shuffling the class order. According to the benchmark setting, it is set to 1993 by default.

Other parameters in terms of model optimization, e.g., batch size, optimization epoch, learning rate, learning rate decay, weight decay, milestone, and temperature, can be modified in the corresponding Python file.

Datasets
--------------

We have implemented the pre-processing of ``CIFAR100``, ``imagenet100``, and ``imagenet1000``. When training on ``CIFAR100``, this framework will automatically download it. When training on ``imagenet100/1000``, you should specify the folder of your dataset in ``utils/data.py``.

.. code-block:: python

   def download_data(self):
       assert 0, "You should specify the folder of your dataset"
       train_dir = '[DATA-PATH]/train/'
       test_dir = '[DATA-PATH]/val/'

|

`Here <https://drive.google.com/drive/folders/1RBrPGrZzd1bHU5YG8PjdfwpHANZR_lhJ?usp=sharing>`_ is the file list of ImageNet100 (or say ImageNet-Sub).
