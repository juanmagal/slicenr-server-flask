# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nwdaf_function_single_all_of_attributes import NwdafFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.nwdaf_function_single_all_of_attributes import NwdafFunctionSingleAllOfAttributes  # noqa: E501

class NwdafFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """NwdafFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this NwdafFunctionSingleAllOf.  # noqa: E501
        :type attributes: NwdafFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': NwdafFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'NwdafFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NwdafFunction_Single_allOf of this NwdafFunctionSingleAllOf.  # noqa: E501
        :rtype: NwdafFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this NwdafFunctionSingleAllOf.


        :return: The attributes of this NwdafFunctionSingleAllOf.
        :rtype: NwdafFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NwdafFunctionSingleAllOf.


        :param attributes: The attributes of this NwdafFunctionSingleAllOf.
        :type attributes: NwdafFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
