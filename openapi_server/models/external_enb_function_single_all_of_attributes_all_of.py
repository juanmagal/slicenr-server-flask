# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ExternalENBFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, e_nbid=None):  # noqa: E501
        """ExternalENBFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param e_nbid: The e_nbid of this ExternalENBFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type e_nbid: int
        """
        self.openapi_types = {
            'e_nbid': int
        }

        self.attribute_map = {
            'e_nbid': 'eNBId'
        }

        self._e_nbid = e_nbid

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalENBFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalENBFunction_Single_allOf_attributes_allOf of this ExternalENBFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: ExternalENBFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def e_nbid(self):
        """Gets the e_nbid of this ExternalENBFunctionSingleAllOfAttributesAllOf.


        :return: The e_nbid of this ExternalENBFunctionSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._e_nbid

    @e_nbid.setter
    def e_nbid(self, e_nbid):
        """Sets the e_nbid of this ExternalENBFunctionSingleAllOfAttributesAllOf.


        :param e_nbid: The e_nbid of this ExternalENBFunctionSingleAllOfAttributesAllOf.
        :type e_nbid: int
        """

        self._e_nbid = e_nbid
