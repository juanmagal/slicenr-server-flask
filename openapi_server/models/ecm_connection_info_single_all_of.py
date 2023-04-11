# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ecm_connection_info_single_all_of_attributes import EcmConnectionInfoSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.ecm_connection_info_single_all_of_attributes import EcmConnectionInfoSingleAllOfAttributes  # noqa: E501

class EcmConnectionInfoSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """EcmConnectionInfoSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this EcmConnectionInfoSingleAllOf.  # noqa: E501
        :type attributes: EcmConnectionInfoSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': EcmConnectionInfoSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'EcmConnectionInfoSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EcmConnectionInfo_Single_allOf of this EcmConnectionInfoSingleAllOf.  # noqa: E501
        :rtype: EcmConnectionInfoSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this EcmConnectionInfoSingleAllOf.


        :return: The attributes of this EcmConnectionInfoSingleAllOf.
        :rtype: EcmConnectionInfoSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EcmConnectionInfoSingleAllOf.


        :param attributes: The attributes of this EcmConnectionInfoSingleAllOf.
        :type attributes: EcmConnectionInfoSingleAllOfAttributes
        """

        self._attributes = attributes
