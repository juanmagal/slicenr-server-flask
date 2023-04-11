# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server import util

from openapi_server.models.managed_element_single import ManagedElementSingle  # noqa: E501

class MnSOneOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, managed_element=None):  # noqa: E501
        """MnSOneOf1 - a model defined in OpenAPI

        :param managed_element: The managed_element of this MnSOneOf1.  # noqa: E501
        :type managed_element: List[ManagedElementSingle]
        """
        self.openapi_types = {
            'managed_element': List[ManagedElementSingle]
        }

        self.attribute_map = {
            'managed_element': 'ManagedElement'
        }

        self._managed_element = managed_element

    @classmethod
    def from_dict(cls, dikt) -> 'MnSOneOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MnS_oneOf_1 of this MnSOneOf1.  # noqa: E501
        :rtype: MnSOneOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def managed_element(self):
        """Gets the managed_element of this MnSOneOf1.


        :return: The managed_element of this MnSOneOf1.
        :rtype: List[ManagedElementSingle]
        """
        return self._managed_element

    @managed_element.setter
    def managed_element(self, managed_element):
        """Sets the managed_element of this MnSOneOf1.


        :param managed_element: The managed_element of this MnSOneOf1.
        :type managed_element: List[ManagedElementSingle]
        """

        self._managed_element = managed_element
