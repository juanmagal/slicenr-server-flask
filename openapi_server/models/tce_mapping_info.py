# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.tce_mapping_info_tce_ip_address import TceMappingInfoTceIPAddress
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
from openapi_server.models.tce_mapping_info_tce_ip_address import TceMappingInfoTceIPAddress  # noqa: E501

class TceMappingInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tce_ip_address=None, tce_id=None, plmn_target=None):  # noqa: E501
        """TceMappingInfo - a model defined in OpenAPI

        :param tce_ip_address: The tce_ip_address of this TceMappingInfo.  # noqa: E501
        :type tce_ip_address: TceMappingInfoTceIPAddress
        :param tce_id: The tce_id of this TceMappingInfo.  # noqa: E501
        :type tce_id: int
        :param plmn_target: The plmn_target of this TceMappingInfo.  # noqa: E501
        :type plmn_target: PlmnId
        """
        self.openapi_types = {
            'tce_ip_address': TceMappingInfoTceIPAddress,
            'tce_id': int,
            'plmn_target': PlmnId
        }

        self.attribute_map = {
            'tce_ip_address': 'TceIPAddress',
            'tce_id': 'TceID',
            'plmn_target': 'PlmnTarget'
        }

        self._tce_ip_address = tce_ip_address
        self._tce_id = tce_id
        self._plmn_target = plmn_target

    @classmethod
    def from_dict(cls, dikt) -> 'TceMappingInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TceMappingInfo of this TceMappingInfo.  # noqa: E501
        :rtype: TceMappingInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tce_ip_address(self):
        """Gets the tce_ip_address of this TceMappingInfo.


        :return: The tce_ip_address of this TceMappingInfo.
        :rtype: TceMappingInfoTceIPAddress
        """
        return self._tce_ip_address

    @tce_ip_address.setter
    def tce_ip_address(self, tce_ip_address):
        """Sets the tce_ip_address of this TceMappingInfo.


        :param tce_ip_address: The tce_ip_address of this TceMappingInfo.
        :type tce_ip_address: TceMappingInfoTceIPAddress
        """

        self._tce_ip_address = tce_ip_address

    @property
    def tce_id(self):
        """Gets the tce_id of this TceMappingInfo.


        :return: The tce_id of this TceMappingInfo.
        :rtype: int
        """
        return self._tce_id

    @tce_id.setter
    def tce_id(self, tce_id):
        """Sets the tce_id of this TceMappingInfo.


        :param tce_id: The tce_id of this TceMappingInfo.
        :type tce_id: int
        """

        self._tce_id = tce_id

    @property
    def plmn_target(self):
        """Gets the plmn_target of this TceMappingInfo.


        :return: The plmn_target of this TceMappingInfo.
        :rtype: PlmnId
        """
        return self._plmn_target

    @plmn_target.setter
    def plmn_target(self, plmn_target):
        """Sets the plmn_target of this TceMappingInfo.


        :param plmn_target: The plmn_target of this TceMappingInfo.
        :type plmn_target: PlmnId
        """

        self._plmn_target = plmn_target