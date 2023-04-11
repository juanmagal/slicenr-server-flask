# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.cco_parameters_attr_all_of_attributes import CCOParametersAttrAllOfAttributes
from openapi_server import util

from openapi_server.models.cco_parameters_attr_all_of_attributes import CCOParametersAttrAllOfAttributes  # noqa: E501

class CCOParametersAttrAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """CCOParametersAttrAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this CCOParametersAttrAllOf.  # noqa: E501
        :type attributes: CCOParametersAttrAllOfAttributes
        """
        self.openapi_types = {
            'attributes': CCOParametersAttrAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'CCOParametersAttrAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CCOParameters_Attr_allOf of this CCOParametersAttrAllOf.  # noqa: E501
        :rtype: CCOParametersAttrAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this CCOParametersAttrAllOf.


        :return: The attributes of this CCOParametersAttrAllOf.
        :rtype: CCOParametersAttrAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CCOParametersAttrAllOf.


        :param attributes: The attributes of this CCOParametersAttrAllOf.
        :type attributes: CCOParametersAttrAllOfAttributes
        """

        self._attributes = attributes
