# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.external_sepp_function_single_all_of_attributes import ExternalSeppFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.external_sepp_function_single_all_of_attributes import ExternalSeppFunctionSingleAllOfAttributes  # noqa: E501

class ExternalSeppFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """ExternalSeppFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this ExternalSeppFunctionSingleAllOf.  # noqa: E501
        :type attributes: ExternalSeppFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': ExternalSeppFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalSeppFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalSeppFunction_Single_allOf of this ExternalSeppFunctionSingleAllOf.  # noqa: E501
        :rtype: ExternalSeppFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ExternalSeppFunctionSingleAllOf.


        :return: The attributes of this ExternalSeppFunctionSingleAllOf.
        :rtype: ExternalSeppFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExternalSeppFunctionSingleAllOf.


        :param attributes: The attributes of this ExternalSeppFunctionSingleAllOf.
        :type attributes: ExternalSeppFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
