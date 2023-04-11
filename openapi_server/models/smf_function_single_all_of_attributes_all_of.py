# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_type import AccessType
from openapi_server.models.comm_model import CommModel
from openapi_server.models.ip_addr1 import IpAddr1
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.s_nssai_smf_info_item import SNssaiSmfInfoItem
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange
from openapi_server import util

from openapi_server.models.access_type import AccessType  # noqa: E501
from openapi_server.models.comm_model import CommModel  # noqa: E501
from openapi_server.models.ip_addr1 import IpAddr1  # noqa: E501
from openapi_server.models.managed_nf_profile import ManagedNFProfile  # noqa: E501
from openapi_server.models.plmn_info import PlmnInfo  # noqa: E501
from openapi_server.models.s_nssai_smf_info_item import SNssaiSmfInfoItem  # noqa: E501
from openapi_server.models.tai import Tai  # noqa: E501
from openapi_server.models.tai_range import TaiRange  # noqa: E501

class SmfFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, p_lmn_info_list=None, n_rtac_list=None, s_bi_fqdn=None, s_nssai_smf_info_list=None, tai_list=None, tai_range_list=None, pwg_fqdn=None, pgw_addr_list=None, access_type=None, priority=None, c_nsiid_list=None, vsmf_support_ind=None, pwg_fqdn_list=None, managed_nf_profile=None, comm_model_list=None, configurable5_qi_set_ref=None, dynamic5_qi_set_ref=None):  # noqa: E501
        """SmfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param p_lmn_info_list: The p_lmn_info_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type p_lmn_info_list: List[PlmnInfo]
        :param n_rtac_list: The n_rtac_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type n_rtac_list: List[int]
        :param s_bi_fqdn: The s_bi_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_bi_fqdn: str
        :param s_nssai_smf_info_list: The s_nssai_smf_info_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_nssai_smf_info_list: List[SNssaiSmfInfoItem]
        :param tai_list: The tai_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type tai_list: List[Tai]
        :param tai_range_list: The tai_range_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type tai_range_list: List[TaiRange]
        :param pwg_fqdn: The pwg_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type pwg_fqdn: str
        :param pgw_addr_list: The pgw_addr_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type pgw_addr_list: List[IpAddr1]
        :param access_type: The access_type of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type access_type: AccessType
        :param priority: The priority of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type priority: int
        :param c_nsiid_list: The c_nsiid_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type c_nsiid_list: List[str]
        :param vsmf_support_ind: The vsmf_support_ind of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type vsmf_support_ind: bool
        :param pwg_fqdn_list: The pwg_fqdn_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type pwg_fqdn_list: List[str]
        :param managed_nf_profile: The managed_nf_profile of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type managed_nf_profile: ManagedNFProfile
        :param comm_model_list: The comm_model_list of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type comm_model_list: List[CommModel]
        :param configurable5_qi_set_ref: The configurable5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type configurable5_qi_set_ref: str
        :param dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type dynamic5_qi_set_ref: str
        """
        self.openapi_types = {
            'p_lmn_info_list': List[PlmnInfo],
            'n_rtac_list': List[int],
            's_bi_fqdn': str,
            's_nssai_smf_info_list': List[SNssaiSmfInfoItem],
            'tai_list': List[Tai],
            'tai_range_list': List[TaiRange],
            'pwg_fqdn': str,
            'pgw_addr_list': List[IpAddr1],
            'access_type': AccessType,
            'priority': int,
            'c_nsiid_list': List[str],
            'vsmf_support_ind': bool,
            'pwg_fqdn_list': List[str],
            'managed_nf_profile': ManagedNFProfile,
            'comm_model_list': List[CommModel],
            'configurable5_qi_set_ref': str,
            'dynamic5_qi_set_ref': str
        }

        self.attribute_map = {
            'p_lmn_info_list': 'pLMNInfoList',
            'n_rtac_list': 'nRTACList',
            's_bi_fqdn': 'sBIFqdn',
            's_nssai_smf_info_list': 'sNssaiSmfInfoList',
            'tai_list': 'taiList',
            'tai_range_list': 'taiRangeList',
            'pwg_fqdn': 'pwgFqdn',
            'pgw_addr_list': 'pgwAddrList',
            'access_type': 'accessType',
            'priority': 'priority',
            'c_nsiid_list': 'cNSIIdList',
            'vsmf_support_ind': 'vsmfSupportInd',
            'pwg_fqdn_list': 'pwgFqdnList',
            'managed_nf_profile': 'managedNFProfile',
            'comm_model_list': 'commModelList',
            'configurable5_qi_set_ref': 'configurable5QISetRef',
            'dynamic5_qi_set_ref': 'dynamic5QISetRef'
        }

        self._p_lmn_info_list = p_lmn_info_list
        self._n_rtac_list = n_rtac_list
        self._s_bi_fqdn = s_bi_fqdn
        self._s_nssai_smf_info_list = s_nssai_smf_info_list
        self._tai_list = tai_list
        self._tai_range_list = tai_range_list
        self._pwg_fqdn = pwg_fqdn
        self._pgw_addr_list = pgw_addr_list
        self._access_type = access_type
        self._priority = priority
        self._c_nsiid_list = c_nsiid_list
        self._vsmf_support_ind = vsmf_support_ind
        self._pwg_fqdn_list = pwg_fqdn_list
        self._managed_nf_profile = managed_nf_profile
        self._comm_model_list = comm_model_list
        self._configurable5_qi_set_ref = configurable5_qi_set_ref
        self._dynamic5_qi_set_ref = dynamic5_qi_set_ref

    @classmethod
    def from_dict(cls, dikt) -> 'SmfFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmfFunction_Single_allOf_attributes_allOf of this SmfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: SmfFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_lmn_info_list(self):
        """Gets the p_lmn_info_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The p_lmn_info_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[PlmnInfo]
        """
        return self._p_lmn_info_list

    @p_lmn_info_list.setter
    def p_lmn_info_list(self, p_lmn_info_list):
        """Sets the p_lmn_info_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param p_lmn_info_list: The p_lmn_info_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type p_lmn_info_list: List[PlmnInfo]
        """

        self._p_lmn_info_list = p_lmn_info_list

    @property
    def n_rtac_list(self):
        """Gets the n_rtac_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The n_rtac_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[int]
        """
        return self._n_rtac_list

    @n_rtac_list.setter
    def n_rtac_list(self, n_rtac_list):
        """Sets the n_rtac_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param n_rtac_list: The n_rtac_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type n_rtac_list: List[int]
        """

        self._n_rtac_list = n_rtac_list

    @property
    def s_bi_fqdn(self):
        """Gets the s_bi_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The s_bi_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._s_bi_fqdn

    @s_bi_fqdn.setter
    def s_bi_fqdn(self, s_bi_fqdn):
        """Sets the s_bi_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.


        :param s_bi_fqdn: The s_bi_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.
        :type s_bi_fqdn: str
        """

        self._s_bi_fqdn = s_bi_fqdn

    @property
    def s_nssai_smf_info_list(self):
        """Gets the s_nssai_smf_info_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The s_nssai_smf_info_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[SNssaiSmfInfoItem]
        """
        return self._s_nssai_smf_info_list

    @s_nssai_smf_info_list.setter
    def s_nssai_smf_info_list(self, s_nssai_smf_info_list):
        """Sets the s_nssai_smf_info_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param s_nssai_smf_info_list: The s_nssai_smf_info_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type s_nssai_smf_info_list: List[SNssaiSmfInfoItem]
        """

        self._s_nssai_smf_info_list = s_nssai_smf_info_list

    @property
    def tai_list(self):
        """Gets the tai_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The tai_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[Tai]
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param tai_list: The tai_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type tai_list: List[Tai]
        """

        self._tai_list = tai_list

    @property
    def tai_range_list(self):
        """Gets the tai_range_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The tai_range_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[TaiRange]
        """
        return self._tai_range_list

    @tai_range_list.setter
    def tai_range_list(self, tai_range_list):
        """Sets the tai_range_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param tai_range_list: The tai_range_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type tai_range_list: List[TaiRange]
        """

        self._tai_range_list = tai_range_list

    @property
    def pwg_fqdn(self):
        """Gets the pwg_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The pwg_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._pwg_fqdn

    @pwg_fqdn.setter
    def pwg_fqdn(self, pwg_fqdn):
        """Sets the pwg_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.


        :param pwg_fqdn: The pwg_fqdn of this SmfFunctionSingleAllOfAttributesAllOf.
        :type pwg_fqdn: str
        """

        self._pwg_fqdn = pwg_fqdn

    @property
    def pgw_addr_list(self):
        """Gets the pgw_addr_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The pgw_addr_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[IpAddr1]
        """
        return self._pgw_addr_list

    @pgw_addr_list.setter
    def pgw_addr_list(self, pgw_addr_list):
        """Sets the pgw_addr_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param pgw_addr_list: The pgw_addr_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type pgw_addr_list: List[IpAddr1]
        """

        self._pgw_addr_list = pgw_addr_list

    @property
    def access_type(self):
        """Gets the access_type of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The access_type of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: AccessType
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this SmfFunctionSingleAllOfAttributesAllOf.


        :param access_type: The access_type of this SmfFunctionSingleAllOfAttributesAllOf.
        :type access_type: AccessType
        """

        self._access_type = access_type

    @property
    def priority(self):
        """Gets the priority of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The priority of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SmfFunctionSingleAllOfAttributesAllOf.


        :param priority: The priority of this SmfFunctionSingleAllOfAttributesAllOf.
        :type priority: int
        """

        self._priority = priority

    @property
    def c_nsiid_list(self):
        """Gets the c_nsiid_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The c_nsiid_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._c_nsiid_list

    @c_nsiid_list.setter
    def c_nsiid_list(self, c_nsiid_list):
        """Sets the c_nsiid_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param c_nsiid_list: The c_nsiid_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type c_nsiid_list: List[str]
        """

        self._c_nsiid_list = c_nsiid_list

    @property
    def vsmf_support_ind(self):
        """Gets the vsmf_support_ind of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The vsmf_support_ind of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: bool
        """
        return self._vsmf_support_ind

    @vsmf_support_ind.setter
    def vsmf_support_ind(self, vsmf_support_ind):
        """Sets the vsmf_support_ind of this SmfFunctionSingleAllOfAttributesAllOf.


        :param vsmf_support_ind: The vsmf_support_ind of this SmfFunctionSingleAllOfAttributesAllOf.
        :type vsmf_support_ind: bool
        """

        self._vsmf_support_ind = vsmf_support_ind

    @property
    def pwg_fqdn_list(self):
        """Gets the pwg_fqdn_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The pwg_fqdn_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._pwg_fqdn_list

    @pwg_fqdn_list.setter
    def pwg_fqdn_list(self, pwg_fqdn_list):
        """Sets the pwg_fqdn_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param pwg_fqdn_list: The pwg_fqdn_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type pwg_fqdn_list: List[str]
        """

        self._pwg_fqdn_list = pwg_fqdn_list

    @property
    def managed_nf_profile(self):
        """Gets the managed_nf_profile of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The managed_nf_profile of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: ManagedNFProfile
        """
        return self._managed_nf_profile

    @managed_nf_profile.setter
    def managed_nf_profile(self, managed_nf_profile):
        """Sets the managed_nf_profile of this SmfFunctionSingleAllOfAttributesAllOf.


        :param managed_nf_profile: The managed_nf_profile of this SmfFunctionSingleAllOfAttributesAllOf.
        :type managed_nf_profile: ManagedNFProfile
        """

        self._managed_nf_profile = managed_nf_profile

    @property
    def comm_model_list(self):
        """Gets the comm_model_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The comm_model_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[CommModel]
        """
        return self._comm_model_list

    @comm_model_list.setter
    def comm_model_list(self, comm_model_list):
        """Sets the comm_model_list of this SmfFunctionSingleAllOfAttributesAllOf.


        :param comm_model_list: The comm_model_list of this SmfFunctionSingleAllOfAttributesAllOf.
        :type comm_model_list: List[CommModel]
        """

        self._comm_model_list = comm_model_list

    @property
    def configurable5_qi_set_ref(self):
        """Gets the configurable5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The configurable5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._configurable5_qi_set_ref

    @configurable5_qi_set_ref.setter
    def configurable5_qi_set_ref(self, configurable5_qi_set_ref):
        """Sets the configurable5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.


        :param configurable5_qi_set_ref: The configurable5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.
        :type configurable5_qi_set_ref: str
        """

        self._configurable5_qi_set_ref = configurable5_qi_set_ref

    @property
    def dynamic5_qi_set_ref(self):
        """Gets the dynamic5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.


        :return: The dynamic5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._dynamic5_qi_set_ref

    @dynamic5_qi_set_ref.setter
    def dynamic5_qi_set_ref(self, dynamic5_qi_set_ref):
        """Sets the dynamic5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.


        :param dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this SmfFunctionSingleAllOfAttributesAllOf.
        :type dynamic5_qi_set_ref: str
        """

        self._dynamic5_qi_set_ref = dynamic5_qi_set_ref
