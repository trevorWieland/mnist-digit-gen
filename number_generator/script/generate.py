from typing import Iterable, Tuple, Optional
from .dataload import MNIST_Loader
from .imageprocessor import invert_image, space_images, pad_image_bounds
import numpy as np

def generate_numbers_sequence(
    digits: Iterable[int],
    spacing_range: Tuple[int, int],
    image_width: int,
    random_seed: Optional[int] = None,
    verbose: bool = True
) -> np.ndarray:
    """
    Generate an image that contains the sequence of given numbers, spaced
    randomly using a uniform distribution.

    Parameters
    ----------
    digits:
	An iterable containing the numerical values of the digits from which
        the sequence will be generated (for example [3, 5, 0]).
    spacing_range:
	   a (minimum, maximum) int pair (tuple), representing the min and max spacing
       between digits. Unit should be pixel.
    image_width:
        specifies the width of the image in pixels.
    random_seed:
        An optional parameter to initialize random number generation
    verbose:
        An optional parameter of whether to print progress or not.

    Returns
    -------
    The image containing the sequence of numbers. Images should be represented
    as floating point 32bits numpy arrays with a scale ranging from 0 (black) to
    1 (white), the first dimension corresponding to the height and the second
    dimension to the width.
    """

    mnist = MNIST_Loader(random_seed=random_seed)

    mnist.load_MNIST()

    images = [mnist.fetch_digit(d) for d in digits]

    image = space_images(images, spacing_range, random_seed=random_seed)
    image = pad_image_bounds(image, image_width, random_seed=random_seed)
    image = invert_image(image)

    return image

def generate_phone_number(
    spacing_range: Tuple[int, int],
    image_width: int,
    random_seed: Optional[int] = None,
    verbose: bool = True
) -> np.ndarray:
    """
    Generates an image that contains random digits, in the format of
    a Japanese phone number.

    Parameters
    ----------
    spacing_range:
	    a (minimum, maximum) int pair (tuple), representing the min and max spacing
        between digits. Unit should be pixel.
    image_width:
        specifies the width of the image in pixels.
    random_seed:
        An optional parameter to initialize random number generation
    verbose:
        An optional parameter of whether to print progress or not.

    Returns
    -------
    An image containing the sequence of numbers generated.

    The image is represented as floating point 32bit numpy arrays with a scale
    ranging from 0 (black) to 1 (white), with the first dimension corresponding
    to the height and the second dimension to the width.
    """

    random_digits = generate_japanese_number(random_seed)

    image = generate_numbers_sequence(random_digits, spacing_range, image_width, random_seed=random_seed, verbose=verbose)

    return image

def generate_japanese_number(random_seed: Optional[int] = None):
    """
    Generates a random set of digits in the format of a japanese phone number.

    Parameters
    ----------
    random_seed:
        An optional parameter to initialize random number generation

    Returns
    -------
    random_digits, a list of 10 random digits to use in image generation.
    """

    rng = np.random.default_rng(random_seed)

    random_digits = rng.integers(low=0, high=10, size=(10,))

    return random_digits
