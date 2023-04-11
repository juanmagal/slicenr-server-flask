# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.smsf_function_single_all_of_attributes import SmsfFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.smsf_function_single_all_of_attributes import SmsfFunctionSingleAllOfAttributes  # noqa: E501

class SmsfFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """SmsfFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this SmsfFunctionSingleAllOf.  # noqa: E501
        :type attributes: SmsfFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': SmsfFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'SmsfFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmsfFunction_Single_allOf of this SmsfFunctionSingleAllOf.  # noqa: E501
        :rtype: SmsfFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this SmsfFunctionSingleAllOf.


        :return: The attributes of this SmsfFunctionSingleAllOf.
        :rtype: SmsfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SmsfFunctionSingleAllOf.


        :param attributes: The attributes of this SmsfFunctionSingleAllOf.
        :type attributes: SmsfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
