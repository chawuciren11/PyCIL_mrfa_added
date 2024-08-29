.. _How To Use:

How To Use
==================

Clone this GitHub repository:

::

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

::

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

::

   def download_data(self):
       assert 0, "You should specify the folder of your dataset"
       train_dir = '[DATA-PATH]/train/'
       test_dir = '[DATA-PATH]/val/'

|

`Here <https://drive.google.com/drive/folders/1RBrPGrZzd1bHU5YG8PjdfwpHANZR_lhJ?usp=sharing>`_ is the file list of ImageNet100 (or say ImageNet-Sub).