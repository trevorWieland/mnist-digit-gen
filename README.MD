# MNIST Digit Generator

A python library to assist in the training of handwritten digit recognition.

## Usage
This library provides several ways to interact with the underlying functionality.
Each usage style uses the same base code, so which option you choose is just a matter of convenience.

The primary purpose of this library is to generate images containing a sequence of digits, which originate from the MNIST dataset.
These images can then be used in the training pipeline of some model, for an automated source of training / testing data.

This library relies on poetry as its dependency manager, which is a modern approach to organizing dependencies for python packages.
You can find more details about it [here](https://python-poetry.org/).

### Usage as a library
This repo is installable as a python package, with its functionality able to be directly referenced.

Upon downloading the source code, you can install the library by opening the code in a terminal and typing:

    poetry install

This single command will manage all dependency installation for you, and provide its own built in virtual environment for you.
After running the installation command above, the package will be installed and available for use.

This interface provides two main functions:
- `generate_numbers_sequence`
- `generate_phone_number`

These functions

### Usage from the command line
After installation of this library as a python package, you are able to use it from the command line as well.

Upon downloading the source code, you can install the library by opening the code in a terminal and typing:

    poetry install

This single command will manage all dependency installation for you, and provide its own built in virtual environment for you.
After running the installation command above, the package will be installed and available for use.

### Usage as a RESTful API


## Expansion

### EMNIST
In addition to the standard MNIST digit dataset, there is an extended dataset known as EMNIST. This dataset is not used by default,
as it is much larger than normal MNIST. This extended dataset brings upper and lowercase english characters, as well as a much larger,
more varied set of images.

If installed, it will require an additional ~500MB of storage, as well as increased memory use when using the library. This function is
required to create sequences of characters however, so there is some tradeoff.

Installation depends on the usage style, see the relevant usage section for more details.

### Image Augmentation
As this library is primarily focussed on working as a data pipeline for machine learning models, there is also support for many standard
forms of data augmentation, such as warping, noise, brightness, and many others.
