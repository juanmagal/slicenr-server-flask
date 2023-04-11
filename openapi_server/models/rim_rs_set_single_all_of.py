# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.rim_rs_set_single_all_of_attributes import RimRSSetSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.rim_rs_set_single_all_of_attributes import RimRSSetSingleAllOfAttributes  # noqa: E501

class RimRSSetSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """RimRSSetSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this RimRSSetSingleAllOf.  # noqa: E501
        :type attributes: RimRSSetSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': RimRSSetSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'RimRSSetSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RimRSSet_Single_allOf of this RimRSSetSingleAllOf.  # noqa: E501
        :rtype: RimRSSetSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this RimRSSetSingleAllOf.


        :return: The attributes of this RimRSSetSingleAllOf.
        :rtype: RimRSSetSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this RimRSSetSingleAllOf.


        :param attributes: The attributes of this RimRSSetSingleAllOf.
        :type attributes: RimRSSetSingleAllOfAttributes
        """

        self._attributes = attributes