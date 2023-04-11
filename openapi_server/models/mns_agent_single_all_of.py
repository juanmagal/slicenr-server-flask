# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.mns_agent_single_all_of_attributes import MnsAgentSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.mns_agent_single_all_of_attributes import MnsAgentSingleAllOfAttributes  # noqa: E501

class MnsAgentSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """MnsAgentSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this MnsAgentSingleAllOf.  # noqa: E501
        :type attributes: MnsAgentSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': MnsAgentSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'MnsAgentSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MnsAgent_Single_allOf of this MnsAgentSingleAllOf.  # noqa: E501
        :rtype: MnsAgentSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this MnsAgentSingleAllOf.


        :return: The attributes of this MnsAgentSingleAllOf.
        :rtype: MnsAgentSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this MnsAgentSingleAllOf.


        :param attributes: The attributes of this MnsAgentSingleAllOf.
        :type attributes: MnsAgentSingleAllOfAttributes
        """

        self._attributes = attributes
