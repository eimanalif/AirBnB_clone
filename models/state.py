#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent state.

    Attributes:
        name (str): name of state.
    """

    name = ""
