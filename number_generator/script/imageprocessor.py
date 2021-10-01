from typing import List, Tuple, Optional
import numpy as np

def invert_image(image: np.ndarray) -> np.ndarray:
    """
    Inverts the color of an image for readability

    Parameters
    ----------
    image:
        A single image in numpy matrix format. Each cell should be a value 0-255.

    Returns
    -------
    image:
        The same image as given, but with each pixel invert in color
    """

    return 255 - image


def trim_image(image: np.ndarray) -> np.ndarray:
    """
    Trims an image in numpy format. Removes all horizontal empty (0) space.

    Parameters
    ----------
    image:
        A single image in numpy matrix format. Each cell should be a value 0-255.

    Returns
    -------
    image:
        The same image as given, but trimmed so that all horizontal empty space
        is gone.
    """

    maxs = np.max(image, axis=0)
    nonzero = np.nonzero(maxs)[0]

    new_image = image[:, nonzero[0]:nonzero[-1]+1]

    return new_image


def space_images(
    images: List[np.ndarray],
    spacing_range: Tuple[int, int],
    random_seed: Optional[int] = None
) -> np.ndarray:
    """
    Takes a lsit of numpy image matrices and spaces them in a single image,
    with random buffers between each in the given `spacing_range`.

    Parameters
    ----------
    images:
        A list of images, in numpy matrix format.
    spacing_range:
        A tuple of integers (min, max) to uniform draw spacings from.
    random_seed:
        An optional int to feed to the random number generator for consistency:
        Default is None.

    Returns
    -------
    image, a combined numpy ndarray that has all digits in it, with uniform
    random spacing between each digit.
    """

    rng = np.random.default_rng(random_seed)

    images = [trim_image(img) for img in images]

    grand_image_list = [images[0]]

    for i in range(1, len(images)):
        random_space = rng.integers(low=spacing_range[0], high=spacing_range[1]+1, size=1)[0]

        grand_image_list.append(np.zeros((28, random_space)))
        grand_image_list.append(images[i])

    image = np.concatenate(grand_image_list, axis=1)

    return image

def pad_image_bounds(
    image: np.ndarray,
    image_width: int,
    random_seed: Optional[int] = None
) -> np.ndarray:
    """
    Pads the left and right of the image with extra empty space, to reach the
    target `image_width`.

    Parameters
    ----------
    image:
        An image in numpy matrix format
    image_width:
        An integer number of pizels the image should be in total
    random_seed:
        An optional int to feed to the random number generator for consistency:
        Default is None.

    Returns
    -------
    image, a numpy matrix image with the desired target width.
    """

    rng = np.random.default_rng(random_seed)

    current_width = image.shape[1]
    remaining_width = image_width - current_width

    left_width = rng.integers(low=0, high=remaining_width, size=1)[0]
    right_width = remaining_width - left_width

    images = [np.zeros((28, left_width)), image, np.zeros((28, right_width))]
    image = np.concatenate(images, axis=1)

    return image
