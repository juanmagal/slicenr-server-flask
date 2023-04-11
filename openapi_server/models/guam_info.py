# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class GUAMInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, p_lmnid=None, a_mf_identifier=None):  # noqa: E501
        """GUAMInfo - a model defined in OpenAPI

        :param p_lmnid: The p_lmnid of this GUAMInfo.  # noqa: E501
        :type p_lmnid: PlmnId
        :param a_mf_identifier: The a_mf_identifier of this GUAMInfo.  # noqa: E501
        :type a_mf_identifier: int
        """
        self.openapi_types = {
            'p_lmnid': PlmnId,
            'a_mf_identifier': int
        }

        self.attribute_map = {
            'p_lmnid': 'pLMNId',
            'a_mf_identifier': 'aMFIdentifier'
        }

        self._p_lmnid = p_lmnid
        self._a_mf_identifier = a_mf_identifier

    @classmethod
    def from_dict(cls, dikt) -> 'GUAMInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GUAMInfo of this GUAMInfo.  # noqa: E501
        :rtype: GUAMInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_lmnid(self):
        """Gets the p_lmnid of this GUAMInfo.


        :return: The p_lmnid of this GUAMInfo.
        :rtype: PlmnId
        """
        return self._p_lmnid

    @p_lmnid.setter
    def p_lmnid(self, p_lmnid):
        """Sets the p_lmnid of this GUAMInfo.


        :param p_lmnid: The p_lmnid of this GUAMInfo.
        :type p_lmnid: PlmnId
        """

        self._p_lmnid = p_lmnid

    @property
    def a_mf_identifier(self):
        """Gets the a_mf_identifier of this GUAMInfo.


        :return: The a_mf_identifier of this GUAMInfo.
        :rtype: int
        """
        return self._a_mf_identifier

    @a_mf_identifier.setter
    def a_mf_identifier(self, a_mf_identifier):
        """Sets the a_mf_identifier of this GUAMInfo.


        :param a_mf_identifier: The a_mf_identifier of this GUAMInfo.
        :type a_mf_identifier: int
        """

        self._a_mf_identifier = a_mf_identifier