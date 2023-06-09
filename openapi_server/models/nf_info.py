# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ausf_info import AusfInfo
from openapi_server.models.supported_data_set_id import SupportedDataSetId
from openapi_server.models.udm_info import UdmInfo
from openapi_server.models.udrinfo import Udrinfo
from openapi_server.models.upf_info import UpfInfo
from openapi_server import util

from openapi_server.models.ausf_info import AusfInfo  # noqa: E501
from openapi_server.models.supported_data_set_id import SupportedDataSetId  # noqa: E501
from openapi_server.models.udm_info import UdmInfo  # noqa: E501
from openapi_server.models.udrinfo import Udrinfo  # noqa: E501
from openapi_server.models.upf_info import UpfInfo  # noqa: E501

class NFInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, n_f_srv_group_id=None, smf_serving_areas=None, supported_data_set_ids=None):  # noqa: E501
        """NFInfo - a model defined in OpenAPI

        :param n_f_srv_group_id: The n_f_srv_group_id of this NFInfo.  # noqa: E501
        :type n_f_srv_group_id: str
        :param smf_serving_areas: The smf_serving_areas of this NFInfo.  # noqa: E501
        :type smf_serving_areas: str
        :param supported_data_set_ids: The supported_data_set_ids of this NFInfo.  # noqa: E501
        :type supported_data_set_ids: List[SupportedDataSetId]
        """
        self.openapi_types = {
            'n_f_srv_group_id': str,
            'smf_serving_areas': str,
            'supported_data_set_ids': List[SupportedDataSetId]
        }

        self.attribute_map = {
            'n_f_srv_group_id': 'nFSrvGroupId',
            'smf_serving_areas': 'smfServingAreas',
            'supported_data_set_ids': 'supportedDataSetIds'
        }

        self._n_f_srv_group_id = n_f_srv_group_id
        self._smf_serving_areas = smf_serving_areas
        self._supported_data_set_ids = supported_data_set_ids

    @classmethod
    def from_dict(cls, dikt) -> 'NFInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NFInfo of this NFInfo.  # noqa: E501
        :rtype: NFInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n_f_srv_group_id(self):
        """Gets the n_f_srv_group_id of this NFInfo.


        :return: The n_f_srv_group_id of this NFInfo.
        :rtype: str
        """
        return self._n_f_srv_group_id

    @n_f_srv_group_id.setter
    def n_f_srv_group_id(self, n_f_srv_group_id):
        """Sets the n_f_srv_group_id of this NFInfo.


        :param n_f_srv_group_id: The n_f_srv_group_id of this NFInfo.
        :type n_f_srv_group_id: str
        """

        self._n_f_srv_group_id = n_f_srv_group_id

    @property
    def smf_serving_areas(self):
        """Gets the smf_serving_areas of this NFInfo.


        :return: The smf_serving_areas of this NFInfo.
        :rtype: str
        """
        return self._smf_serving_areas

    @smf_serving_areas.setter
    def smf_serving_areas(self, smf_serving_areas):
        """Sets the smf_serving_areas of this NFInfo.


        :param smf_serving_areas: The smf_serving_areas of this NFInfo.
        :type smf_serving_areas: str
        """

        self._smf_serving_areas = smf_serving_areas

    @property
    def supported_data_set_ids(self):
        """Gets the supported_data_set_ids of this NFInfo.


        :return: The supported_data_set_ids of this NFInfo.
        :rtype: List[SupportedDataSetId]
        """
        return self._supported_data_set_ids

    @supported_data_set_ids.setter
    def supported_data_set_ids(self, supported_data_set_ids):
        """Sets the supported_data_set_ids of this NFInfo.


        :param supported_data_set_ids: The supported_data_set_ids of this NFInfo.
        :type supported_data_set_ids: List[SupportedDataSetId]
        """

        self._supported_data_set_ids = supported_data_set_ids
