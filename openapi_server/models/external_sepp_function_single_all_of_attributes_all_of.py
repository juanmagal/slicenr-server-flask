# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class ExternalSeppFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, s_eppid=None, fqdn=None):  # noqa: E501
        """ExternalSeppFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this ExternalSeppFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id: PlmnId
        :param s_eppid: The s_eppid of this ExternalSeppFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_eppid: int
        :param fqdn: The fqdn of this ExternalSeppFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type fqdn: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            's_eppid': int,
            'fqdn': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            's_eppid': 'sEPPId',
            'fqdn': 'fqdn'
        }

        self._plmn_id = plmn_id
        self._s_eppid = s_eppid
        self._fqdn = fqdn

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalSeppFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalSeppFunction_Single_allOf_attributes_allOf of this ExternalSeppFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: ExternalSeppFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :return: The plmn_id of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :param plmn_id: The plmn_id of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def s_eppid(self):
        """Gets the s_eppid of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :return: The s_eppid of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._s_eppid

    @s_eppid.setter
    def s_eppid(self, s_eppid):
        """Sets the s_eppid of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :param s_eppid: The s_eppid of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :type s_eppid: int
        """

        self._s_eppid = s_eppid

    @property
    def fqdn(self):
        """Gets the fqdn of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :return: The fqdn of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this ExternalSeppFunctionSingleAllOfAttributesAllOf.


        :param fqdn: The fqdn of this ExternalSeppFunctionSingleAllOfAttributesAllOf.
        :type fqdn: str
        """

        self._fqdn = fqdn