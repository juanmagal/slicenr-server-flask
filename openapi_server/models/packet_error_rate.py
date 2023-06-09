# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PacketErrorRate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, scalar=None, exponent=None):  # noqa: E501
        """PacketErrorRate - a model defined in OpenAPI

        :param scalar: The scalar of this PacketErrorRate.  # noqa: E501
        :type scalar: int
        :param exponent: The exponent of this PacketErrorRate.  # noqa: E501
        :type exponent: int
        """
        self.openapi_types = {
            'scalar': int,
            'exponent': int
        }

        self.attribute_map = {
            'scalar': 'scalar',
            'exponent': 'exponent'
        }

        self._scalar = scalar
        self._exponent = exponent

    @classmethod
    def from_dict(cls, dikt) -> 'PacketErrorRate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PacketErrorRate of this PacketErrorRate.  # noqa: E501
        :rtype: PacketErrorRate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def scalar(self):
        """Gets the scalar of this PacketErrorRate.


        :return: The scalar of this PacketErrorRate.
        :rtype: int
        """
        return self._scalar

    @scalar.setter
    def scalar(self, scalar):
        """Sets the scalar of this PacketErrorRate.


        :param scalar: The scalar of this PacketErrorRate.
        :type scalar: int
        """

        self._scalar = scalar

    @property
    def exponent(self):
        """Gets the exponent of this PacketErrorRate.


        :return: The exponent of this PacketErrorRate.
        :rtype: int
        """
        return self._exponent

    @exponent.setter
    def exponent(self, exponent):
        """Sets the exponent of this PacketErrorRate.


        :param exponent: The exponent of this PacketErrorRate.
        :type exponent: int
        """

        self._exponent = exponent
