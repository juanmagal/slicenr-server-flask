# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.common_beamforming_function_single_all_of_attributes import CommonBeamformingFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.common_beamforming_function_single_all_of_attributes import CommonBeamformingFunctionSingleAllOfAttributes  # noqa: E501

class CommonBeamformingFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """CommonBeamformingFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this CommonBeamformingFunctionSingleAllOf.  # noqa: E501
        :type attributes: CommonBeamformingFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': CommonBeamformingFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'CommonBeamformingFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommonBeamformingFunction_Single_allOf of this CommonBeamformingFunctionSingleAllOf.  # noqa: E501
        :rtype: CommonBeamformingFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this CommonBeamformingFunctionSingleAllOf.


        :return: The attributes of this CommonBeamformingFunctionSingleAllOf.
        :rtype: CommonBeamformingFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CommonBeamformingFunctionSingleAllOf.


        :param attributes: The attributes of this CommonBeamformingFunctionSingleAllOf.
        :type attributes: CommonBeamformingFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
