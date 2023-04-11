# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.files_single_all_of_attributes import FilesSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.files_single_all_of_attributes import FilesSingleAllOfAttributes  # noqa: E501

class FilesSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """FilesSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this FilesSingleAllOf.  # noqa: E501
        :type attributes: FilesSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': FilesSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'FilesSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Files_Single_allOf of this FilesSingleAllOf.  # noqa: E501
        :rtype: FilesSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this FilesSingleAllOf.


        :return: The attributes of this FilesSingleAllOf.
        :rtype: FilesSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this FilesSingleAllOf.


        :param attributes: The attributes of this FilesSingleAllOf.
        :type attributes: FilesSingleAllOfAttributes
        """

        self._attributes = attributes
