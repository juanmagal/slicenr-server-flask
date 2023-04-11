# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GeographicalCoordinates(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lattitude=None, longitude=None):  # noqa: E501
        """GeographicalCoordinates - a model defined in OpenAPI

        :param lattitude: The lattitude of this GeographicalCoordinates.  # noqa: E501
        :type lattitude: int
        :param longitude: The longitude of this GeographicalCoordinates.  # noqa: E501
        :type longitude: int
        """
        self.openapi_types = {
            'lattitude': int,
            'longitude': int
        }

        self.attribute_map = {
            'lattitude': 'lattitude',
            'longitude': 'longitude'
        }

        self._lattitude = lattitude
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt) -> 'GeographicalCoordinates':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeographicalCoordinates of this GeographicalCoordinates.  # noqa: E501
        :rtype: GeographicalCoordinates
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lattitude(self):
        """Gets the lattitude of this GeographicalCoordinates.


        :return: The lattitude of this GeographicalCoordinates.
        :rtype: int
        """
        return self._lattitude

    @lattitude.setter
    def lattitude(self, lattitude):
        """Sets the lattitude of this GeographicalCoordinates.


        :param lattitude: The lattitude of this GeographicalCoordinates.
        :type lattitude: int
        """

        self._lattitude = lattitude

    @property
    def longitude(self):
        """Gets the longitude of this GeographicalCoordinates.


        :return: The longitude of this GeographicalCoordinates.
        :rtype: int
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this GeographicalCoordinates.


        :param longitude: The longitude of this GeographicalCoordinates.
        :type longitude: int
        """

        self._longitude = longitude