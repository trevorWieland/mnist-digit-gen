from number_generator.cli.cli import app
from typer.testing import CliRunner
from os import path
runner = CliRunner()

def test_cli_seq():
    """
    Tests the CLI for creating a sequence
    """

    digits = [1, 2, 3, 4, 5]
    spacing_range = (0, 10)
    image_width = 256
    random_seed = 12345

    result = runner.invoke(
        app,
        [
            "generate-numbers-sequence",
            "1", "2", "3", "4", "5",
            "--min-spacing", "0",
            "--max-spacing", "10",
            "--image-width", "256",
            "--random-seed", "12345",
            "--output-path", "cli_seq_test.png",
            "--no-verbose"
        ]
    )

    print(result.stdout)

    assert result.exit_code == 0
    assert path.exists("cli_seq_test.png")
    assert path.isfile("cli_seq_test.png")

    #Can be expanded by reading the image, and comparing the contents to expectations
