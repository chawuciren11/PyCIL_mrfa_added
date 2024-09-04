main.py
=========

These functions collectively prepare the environment for training a model
by handling configurations and command line inputs and initiating the training process.

* **main()** It serves as the entry point of the application.It creates an argument parser and parse command line arguments,loads a JSON configuration file specified by the config argumentand starts the training process.

* **load_json(settings_path)** It loads a JSON configuration file,which is used in the main function.

* **setup_parser()** It sets up and configures the command line argument parser,which is also used in the main function
