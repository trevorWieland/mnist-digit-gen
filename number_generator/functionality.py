from typing import Iterable, Tuple, Optional
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

    return np.ones((1,1))

def generate_phone_numbers(
    spacing_range: Tuple[int, int],
    image_width: int,
    num_images: int,
    random_seed: Optional[int] = None,
    verbose: bool = True
) -> List[np.ndarray]:
    """
    Generates a list of images that contain random digits, in the format of
    Japanese phone numbers.

    Parameters
    ----------
    spacing_range:
	    a (minimum, maximum) int pair (tuple), representing the min and max spacing
        between digits. Unit should be pixel.
    image_width:
        specifies the width of the image in pixels.
    num_images:
        The integer number of images to create
    random_seed:
        An optional parameter to initialize random number generation
    verbose:
        An optional parameter of whether to print progress or not.

    Returns
    -------
    A list of images containing the sequences of numbers generated.

    Each image is represented as floating point 32bit numpy arrays with a scale
    ranging from 0 (black) to 1 (white), with the first dimension corresponding
    to the height and the second dimension to the width.
    """

    return [np.ones((1,1))]
