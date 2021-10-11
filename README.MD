# MNIST Digit Generator

A python library to assist in the training of handwritten digit recognition.

## Usage
This library provides several ways to interact with the underlying functionality.
Each usage style uses the same base code, so which option you choose is just a matter of convenience.

The primary purpose of this library is to generate images containing a sequence of digits, which originate from the MNIST dataset.
These images can then be used in the training pipeline of some model, for an automated source of training / testing data.

This library relies on poetry as its dependency manager, which is a modern approach to organizing dependencies for python packages.
You can find more details about it [here](https://python-poetry.org/).

## Installation

This library supports multiple ways to install. The simplest way is to install using poetry, which is a modern dependency tracker and environment manager for python.

### Installation with poetry

If poetry is already installed on your system, simply cd to the root directory of the code, and run:

    poetry install

This will create a new poetry-managed virtual environment, with all dependencies installed. You can then open this environment by running:

    poetry shell

Or directly run the script by running

    poetry run number-generator
    
For more details about running the code, see below.

### Installation with wheel

In addition to poetry, which is the recommended installation method, a python wheel is provided for installation. To install, simply cownload the .whl file included in the dist folder. Then (assuming you're in the same folder), run:

    pip install number_generator-0.1.0-py3-none-any.whl

This will install the library like any other python package.

## Usage as a library

Assuming you've already got in installed, its now ready to be imported, as:

    from number_generator import generate_numbers_sequence, generate_phone_number

This interface provides two main functions:
- `generate_numbers_sequence`
- `generate_phone_number`

These functions handle two different ways of image generation, with full type-hints and docstrings explaining their usage.

## Usage from the command line

Assuming you've already got in installed, this library can be used from the command line in a few ways, depending on installation.

If you've installed it through poetry, in a poetry virtual environment, you can run:

    poetry run number-generator --help

Otherwise, if installed as a normal python package, you can run:

    python -m number-generator --help

For full information on how to run this from the command line, run one of the above commands to see the help, which will walk you through the script usage. This commandline interface is provided via the `typer` library, and is a modern approach to making auto-documenting CLIs in python.

## Usage as an API

Unlike the other two use-cases, using this as a library does not involve installing the library, but instead involves running a docker container using the included `Dockerfile`.

To compose this container:
- Download the source code
- CD to the root folder of the source code
- RUN `docker build -t digitgenerator .`
- RUN `docker run -p 8085:80 digitgenerator`
- In a browser, go to [localhost:8085/docs](http://localhost:8085/docs) to view the interactive documentation.

In addition to this browser window, the API is now accessible from the ip address you've run this docker image from. Ensure functionality by manually using the web documentation first before relying on it in production.

This API is build using `FastAPI`, a modern API framework in python, that provides plentiful auto-documentation, and many conveniences that other libraries like `flask` don't. 
