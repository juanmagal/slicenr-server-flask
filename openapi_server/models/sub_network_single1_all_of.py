# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.sub_network_single1_all_of_attributes import SubNetworkSingle1AllOfAttributes
from openapi_server import util

from openapi_server.models.sub_network_single1_all_of_attributes import SubNetworkSingle1AllOfAttributes  # noqa: E501

class SubNetworkSingle1AllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """SubNetworkSingle1AllOf - a model defined in OpenAPI

        :param attributes: The attributes of this SubNetworkSingle1AllOf.  # noqa: E501
        :type attributes: SubNetworkSingle1AllOfAttributes
        """
        self.openapi_types = {
            'attributes': SubNetworkSingle1AllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'SubNetworkSingle1AllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubNetwork_Single_1_allOf of this SubNetworkSingle1AllOf.  # noqa: E501
        :rtype: SubNetworkSingle1AllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this SubNetworkSingle1AllOf.


        :return: The attributes of this SubNetworkSingle1AllOf.
        :rtype: SubNetworkSingle1AllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SubNetworkSingle1AllOf.


        :param attributes: The attributes of this SubNetworkSingle1AllOf.
        :type attributes: SubNetworkSingle1AllOfAttributes
        """

        self._attributes = attributes