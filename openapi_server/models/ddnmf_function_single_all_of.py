# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ddnmf_function_single_all_of_attributes import DDNMFFunctionSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.ddnmf_function_single_all_of_attributes import DDNMFFunctionSingleAllOfAttributes  # noqa: E501

class DDNMFFunctionSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """DDNMFFunctionSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this DDNMFFunctionSingleAllOf.  # noqa: E501
        :type attributes: DDNMFFunctionSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': DDNMFFunctionSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'DDNMFFunctionSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DDNMFFunction_Single_allOf of this DDNMFFunctionSingleAllOf.  # noqa: E501
        :rtype: DDNMFFunctionSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this DDNMFFunctionSingleAllOf.


        :return: The attributes of this DDNMFFunctionSingleAllOf.
        :rtype: DDNMFFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DDNMFFunctionSingleAllOf.


        :param attributes: The attributes of this DDNMFFunctionSingleAllOf.
        :type attributes: DDNMFFunctionSingleAllOfAttributes
        """

        self._attributes = attributes
