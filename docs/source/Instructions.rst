.. _Instructions:

Instructions
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