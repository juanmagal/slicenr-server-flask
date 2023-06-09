# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.comm_model import CommModel
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server import util

from openapi_server.models.comm_model import CommModel  # noqa: E501
from openapi_server.models.managed_nf_profile import ManagedNFProfile  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501

class DDNMFFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, s_bi_fqdn=None, managed_nf_profile=None, comm_model_list=None):  # noqa: E501
        """DDNMFFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this DDNMFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id: PlmnId
        :param s_bi_fqdn: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_bi_fqdn: str
        :param managed_nf_profile: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type managed_nf_profile: ManagedNFProfile
        :param comm_model_list: The comm_model_list of this DDNMFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type comm_model_list: List[CommModel]
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            's_bi_fqdn': str,
            'managed_nf_profile': ManagedNFProfile,
            'comm_model_list': List[CommModel]
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            's_bi_fqdn': 'sBIFqdn',
            'managed_nf_profile': 'managedNFProfile',
            'comm_model_list': 'commModelList'
        }

        self._plmn_id = plmn_id
        self._s_bi_fqdn = s_bi_fqdn
        self._managed_nf_profile = managed_nf_profile
        self._comm_model_list = comm_model_list

    @classmethod
    def from_dict(cls, dikt) -> 'DDNMFFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DDNMFFunction_Single_allOf_attributes_allOf of this DDNMFFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: DDNMFFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :return: The plmn_id of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :param plmn_id: The plmn_id of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :type plmn_id: PlmnId
        """

        self._plmn_id = plmn_id

    @property
    def s_bi_fqdn(self):
        """Gets the s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :return: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._s_bi_fqdn

    @s_bi_fqdn.setter
    def s_bi_fqdn(self, s_bi_fqdn):
        """Sets the s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :param s_bi_fqdn: The s_bi_fqdn of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :type s_bi_fqdn: str
        """

        self._s_bi_fqdn = s_bi_fqdn

    @property
    def managed_nf_profile(self):
        """Gets the managed_nf_profile of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :return: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :rtype: ManagedNFProfile
        """
        return self._managed_nf_profile

    @managed_nf_profile.setter
    def managed_nf_profile(self, managed_nf_profile):
        """Sets the managed_nf_profile of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :param managed_nf_profile: The managed_nf_profile of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :type managed_nf_profile: ManagedNFProfile
        """

        self._managed_nf_profile = managed_nf_profile

    @property
    def comm_model_list(self):
        """Gets the comm_model_list of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :return: The comm_model_list of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :rtype: List[CommModel]
        """
        return self._comm_model_list

    @comm_model_list.setter
    def comm_model_list(self, comm_model_list):
        """Sets the comm_model_list of this DDNMFFunctionSingleAllOfAttributesAllOf.


        :param comm_model_list: The comm_model_list of this DDNMFFunctionSingleAllOfAttributesAllOf.
        :type comm_model_list: List[CommModel]
        """

        self._comm_model_list = comm_model_list
