# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ip_address import IpAddress
from openapi_server.models.logical_interface_info import LogicalInterfaceInfo
from openapi_server import util

from openapi_server.models.ip_address import IpAddress  # noqa: E501
from openapi_server.models.logical_interface_info import LogicalInterfaceInfo  # noqa: E501

class EPTransportSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ip_address=None, logical_interface_info=None, next_hop_info=None, qos_profile=None, ep_application_refs=None):  # noqa: E501
        """EPTransportSingleAllOfAttributes - a model defined in OpenAPI

        :param ip_address: The ip_address of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :type ip_address: IpAddress
        :param logical_interface_info: The logical_interface_info of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :type logical_interface_info: LogicalInterfaceInfo
        :param next_hop_info: The next_hop_info of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :type next_hop_info: str
        :param qos_profile: The qos_profile of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :type qos_profile: str
        :param ep_application_refs: The ep_application_refs of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :type ep_application_refs: List[str]
        """
        self.openapi_types = {
            'ip_address': IpAddress,
            'logical_interface_info': LogicalInterfaceInfo,
            'next_hop_info': str,
            'qos_profile': str,
            'ep_application_refs': List[str]
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'logical_interface_info': 'logicalInterfaceInfo',
            'next_hop_info': 'nextHopInfo',
            'qos_profile': 'qosProfile',
            'ep_application_refs': 'epApplicationRefs'
        }

        self._ip_address = ip_address
        self._logical_interface_info = logical_interface_info
        self._next_hop_info = next_hop_info
        self._qos_profile = qos_profile
        self._ep_application_refs = ep_application_refs

    @classmethod
    def from_dict(cls, dikt) -> 'EPTransportSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EP_Transport_Single_allOf_attributes of this EPTransportSingleAllOfAttributes.  # noqa: E501
        :rtype: EPTransportSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_address(self):
        """Gets the ip_address of this EPTransportSingleAllOfAttributes.


        :return: The ip_address of this EPTransportSingleAllOfAttributes.
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EPTransportSingleAllOfAttributes.


        :param ip_address: The ip_address of this EPTransportSingleAllOfAttributes.
        :type ip_address: IpAddress
        """

        self._ip_address = ip_address

    @property
    def logical_interface_info(self):
        """Gets the logical_interface_info of this EPTransportSingleAllOfAttributes.


        :return: The logical_interface_info of this EPTransportSingleAllOfAttributes.
        :rtype: LogicalInterfaceInfo
        """
        return self._logical_interface_info

    @logical_interface_info.setter
    def logical_interface_info(self, logical_interface_info):
        """Sets the logical_interface_info of this EPTransportSingleAllOfAttributes.


        :param logical_interface_info: The logical_interface_info of this EPTransportSingleAllOfAttributes.
        :type logical_interface_info: LogicalInterfaceInfo
        """

        self._logical_interface_info = logical_interface_info

    @property
    def next_hop_info(self):
        """Gets the next_hop_info of this EPTransportSingleAllOfAttributes.


        :return: The next_hop_info of this EPTransportSingleAllOfAttributes.
        :rtype: str
        """
        return self._next_hop_info

    @next_hop_info.setter
    def next_hop_info(self, next_hop_info):
        """Sets the next_hop_info of this EPTransportSingleAllOfAttributes.


        :param next_hop_info: The next_hop_info of this EPTransportSingleAllOfAttributes.
        :type next_hop_info: str
        """

        self._next_hop_info = next_hop_info

    @property
    def qos_profile(self):
        """Gets the qos_profile of this EPTransportSingleAllOfAttributes.


        :return: The qos_profile of this EPTransportSingleAllOfAttributes.
        :rtype: str
        """
        return self._qos_profile

    @qos_profile.setter
    def qos_profile(self, qos_profile):
        """Sets the qos_profile of this EPTransportSingleAllOfAttributes.


        :param qos_profile: The qos_profile of this EPTransportSingleAllOfAttributes.
        :type qos_profile: str
        """

        self._qos_profile = qos_profile

    @property
    def ep_application_refs(self):
        """Gets the ep_application_refs of this EPTransportSingleAllOfAttributes.


        :return: The ep_application_refs of this EPTransportSingleAllOfAttributes.
        :rtype: List[str]
        """
        return self._ep_application_refs

    @ep_application_refs.setter
    def ep_application_refs(self, ep_application_refs):
        """Sets the ep_application_refs of this EPTransportSingleAllOfAttributes.


        :param ep_application_refs: The ep_application_refs of this EPTransportSingleAllOfAttributes.
        :type ep_application_refs: List[str]
        """

        self._ep_application_refs = ep_application_refs
