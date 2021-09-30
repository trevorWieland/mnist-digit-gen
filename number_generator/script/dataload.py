from typing import Optional
import numpy as np
import idx2numpy
import os
import io
import wget
import zipfile
import gzip

class MNIST_Loader:
    """
    A helper class to manage downloading and using the MNIST data.

    General order of use:
        - Initialze MNIST_Loader as a new object
        - Call the .load_MNIST() function to download/load the data
        - Call the .fetch_digit() function as many times as needed to fetch digits.
    """

    def __init__(self, download_directory: str = "mnist/", random_seed: Optional[int] = None):
        """
        Initializes the MNIST Digit Loader.
        Sets needed path information for use in reading the dataset.

        Parameters
        ----------
        download_directory:
            A string path to a folder to store data in. If this folder does not exist, it will be created.
            Default is 'mnist/'
        random_seed:
            An integer seed to feed to the random number generator when fetching a random digit.
            Default is None.

        Returns
        -------
        self, a MNIST_Loader object with initial parameters set up. Need to separately call
        .load_MNIST to read the files into memory.
        """

        self.download_directory = download_directory

        self.image_path = os.path.join(download_directory, "train-images-idx3-ubyte")
        self.label_path = os.path.join(download_directory, "train-labels-idx1-ubyte")

        if (not os.path.exists(self.image_path)) or (not os.path.exists(self.label_path)):
            self.downloaded_data = False
        else:
            self.downloaded_data = True

        self.rng = np.random.default_rng(random_seed)

        self.digit_mapping = None


    def load_MNIST(self) -> None:
        """
        Loads the data from the downloaded files into memory, for quick selection
        of digits.

        If the data is not downloaded in the expected location, it will download and extract
        the files.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if not self.downloaded_data:
            self.download_MNIST()

        self.image_array = idx2numpy.convert_from_file(self.image_path)
        label_array = idx2numpy.convert_from_file(self.label_path)

        self.digit_mapping = {}

        for e, label in enumerate(label_array):
            self.digit_mapping[label] = [e] + self.digit_mapping.get(label, [])

    def download_MNIST(self) -> None:
        """
        Downloads the MNIST dataset for use in selecting digits.
        Will also extract the data.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

        zip_path = os.path.join(self.download_directory, "mnist.zip")

        print("Downloading MNIST...")
        wget.download("https://data.deepai.org/mnist.zip", zip_path)

        print("Download Completed!")


        print("Processing Extraction...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.download_directory)

        image_path_gz = f"{self.image_path}.gz"
        with gzip.open(image_path_gz, "r") as ip:
            content = ip.read()

        with open(self.image_path, "wb") as f:
            f.write(content)

        label_path_gz = f"{self.label_path}.gz"
        with gzip.open(label_path_gz, "rb") as ip:
            content = ip.read()

        with open(self.label_path, "wb") as f:
            f.write(content)

        print("Extraction Completed!")


    def fetch_digit(self, digit: int) -> np.ndarray:
        """
        Fetch a random digit from the loaded MNIST dataset.

        Parameters
        ----------
        digit:
            An integer in the range [0,9] to select from the dataset.

        Returns
        -------
        array, a numpy ndarray with the pixel data of the requested digit.
        """

        if self.digit_mapping is None:
            raise RuntimeError("MNIST_Loader must be loaded prior to use!")

        ind = self.rng.choice(self.digit_mapping[digit])

        array = self.image_array[ind]

        return array
