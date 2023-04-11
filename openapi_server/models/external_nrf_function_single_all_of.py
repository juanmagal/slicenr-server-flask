# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.external_nrf_function_single_all_of_attributes import ExternalNrfFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.external_nrf_function_single_all_of_attributes import ExternalNrfFunctionSingleAllOfAttributes  # noqa: E501

class ExternalNrfFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """ExternalNrfFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this ExternalNrfFunctionSingleAllOf.  # noqa: E501
        :type attributes: ExternalNrfFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': ExternalNrfFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalNrfFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalNrfFunction_Single_allOf of this ExternalNrfFunctionSingleAllOf.  # noqa: E501
        :rtype: ExternalNrfFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ExternalNrfFunctionSingleAllOf.


        :return: The attributes of this ExternalNrfFunctionSingleAllOf.
        :rtype: ExternalNrfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExternalNrfFunctionSingleAllOf.


        :param attributes: The attributes of this ExternalNrfFunctionSingleAllOf.
        :type attributes: ExternalNrfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes