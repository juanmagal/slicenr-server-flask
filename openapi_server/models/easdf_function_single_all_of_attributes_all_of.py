# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.managed_nf_profile import ManagedNFProfile  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class EASDFFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, s_bi_fqdn=None, managed_nf_profile=None, server_addr=None):  # noqa: E501
        """EASDFFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this EASDFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id: PlmnId
        :param s_bi_fqdn: The s_bi_fqdn of this EASDFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_bi_fqdn: str
        :param managed_nf_profile: The managed_nf_profile of this EASDFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type managed_nf_profile: ManagedNFProfile
        :param server_addr: The server_addr of this EASDFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type server_addr: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            's_bi_fqdn': str,
            'managed_nf_profile': ManagedNFProfile,
            'server_addr': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            's_bi_fqdn': 'sBIFqdn',
            'managed_nf_profile': 'managedNFProfile',
            'server_addr': 'serverAddr'
        }

        self._plmn_id = plmn_id
        self._s_bi_fqdn = s_bi_fqdn
        self._managed_nf_profile = managed_nf_profile
        self._server_addr = server_addr

    @classmethod
    def from_dict(cls, dikt) -> 'EASDFFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EASDFFunction_Single_allOf_attributes_allOf of this EASDFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: EASDFFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this EASDFFunctionSingleAllOfAttributesAllOf.


        :return: The plmn_id of this EASDFFunctionSingleAllOfAttributesAllOf.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this EASDFFunctionSingleAllOfAttributesAllOf.


        :param plmn_id: The plmn_id of this EASDFFunctionSingleAllOfAttributesAllOf.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def s_bi_fqdn(self):
        """Gets the s_bi_fqdn of this EASDFFunctionSingleAllOfAttributesAllOf.


        :return: The s_bi_fqdn of this EASDFFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._s_bi_fqdn

    @s_bi_fqdn.setter
    def s_bi_fqdn(self, s_bi_fqdn):
        """Sets the s_bi_fqdn of this EASDFFunctionSingleAllOfAttributesAllOf.


        :param s_bi_fqdn: The s_bi_fqdn of this EASDFFunctionSingleAllOfAttributesAllOf.
        :type s_bi_fqdn: str
        """

        self._s_bi_fqdn = s_bi_fqdn

    @property
    def managed_nf_profile(self):
        """Gets the managed_nf_profile of this EASDFFunctionSingleAllOfAttributesAllOf.


        :return: The managed_nf_profile of this EASDFFunctionSingleAllOfAttributesAllOf.
        :rtype: ManagedNFProfile
        """
        return self._managed_nf_profile

    @managed_nf_profile.setter
    def managed_nf_profile(self, managed_nf_profile):
        """Sets the managed_nf_profile of this EASDFFunctionSingleAllOfAttributesAllOf.


        :param managed_nf_profile: The managed_nf_profile of this EASDFFunctionSingleAllOfAttributesAllOf.
        :type managed_nf_profile: ManagedNFProfile
        """

        self._managed_nf_profile = managed_nf_profile

    @property
    def server_addr(self):
        """Gets the server_addr of this EASDFFunctionSingleAllOfAttributesAllOf.


        :return: The server_addr of this EASDFFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._server_addr

    @server_addr.setter
    def server_addr(self, server_addr):
        """Sets the server_addr of this EASDFFunctionSingleAllOfAttributesAllOf.


        :param server_addr: The server_addr of this EASDFFunctionSingleAllOfAttributesAllOf.
        :type server_addr: str
        """

        self._server_addr = server_addr
