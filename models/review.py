#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): User id.
        text (str): text of review.
    """

    place_id = ""
    user_id = ""
    text = ""
