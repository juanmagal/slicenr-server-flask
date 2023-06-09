# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.ns_info import NsInfo
from openapi_server.models.operational_state import OperationalState
from openapi_server.models.slice_profile import SliceProfile
from openapi_server import util

from openapi_server.models.administrative_state import AdministrativeState  # noqa: E501
from openapi_server.models.ns_info import NsInfo  # noqa: E501
from openapi_server.models.operational_state import OperationalState  # noqa: E501
from openapi_server.models.slice_profile import SliceProfile  # noqa: E501

class NetworkSliceSubnetSingleAllOfAttributesAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, managed_function_ref_list=None, network_slice_subnet_ref_list=None, operational_state=None, administrative_state=None, ns_info=None, slice_profile_list=None, ep_transport_ref_list=None, priority_label=None, network_slice_subnet_type=None):  # noqa: E501
        """NetworkSliceSubnetSingleAllOfAttributesAllOf - a model defined in OpenAPI

        :param managed_function_ref_list: The managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type managed_function_ref_list: List[str]
        :param network_slice_subnet_ref_list: The network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type network_slice_subnet_ref_list: List[str]
        :param operational_state: The operational_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type operational_state: OperationalState
        :param administrative_state: The administrative_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type administrative_state: AdministrativeState
        :param ns_info: The ns_info of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type ns_info: NsInfo
        :param slice_profile_list: The slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type slice_profile_list: List[SliceProfile]
        :param ep_transport_ref_list: The ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type ep_transport_ref_list: List[str]
        :param priority_label: The priority_label of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type priority_label: int
        :param network_slice_subnet_type: The network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :type network_slice_subnet_type: str
        """
        self.openapi_types = {
            'managed_function_ref_list': List[str],
            'network_slice_subnet_ref_list': List[str],
            'operational_state': OperationalState,
            'administrative_state': AdministrativeState,
            'ns_info': NsInfo,
            'slice_profile_list': List[SliceProfile],
            'ep_transport_ref_list': List[str],
            'priority_label': int,
            'network_slice_subnet_type': str
        }

        self.attribute_map = {
            'managed_function_ref_list': 'managedFunctionRefList',
            'network_slice_subnet_ref_list': 'networkSliceSubnetRefList',
            'operational_state': 'operationalState',
            'administrative_state': 'administrativeState',
            'ns_info': 'nsInfo',
            'slice_profile_list': 'sliceProfileList',
            'ep_transport_ref_list': 'epTransportRefList',
            'priority_label': 'priorityLabel',
            'network_slice_subnet_type': 'networkSliceSubnetType'
        }

        self._managed_function_ref_list = managed_function_ref_list
        self._network_slice_subnet_ref_list = network_slice_subnet_ref_list
        self._operational_state = operational_state
        self._administrative_state = administrative_state
        self._ns_info = ns_info
        self._slice_profile_list = slice_profile_list
        self._ep_transport_ref_list = ep_transport_ref_list
        self._priority_label = priority_label
        self._network_slice_subnet_type = network_slice_subnet_type

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkSliceSubnetSingleAllOfAttributesAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NetworkSliceSubnet_Single_allOf_attributes_allOf of this NetworkSliceSubnetSingleAllOfAttributesAllOf.  # noqa: E501
        :rtype: NetworkSliceSubnetSingleAllOfAttributesAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def managed_function_ref_list(self):
        """Gets the managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._managed_function_ref_list

    @managed_function_ref_list.setter
    def managed_function_ref_list(self, managed_function_ref_list):
        """Sets the managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param managed_function_ref_list: The managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type managed_function_ref_list: List[str]
        """

        self._managed_function_ref_list = managed_function_ref_list

    @property
    def network_slice_subnet_ref_list(self):
        """Gets the network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._network_slice_subnet_ref_list

    @network_slice_subnet_ref_list.setter
    def network_slice_subnet_ref_list(self, network_slice_subnet_ref_list):
        """Sets the network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param network_slice_subnet_ref_list: The network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type network_slice_subnet_ref_list: List[str]
        """

        self._network_slice_subnet_ref_list = network_slice_subnet_ref_list

    @property
    def operational_state(self):
        """Gets the operational_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The operational_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: OperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param operational_state: The operational_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type operational_state: OperationalState
        """

        self._operational_state = operational_state

    @property
    def administrative_state(self):
        """Gets the administrative_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The administrative_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: AdministrativeState
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state):
        """Sets the administrative_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param administrative_state: The administrative_state of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type administrative_state: AdministrativeState
        """

        self._administrative_state = administrative_state

    @property
    def ns_info(self):
        """Gets the ns_info of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The ns_info of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: NsInfo
        """
        return self._ns_info

    @ns_info.setter
    def ns_info(self, ns_info):
        """Sets the ns_info of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param ns_info: The ns_info of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type ns_info: NsInfo
        """

        self._ns_info = ns_info

    @property
    def slice_profile_list(self):
        """Gets the slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: List[SliceProfile]
        """
        return self._slice_profile_list

    @slice_profile_list.setter
    def slice_profile_list(self, slice_profile_list):
        """Sets the slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param slice_profile_list: The slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type slice_profile_list: List[SliceProfile]
        """

        self._slice_profile_list = slice_profile_list

    @property
    def ep_transport_ref_list(self):
        """Gets the ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: List[str]
        """
        return self._ep_transport_ref_list

    @ep_transport_ref_list.setter
    def ep_transport_ref_list(self, ep_transport_ref_list):
        """Sets the ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param ep_transport_ref_list: The ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type ep_transport_ref_list: List[str]
        """

        self._ep_transport_ref_list = ep_transport_ref_list

    @property
    def priority_label(self):
        """Gets the priority_label of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The priority_label of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param priority_label: The priority_label of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def network_slice_subnet_type(self):
        """Gets the network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :return: The network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :rtype: str
        """
        return self._network_slice_subnet_type

    @network_slice_subnet_type.setter
    def network_slice_subnet_type(self, network_slice_subnet_type):
        """Sets the network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributesAllOf.


        :param network_slice_subnet_type: The network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributesAllOf.
        :type network_slice_subnet_type: str
        """
        allowed_values = ["TOP_SLICESUBNET", "RAN_SLICESUBNET", "CN_SLICESUBNET"]  # noqa: E501
        if network_slice_subnet_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_slice_subnet_type` ({0}), must be one of {1}"
                .format(network_slice_subnet_type, allowed_values)
            )

        self._network_slice_subnet_type = network_slice_subnet_type
