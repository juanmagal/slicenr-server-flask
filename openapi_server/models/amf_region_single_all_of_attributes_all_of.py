# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.snssai import Snssai  # noqa: E501

class AmfRegionSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id_list=None, n_rtac_list=None, amf_region_id=None, snssai_list=None, a_mf_set_list_ref=None):  # noqa: E501
        """AmfRegionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param plmn_id_list: The plmn_id_list of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :type plmn_id_list: List[PlmnId]
        :param n_rtac_list: The n_rtac_list of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :type n_rtac_list: List[int]
        :param amf_region_id: The amf_region_id of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :type amf_region_id: int
        :param snssai_list: The snssai_list of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :type snssai_list: List[Snssai]
        :param a_mf_set_list_ref: The a_mf_set_list_ref of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :type a_mf_set_list_ref: List[str]
        """
        self.openapi_types = {
            'plmn_id_list': List[PlmnId],
            'n_rtac_list': List[int],
            'amf_region_id': int,
            'snssai_list': List[Snssai],
            'a_mf_set_list_ref': List[str]
        }

        self.attribute_map = {
            'plmn_id_list': 'plmnIdList',
            'n_rtac_list': 'nRTACList',
            'amf_region_id': 'amfRegionId',
            'snssai_list': 'snssaiList',
            'a_mf_set_list_ref': 'aMFSetListRef'
        }

        self._plmn_id_list = plmn_id_list
        self._n_rtac_list = n_rtac_list
        self._amf_region_id = amf_region_id
        self._snssai_list = snssai_list
        self._a_mf_set_list_ref = a_mf_set_list_ref

    @classmethod
    def from_dict(cls, dikt) -> 'AmfRegionSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfRegion_Single_allOf_attributes_allOf of this AmfRegionSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: AmfRegionSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id_list(self):
        """Gets the plmn_id_list of this AmfRegionSingleAllOfAttributesAllOf.


        :return: The plmn_id_list of this AmfRegionSingleAllOfAttributesAllOf.
        :rtype: List[PlmnId]
        """
        return self._plmn_id_list

    @plmn_id_list.setter
    def plmn_id_list(self, plmn_id_list):
        """Sets the plmn_id_list of this AmfRegionSingleAllOfAttributesAllOf.


        :param plmn_id_list: The plmn_id_list of this AmfRegionSingleAllOfAttributesAllOf.
        :type plmn_id_list: List[PlmnId]
        """

        self._plmn_id_list = plmn_id_list

    @property
    def n_rtac_list(self):
        """Gets the n_rtac_list of this AmfRegionSingleAllOfAttributesAllOf.


        :return: The n_rtac_list of this AmfRegionSingleAllOfAttributesAllOf.
        :rtype: List[int]
        """
        return self._n_rtac_list

    @n_rtac_list.setter
    def n_rtac_list(self, n_rtac_list):
        """Sets the n_rtac_list of this AmfRegionSingleAllOfAttributesAllOf.


        :param n_rtac_list: The n_rtac_list of this AmfRegionSingleAllOfAttributesAllOf.
        :type n_rtac_list: List[int]
        """

        self._n_rtac_list = n_rtac_list

    @property
    def amf_region_id(self):
        """Gets the amf_region_id of this AmfRegionSingleAllOfAttributesAllOf.

        AmfRegionId is defined in TS 23.003  # noqa: E501

        :return: The amf_region_id of this AmfRegionSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._amf_region_id

    @amf_region_id.setter
    def amf_region_id(self, amf_region_id):
        """Sets the amf_region_id of this AmfRegionSingleAllOfAttributesAllOf.

        AmfRegionId is defined in TS 23.003  # noqa: E501

        :param amf_region_id: The amf_region_id of this AmfRegionSingleAllOfAttributesAllOf.
        :type amf_region_id: int
        """
        if amf_region_id is not None and amf_region_id > 255:  # noqa: E501
            raise ValueError("Invalid value for `amf_region_id`, must be a value less than or equal to `255`")  # noqa: E501

        self._amf_region_id = amf_region_id

    @property
    def snssai_list(self):
        """Gets the snssai_list of this AmfRegionSingleAllOfAttributesAllOf.


        :return: The snssai_list of this AmfRegionSingleAllOfAttributesAllOf.
        :rtype: List[Snssai]
        """
        return self._snssai_list

    @snssai_list.setter
    def snssai_list(self, snssai_list):
        """Sets the snssai_list of this AmfRegionSingleAllOfAttributesAllOf.


        :param snssai_list: The snssai_list of this AmfRegionSingleAllOfAttributesAllOf.
        :type snssai_list: List[Snssai]
        """

        self._snssai_list = snssai_list

    @property
    def a_mf_set_list_ref(self):
        """Gets the a_mf_set_list_ref of this AmfRegionSingleAllOfAttributesAllOf.


        :return: The a_mf_set_list_ref of this AmfRegionSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._a_mf_set_list_ref

    @a_mf_set_list_ref.setter
    def a_mf_set_list_ref(self, a_mf_set_list_ref):
        """Sets the a_mf_set_list_ref of this AmfRegionSingleAllOfAttributesAllOf.


        :param a_mf_set_list_ref: The a_mf_set_list_ref of this AmfRegionSingleAllOfAttributesAllOf.
        :type a_mf_set_list_ref: List[str]
        """

        self._a_mf_set_list_ref = a_mf_set_list_ref
