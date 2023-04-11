# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nef_function_single_all_of_attributes import NefFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.nef_function_single_all_of_attributes import NefFunctionSingleAllOfAttributes  # noqa: E501

class NefFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """NefFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this NefFunctionSingleAllOf.  # noqa: E501
        :type attributes: NefFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': NefFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'NefFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NefFunction_Single_allOf of this NefFunctionSingleAllOf.  # noqa: E501
        :rtype: NefFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this NefFunctionSingleAllOf.


        :return: The attributes of this NefFunctionSingleAllOf.
        :rtype: NefFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NefFunctionSingleAllOf.


        :param attributes: The attributes of this NefFunctionSingleAllOf.
        :type attributes: NefFunctionSingleAllOfAttributes
        """

        self._attributes = attributes