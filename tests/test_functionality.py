from number_generator import generate_numbers_sequence, generate_phone_number

def test_gen_seq():
    """
    Basic test for functionality
    """

    digits = [1, 2, 3, 4, 5]
    spacing_range = (0, 10)
    image_width = 256
    random_seed = 12345

    image = generate_numbers_sequence(
        digits=digits,
        spacing_range=spacing_range,
        image_width=image_width,
        random_seed=random_seed,
        verbose=False
    )

    assert image.shape == (28, 256) #Makes sure the image is the correct shape
    assert 238.53069 < image.mean() < 238.53070 #Could be changed for an exact comparison, but this should be enough


def test_gen_pn():
    """
    Basic test for functionality
    """

    spacing_range = (0, 10)
    image_width = 512
    random_seed = 12345

    image = generate_phone_number(
        spacing_range=spacing_range,
        image_width=image_width,
        random_seed=random_seed,
        verbose=False
    )

    assert image.shape == (28, 512) #Makes sure the image is the correct shape
    assert 232.70179 < image.mean() < 232.70180 #Could be changed for an exact comparison, but this should be enough
