from ..script.generate import generate_numbers_sequence as gen_seq
from ..script.generate import generate_phone_numbers as gen_phone

from typing import List, Tuple, Optional

import typer
import os
import cv2

app = typer.Typer()

@app.command("generate-numbers-sequence")
def generate_numbers_sequence(
    sequence: List[int] = typer.Argument(..., help="An iterable of the int values to generate"),
    min_spacing: int = typer.Option(..., help="The int minimum amount of pixels between each digit"),
    max_spacing: int = typer.Option(..., help="The int maximum amount of pixels between each digit"),
    image_width: int = typer.Option(..., help="The width of the image in pixels"),
    output_path: str = typer.Option(..., help="The filepath to save the generated image to"),
    random_seed: Optional[int] = typer.Option(None, help="An optional int to use as random seed. Default is None"),
    verbose: bool = typer.Option(True, help="An optional flag of whether to print progress. Default is True")
):
    """
    A CLI for utilizing the basic digit sequence generation function. Runs the routine
    `generate_numbers_sequence` from the api side.
    """

    if verbose:
        typer.echo("Generate Number Sequence")

        typer.echo(f"sequence received: {sequence}")
        typer.echo(f"min_spacing received: {min_spacing}")
        typer.echo(f"max_spacing received: {max_spacing}")
        typer.echo(f"image_width received: {image_width}")
        typer.echo(f"output_path received: {output_path}")
        typer.echo(f"random_seed received: {random_seed}")

    #Generate image
    image = gen_seq(sequence, (min_spacing, max_spacing), image_width, random_seed=random_seed, verbose=verbose)

    #Save image
    cv2.imwrite(output_path, image)

@app.command("generate-phone-numbers")
def generate_phone_numbers(
    min_spacing: int = typer.Option(..., help="The int minimum amount of pixels between each digit"),
    max_spacing: int = typer.Option(..., help="The int maximum amount of pixels between each digit"),
    image_width: int = typer.Option(..., help="The width of the image in pixels"),
    num_images: int = typer.Option(..., help="The number of images to generate"),
    output_path: str = typer.Option(..., help="The folderpath to save the generated images to"),
    random_seed: Optional[int] = typer.Option(None, help="An optional int to use as random seed. Default is None"),
    verbose: bool = typer.Option(True, help="An optional flag of whether to print progress. Default is True")
):
    """
    A CLI for generating digit sequences that match the pattern of Japanese phone numbers.
    Runs the routine `generate_phone_numbers` from the api side.
    """

    if verbose:
        typer.echo("Generate Phone Numbers")

        typer.echo(f"min_spacing received: {min_spacing}")
        typer.echo(f"max_spacing received: {max_spacing}")
        typer.echo(f"image_width received: {image_width}")
        typer.echo(f"num_images received: {num_images}")
        typer.echo(f"output_path received: {output_path}")
        typer.echo(f"random_seed received: {random_seed}")

    #Generate each image and save them
    with typer.progressbar(range(num_images), label="Generating") as progress:
        for i in progress:
            #Ensure that each image isn't exactly the same when giving a random seed
            if random_seed is None:
                seed = None
            else:
                seed = random_seed + i

            #Generate image
            image = gen_phone((min_spacing, max_spacing), image_width, random_seed=seed, verbose=verbose)

            #Save image
            output_full = os.path.join(output_path, f"phone_number_{i}.png")
            cv2.imwrite(output_full, image)
