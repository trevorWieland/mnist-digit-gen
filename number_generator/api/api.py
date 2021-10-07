from ..script.generate import generate_numbers_sequence as gen_seq
from ..script.generate import generate_phone_number as gen_phone
from .api_models import GenerateSequenceRequest, GeneratePhoneNumberRequest

from typing import List, Tuple, Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

import cv2
import io

app = FastAPI()

@app.post("/generate-numbers-sequence", response_class=StreamingResponse, responses={200: {"content": {"image/png":{}}}})
async def generate_numbers_sequence(gen_request: GenerateSequenceRequest) -> StreamingResponse:
    """
    Generates a PNG image of a digit sequence, given a set of guiding parameters.

    See `GenerateSequenceRequest` object model for guidelines on parameters.

    Input:
        gen_request:
            A `GenerateSequenceRequest` object

    Output:
        The PNG image, streamed as an "image/png" media type byte string.
    """


    image = gen_seq(
        digits=gen_request.sequence,
        spacing_range=(gen_request.min_spacing, gen_request.max_spacing),
        image_width=gen_request.image_width,
        random_seed=gen_request.random_seed
    )

    image_bytes = cv2.imencode('.png', image)[1].tobytes()

    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png", headers={'Content-Disposition':'inline; filename="image.png"'})


@app.post("/generate-phone-number", response_class=StreamingResponse, responses={200: {"content": {"image/png":{}}}})
async def generate_phone_number(gen_request: GeneratePhoneNumberRequest) -> StreamingResponse:
    """
    Generates a PNG image of a generated phone number, given a set of guiding parameters.

    See `GeneratePhoneNumberRequest` object model for guidelines on parameters.

    Input:
        gen_request:
            A `GeneratePhoneNumberRequest` object

    Output:
        The PNG image, streamed as an "image/png" media type byte string.
    """

    image = gen_phone(
        spacing_range=(gen_request.min_spacing, gen_request.max_spacing),
        image_width=gen_request.image_width,
        random_seed=gen_request.random_seed
    )

    image_bytes = cv2.imencode('.png', image)[1].tobytes()

    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")
