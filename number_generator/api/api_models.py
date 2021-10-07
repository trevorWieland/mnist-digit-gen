from typing import List, Optional
from pydantic import BaseModel, Field

class GenerateSequenceRequest(BaseModel):
    """
    A helper model class for accessing the digit generator through an API
    """

    sequence: List[int] = Field(..., gt=0, description="An iterable of the int values to generate")
    min_spacing: int = Field(..., gte=0, description="The int minimum amount of pixels between each digit")
    max_spacing: int = Field(..., gte=0, description="The int minimum amount of pixels between each digit")
    image_width: int = Field(..., gt=0, description="The width of the image in pixels")
    random_seed: Optional[int] = Field(None, description="An optional int to use as random seed.")

    class Config:
        schema_extra = {
            "example": {
                "sequence": [1, 2, 3, 4, 5],
                "min_spacing": 0,
                "max_spacing": 10,
                "image_width": 256,
                "random_seed": 0
            }
        }


class GeneratePhoneNumberRequest(BaseModel):
    """
    A helper model class for accessing the phone number generator through an API

    __NOTE:__ This API request will only return a single image in response! This is
    different from other interfaces to the library. In the interest of performance, the
    user should instead call this API endpoint as many times as they need images, in a
    parallel manner, to avoid long API runtimes.
    """

    min_spacing: int = Field(..., gt=0, description="The int minimum amount of pixels between each digit")
    max_spacing: int = Field(..., gt=0, description="The int minimum amount of pixels between each digit")
    image_width: int = Field(..., gt=0, description="The width of the image in pixels")
    random_seed: Optional[int] = Field(None, description="An optional int to use as random seed.")

    class Config:
        schema_extra = {
            "example": {
                "min_spacing": 0,
                "max_spacing": 10,
                "image_width": 512,
                "random_seed": 0
            }
        }
