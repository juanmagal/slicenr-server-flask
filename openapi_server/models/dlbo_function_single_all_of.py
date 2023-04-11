# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dlbo_function_single_all_of_attributes import DLBOFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.dlbo_function_single_all_of_attributes import DLBOFunctionSingleAllOfAttributes  # noqa: E501

class DLBOFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """DLBOFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this DLBOFunctionSingleAllOf.  # noqa: E501
        :type attributes: DLBOFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': DLBOFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'DLBOFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLBOFunction_Single_allOf of this DLBOFunctionSingleAllOf.  # noqa: E501
        :rtype: DLBOFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this DLBOFunctionSingleAllOf.


        :return: The attributes of this DLBOFunctionSingleAllOf.
        :rtype: DLBOFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DLBOFunctionSingleAllOf.


        :param attributes: The attributes of this DLBOFunctionSingleAllOf.
        :type attributes: DLBOFunctionSingleAllOfAttributes
        """

        self._attributes = attributes