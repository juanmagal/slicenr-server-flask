# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.managed_element_single1_all_of_attributes import ManagedElementSingle1AllOfAttributes
from openapi_server import util

from openapi_server.models.managed_element_single1_all_of_attributes import ManagedElementSingle1AllOfAttributes  # noqa: E501

class ManagedElementSingle1AllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """ManagedElementSingle1AllOf - a model defined in OpenAPI

        :param attributes: The attributes of this ManagedElementSingle1AllOf.  # noqa: E501
        :type attributes: ManagedElementSingle1AllOfAttributes
        """
        self.openapi_types = {
            'attributes': ManagedElementSingle1AllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementSingle1AllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement_Single_1_allOf of this ManagedElementSingle1AllOf.  # noqa: E501
        :rtype: ManagedElementSingle1AllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ManagedElementSingle1AllOf.


        :return: The attributes of this ManagedElementSingle1AllOf.
        :rtype: ManagedElementSingle1AllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ManagedElementSingle1AllOf.


        :param attributes: The attributes of this ManagedElementSingle1AllOf.
        :type attributes: ManagedElementSingle1AllOfAttributes
        """

        self._attributes = attributes
