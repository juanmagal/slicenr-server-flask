# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.nf_profile import NFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.nf_profile import NFProfile  # noqa: E501
from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class NrfFunctionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id_list=None, s_bi_fqdn=None, c_nsiid_list=None, n_f_profile_list=None, snssai_list=None):  # noqa: E501
        """NrfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param plmn_id_list: The plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id_list: List[PlmnId]
        :param s_bi_fqdn: The s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type s_bi_fqdn: str
        :param c_nsiid_list: The c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type c_nsiid_list: List[str]
        :param n_f_profile_list: The n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type n_f_profile_list: List[NFProfile]
        :param snssai_list: The snssai_list of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :type snssai_list: List[Snssai]
        """
        self.openapi_types = {
            'plmn_id_list': List[PlmnId],
            's_bi_fqdn': str,
            'c_nsiid_list': List[str],
            'n_f_profile_list': List[NFProfile],
            'snssai_list': List[Snssai]
        }

        self.attribute_map = {
            'plmn_id_list': 'plmnIdList',
            's_bi_fqdn': 'sBIFqdn',
            'c_nsiid_list': 'cNSIIdList',
            'n_f_profile_list': 'nFProfileList',
            'snssai_list': 'snssaiList'
        }

        self._plmn_id_list = plmn_id_list
        self._s_bi_fqdn = s_bi_fqdn
        self._c_nsiid_list = c_nsiid_list
        self._n_f_profile_list = n_f_profile_list
        self._snssai_list = snssai_list

    @classmethod
    def from_dict(cls, dikt) -> 'NrfFunctionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NrfFunction_Single_allOf_attributes_allOf of this NrfFunctionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: NrfFunctionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id_list(self):
        """Gets the plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :return: The plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[PlmnId]
        """
        return self._plmn_id_list

    @plmn_id_list.setter
    def plmn_id_list(self, plmn_id_list):
        """Sets the plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :param plmn_id_list: The plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :type plmn_id_list: List[PlmnId]
        """

        self._plmn_id_list = plmn_id_list

    @property
    def s_bi_fqdn(self):
        """Gets the s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf.


        :return: The s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._s_bi_fqdn

    @s_bi_fqdn.setter
    def s_bi_fqdn(self, s_bi_fqdn):
        """Sets the s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf.


        :param s_bi_fqdn: The s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf.
        :type s_bi_fqdn: str
        """

        self._s_bi_fqdn = s_bi_fqdn

    @property
    def c_nsiid_list(self):
        """Gets the c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :return: The c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._c_nsiid_list

    @c_nsiid_list.setter
    def c_nsiid_list(self, c_nsiid_list):
        """Sets the c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :param c_nsiid_list: The c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :type c_nsiid_list: List[str]
        """

        self._c_nsiid_list = c_nsiid_list

    @property
    def n_f_profile_list(self):
        """Gets the n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf.

        List of NF profile  # noqa: E501

        :return: The n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[NFProfile]
        """
        return self._n_f_profile_list

    @n_f_profile_list.setter
    def n_f_profile_list(self, n_f_profile_list):
        """Sets the n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf.

        List of NF profile  # noqa: E501

        :param n_f_profile_list: The n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :type n_f_profile_list: List[NFProfile]
        """

        self._n_f_profile_list = n_f_profile_list

    @property
    def snssai_list(self):
        """Gets the snssai_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :return: The snssai_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :rtype: List[Snssai]
        """
        return self._snssai_list

    @snssai_list.setter
    def snssai_list(self, snssai_list):
        """Sets the snssai_list of this NrfFunctionSingleAllOfAttributesAllOf.


        :param snssai_list: The snssai_list of this NrfFunctionSingleAllOfAttributesAllOf.
        :type snssai_list: List[Snssai]
        """

        self._snssai_list = snssai_list
