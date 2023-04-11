# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server import util

from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup  # noqa: E501

class ManagedElementAttr(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dn_prefix=None, managed_element_type_list=None, user_label=None, location_name=None, managed_by=None, vendor_name=None, user_defined_state=None, sw_version=None, priority_label=None, supported_perf_metric_groups=None, supported_trace_metrics=None):  # noqa: E501
        """ManagedElementAttr - a model defined in OpenAPI

        :param dn_prefix: The dn_prefix of this ManagedElementAttr.  # noqa: E501
        :type dn_prefix: str
        :param managed_element_type_list: The managed_element_type_list of this ManagedElementAttr.  # noqa: E501
        :type managed_element_type_list: List[str]
        :param user_label: The user_label of this ManagedElementAttr.  # noqa: E501
        :type user_label: str
        :param location_name: The location_name of this ManagedElementAttr.  # noqa: E501
        :type location_name: str
        :param managed_by: The managed_by of this ManagedElementAttr.  # noqa: E501
        :type managed_by: List[str]
        :param vendor_name: The vendor_name of this ManagedElementAttr.  # noqa: E501
        :type vendor_name: str
        :param user_defined_state: The user_defined_state of this ManagedElementAttr.  # noqa: E501
        :type user_defined_state: str
        :param sw_version: The sw_version of this ManagedElementAttr.  # noqa: E501
        :type sw_version: str
        :param priority_label: The priority_label of this ManagedElementAttr.  # noqa: E501
        :type priority_label: int
        :param supported_perf_metric_groups: The supported_perf_metric_groups of this ManagedElementAttr.  # noqa: E501
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        :param supported_trace_metrics: The supported_trace_metrics of this ManagedElementAttr.  # noqa: E501
        :type supported_trace_metrics: List[str]
        """
        self.openapi_types = {
            'dn_prefix': str,
            'managed_element_type_list': List[str],
            'user_label': str,
            'location_name': str,
            'managed_by': List[str],
            'vendor_name': str,
            'user_defined_state': str,
            'sw_version': str,
            'priority_label': int,
            'supported_perf_metric_groups': List[SupportedPerfMetricGroup],
            'supported_trace_metrics': List[str]
        }

        self.attribute_map = {
            'dn_prefix': 'dnPrefix',
            'managed_element_type_list': 'managedElementTypeList',
            'user_label': 'userLabel',
            'location_name': 'locationName',
            'managed_by': 'managedBy',
            'vendor_name': 'vendorName',
            'user_defined_state': 'userDefinedState',
            'sw_version': 'swVersion',
            'priority_label': 'priorityLabel',
            'supported_perf_metric_groups': 'supportedPerfMetricGroups',
            'supported_trace_metrics': 'supportedTraceMetrics'
        }

        self._dn_prefix = dn_prefix
        self._managed_element_type_list = managed_element_type_list
        self._user_label = user_label
        self._location_name = location_name
        self._managed_by = managed_by
        self._vendor_name = vendor_name
        self._user_defined_state = user_defined_state
        self._sw_version = sw_version
        self._priority_label = priority_label
        self._supported_perf_metric_groups = supported_perf_metric_groups
        self._supported_trace_metrics = supported_trace_metrics

    @classmethod
    def from_dict(cls, dikt) -> 'ManagedElementAttr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ManagedElement-Attr of this ManagedElementAttr.  # noqa: E501
        :rtype: ManagedElementAttr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dn_prefix(self):
        """Gets the dn_prefix of this ManagedElementAttr.


        :return: The dn_prefix of this ManagedElementAttr.
        :rtype: str
        """
        return self._dn_prefix

    @dn_prefix.setter
    def dn_prefix(self, dn_prefix):
        """Sets the dn_prefix of this ManagedElementAttr.


        :param dn_prefix: The dn_prefix of this ManagedElementAttr.
        :type dn_prefix: str
        """

        self._dn_prefix = dn_prefix

    @property
    def managed_element_type_list(self):
        """Gets the managed_element_type_list of this ManagedElementAttr.


        :return: The managed_element_type_list of this ManagedElementAttr.
        :rtype: List[str]
        """
        return self._managed_element_type_list

    @managed_element_type_list.setter
    def managed_element_type_list(self, managed_element_type_list):
        """Sets the managed_element_type_list of this ManagedElementAttr.


        :param managed_element_type_list: The managed_element_type_list of this ManagedElementAttr.
        :type managed_element_type_list: List[str]
        """

        self._managed_element_type_list = managed_element_type_list

    @property
    def user_label(self):
        """Gets the user_label of this ManagedElementAttr.


        :return: The user_label of this ManagedElementAttr.
        :rtype: str
        """
        return self._user_label

    @user_label.setter
    def user_label(self, user_label):
        """Sets the user_label of this ManagedElementAttr.


        :param user_label: The user_label of this ManagedElementAttr.
        :type user_label: str
        """

        self._user_label = user_label

    @property
    def location_name(self):
        """Gets the location_name of this ManagedElementAttr.


        :return: The location_name of this ManagedElementAttr.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this ManagedElementAttr.


        :param location_name: The location_name of this ManagedElementAttr.
        :type location_name: str
        """

        self._location_name = location_name

    @property
    def managed_by(self):
        """Gets the managed_by of this ManagedElementAttr.


        :return: The managed_by of this ManagedElementAttr.
        :rtype: List[str]
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this ManagedElementAttr.


        :param managed_by: The managed_by of this ManagedElementAttr.
        :type managed_by: List[str]
        """

        self._managed_by = managed_by

    @property
    def vendor_name(self):
        """Gets the vendor_name of this ManagedElementAttr.


        :return: The vendor_name of this ManagedElementAttr.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this ManagedElementAttr.


        :param vendor_name: The vendor_name of this ManagedElementAttr.
        :type vendor_name: str
        """

        self._vendor_name = vendor_name

    @property
    def user_defined_state(self):
        """Gets the user_defined_state of this ManagedElementAttr.


        :return: The user_defined_state of this ManagedElementAttr.
        :rtype: str
        """
        return self._user_defined_state

    @user_defined_state.setter
    def user_defined_state(self, user_defined_state):
        """Sets the user_defined_state of this ManagedElementAttr.


        :param user_defined_state: The user_defined_state of this ManagedElementAttr.
        :type user_defined_state: str
        """

        self._user_defined_state = user_defined_state

    @property
    def sw_version(self):
        """Gets the sw_version of this ManagedElementAttr.


        :return: The sw_version of this ManagedElementAttr.
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this ManagedElementAttr.


        :param sw_version: The sw_version of this ManagedElementAttr.
        :type sw_version: str
        """

        self._sw_version = sw_version

    @property
    def priority_label(self):
        """Gets the priority_label of this ManagedElementAttr.


        :return: The priority_label of this ManagedElementAttr.
        :rtype: int
        """
        return self._priority_label

    @priority_label.setter
    def priority_label(self, priority_label):
        """Sets the priority_label of this ManagedElementAttr.


        :param priority_label: The priority_label of this ManagedElementAttr.
        :type priority_label: int
        """

        self._priority_label = priority_label

    @property
    def supported_perf_metric_groups(self):
        """Gets the supported_perf_metric_groups of this ManagedElementAttr.


        :return: The supported_perf_metric_groups of this ManagedElementAttr.
        :rtype: List[SupportedPerfMetricGroup]
        """
        return self._supported_perf_metric_groups

    @supported_perf_metric_groups.setter
    def supported_perf_metric_groups(self, supported_perf_metric_groups):
        """Sets the supported_perf_metric_groups of this ManagedElementAttr.


        :param supported_perf_metric_groups: The supported_perf_metric_groups of this ManagedElementAttr.
        :type supported_perf_metric_groups: List[SupportedPerfMetricGroup]
        """

        self._supported_perf_metric_groups = supported_perf_metric_groups

    @property
    def supported_trace_metrics(self):
        """Gets the supported_trace_metrics of this ManagedElementAttr.


        :return: The supported_trace_metrics of this ManagedElementAttr.
        :rtype: List[str]
        """
        return self._supported_trace_metrics

    @supported_trace_metrics.setter
    def supported_trace_metrics(self, supported_trace_metrics):
        """Sets the supported_trace_metrics of this ManagedElementAttr.


        :param supported_trace_metrics: The supported_trace_metrics of this ManagedElementAttr.
        :type supported_trace_metrics: List[str]
        """

        self._supported_trace_metrics = supported_trace_metrics