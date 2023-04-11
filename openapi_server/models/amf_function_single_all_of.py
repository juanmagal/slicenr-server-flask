# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.amf_function_single_all_of_attributes import AmfFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.amf_function_single_all_of_attributes import AmfFunctionSingleAllOfAttributes  # noqa: E501

class AmfFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """AmfFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this AmfFunctionSingleAllOf.  # noqa: E501
        :type attributes: AmfFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': AmfFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'AmfFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfFunction_Single_allOf of this AmfFunctionSingleAllOf.  # noqa: E501
        :rtype: AmfFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this AmfFunctionSingleAllOf.


        :return: The attributes of this AmfFunctionSingleAllOf.
        :rtype: AmfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AmfFunctionSingleAllOf.


        :param attributes: The attributes of this AmfFunctionSingleAllOf.
        :type attributes: AmfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
