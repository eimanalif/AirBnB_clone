#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): name of place.
        description (str): description of place.
        number_rooms (int): number of rooms in place.
        number_bathrooms (int): number of bathrooms
        max_guest (int): Maximum number of guests in the same place.
        price_by_night (int): price by night.
        latitude (float): The latitude of place.
        longitude (float): The longitude of place.
        amenity_ids (list): list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
