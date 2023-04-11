# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.file_single import FileSingle
from openapi_server.models.file_single_all_of_attributes import FileSingleAllOfAttributes
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.heartbeat_control_single import HeartbeatControlSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_info_single import MnsInfoSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.alarm_list_single import AlarmListSingle  # noqa: E501
from openapi_server.models.file_download_job_single import FileDownloadJobSingle  # noqa: E501
from openapi_server.models.file_single import FileSingle  # noqa: E501
from openapi_server.models.file_single_all_of_attributes import FileSingleAllOfAttributes  # noqa: E501
from openapi_server.models.files_single import FilesSingle  # noqa: E501
from openapi_server.models.heartbeat_control_single import HeartbeatControlSingle  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle  # noqa: E501
from openapi_server.models.management_node_single import ManagementNodeSingle  # noqa: E501
from openapi_server.models.me_context_single import MeContextSingle  # noqa: E501
from openapi_server.models.mns_agent_single import MnsAgentSingle  # noqa: E501
from openapi_server.models.mns_info_single import MnsInfoSingle  # noqa: E501
from openapi_server.models.mns_registry_single import MnsRegistrySingle  # noqa: E501
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class ResourcesGenericNrm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, attributes=None, vs_data_container=None, object_class=None, object_instance=None, mns_agent=None, files=None, heartbeat_control=None, mns_info=None, mns_label=None, mns_type=None, mns_version=None, mns_address=None, mns_scope=None):  # noqa: E501
        """ResourcesGenericNrm - a model defined in OpenAPI

        :param id: The id of this ResourcesGenericNrm.  # noqa: E501
        :type id: str
        :param attributes: The attributes of this ResourcesGenericNrm.  # noqa: E501
        :type attributes: FileSingleAllOfAttributes
        :param vs_data_container: The vs_data_container of this ResourcesGenericNrm.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param object_class: The object_class of this ResourcesGenericNrm.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this ResourcesGenericNrm.  # noqa: E501
        :type object_instance: str
        :param mns_agent: The mns_agent of this ResourcesGenericNrm.  # noqa: E501
        :type mns_agent: List[MnsAgentSingle]
        :param files: The files of this ResourcesGenericNrm.  # noqa: E501
        :type files: List[FilesSingle]
        :param heartbeat_control: The heartbeat_control of this ResourcesGenericNrm.  # noqa: E501
        :type heartbeat_control: HeartbeatControlSingle
        :param mns_info: The mns_info of this ResourcesGenericNrm.  # noqa: E501
        :type mns_info: List[MnsInfoSingle]
        :param mns_label: The mns_label of this ResourcesGenericNrm.  # noqa: E501
        :type mns_label: str
        :param mns_type: The mns_type of this ResourcesGenericNrm.  # noqa: E501
        :type mns_type: str
        :param mns_version: The mns_version of this ResourcesGenericNrm.  # noqa: E501
        :type mns_version: str
        :param mns_address: The mns_address of this ResourcesGenericNrm.  # noqa: E501
        :type mns_address: str
        :param mns_scope: The mns_scope of this ResourcesGenericNrm.  # noqa: E501
        :type mns_scope: List[str]
        """
        self.openapi_types = {
            'id': str,
            'attributes': FileSingleAllOfAttributes,
            'vs_data_container': List[VsDataContainerSingle],
            'object_class': str,
            'object_instance': str,
            'mns_agent': List[MnsAgentSingle],
            'files': List[FilesSingle],
            'heartbeat_control': HeartbeatControlSingle,
            'mns_info': List[MnsInfoSingle],
            'mns_label': str,
            'mns_type': str,
            'mns_version': str,
            'mns_address': str,
            'mns_scope': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'attributes': 'attributes',
            'vs_data_container': 'VsDataContainer',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'mns_agent': 'MnsAgent',
            'files': 'Files',
            'heartbeat_control': 'HeartbeatControl',
            'mns_info': 'MnsInfo',
            'mns_label': 'mnsLabel',
            'mns_type': 'mnsType',
            'mns_version': 'mnsVersion',
            'mns_address': 'mnsAddress',
            'mns_scope': 'mnsScope'
        }

        self._id = id
        self._attributes = attributes
        self._vs_data_container = vs_data_container
        self._object_class = object_class
        self._object_instance = object_instance
        self._mns_agent = mns_agent
        self._files = files
        self._heartbeat_control = heartbeat_control
        self._mns_info = mns_info
        self._mns_label = mns_label
        self._mns_type = mns_type
        self._mns_version = mns_version
        self._mns_address = mns_address
        self._mns_scope = mns_scope

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcesGenericNrm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resources-genericNrm of this ResourcesGenericNrm.  # noqa: E501
        :rtype: ResourcesGenericNrm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ResourcesGenericNrm.


        :return: The id of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourcesGenericNrm.


        :param id: The id of this ResourcesGenericNrm.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this ResourcesGenericNrm.


        :return: The attributes of this ResourcesGenericNrm.
        :rtype: FileSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ResourcesGenericNrm.


        :param attributes: The attributes of this ResourcesGenericNrm.
        :type attributes: FileSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this ResourcesGenericNrm.


        :return: The vs_data_container of this ResourcesGenericNrm.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this ResourcesGenericNrm.


        :param vs_data_container: The vs_data_container of this ResourcesGenericNrm.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def object_class(self):
        """Gets the object_class of this ResourcesGenericNrm.


        :return: The object_class of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this ResourcesGenericNrm.


        :param object_class: The object_class of this ResourcesGenericNrm.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this ResourcesGenericNrm.


        :return: The object_instance of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this ResourcesGenericNrm.


        :param object_instance: The object_instance of this ResourcesGenericNrm.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def mns_agent(self):
        """Gets the mns_agent of this ResourcesGenericNrm.


        :return: The mns_agent of this ResourcesGenericNrm.
        :rtype: List[MnsAgentSingle]
        """
        return self._mns_agent

    @mns_agent.setter
    def mns_agent(self, mns_agent):
        """Sets the mns_agent of this ResourcesGenericNrm.


        :param mns_agent: The mns_agent of this ResourcesGenericNrm.
        :type mns_agent: List[MnsAgentSingle]
        """

        self._mns_agent = mns_agent

    @property
    def files(self):
        """Gets the files of this ResourcesGenericNrm.


        :return: The files of this ResourcesGenericNrm.
        :rtype: List[FilesSingle]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ResourcesGenericNrm.


        :param files: The files of this ResourcesGenericNrm.
        :type files: List[FilesSingle]
        """

        self._files = files

    @property
    def heartbeat_control(self):
        """Gets the heartbeat_control of this ResourcesGenericNrm.


        :return: The heartbeat_control of this ResourcesGenericNrm.
        :rtype: HeartbeatControlSingle
        """
        return self._heartbeat_control

    @heartbeat_control.setter
    def heartbeat_control(self, heartbeat_control):
        """Sets the heartbeat_control of this ResourcesGenericNrm.


        :param heartbeat_control: The heartbeat_control of this ResourcesGenericNrm.
        :type heartbeat_control: HeartbeatControlSingle
        """

        self._heartbeat_control = heartbeat_control

    @property
    def mns_info(self):
        """Gets the mns_info of this ResourcesGenericNrm.


        :return: The mns_info of this ResourcesGenericNrm.
        :rtype: List[MnsInfoSingle]
        """
        return self._mns_info

    @mns_info.setter
    def mns_info(self, mns_info):
        """Sets the mns_info of this ResourcesGenericNrm.


        :param mns_info: The mns_info of this ResourcesGenericNrm.
        :type mns_info: List[MnsInfoSingle]
        """

        self._mns_info = mns_info

    @property
    def mns_label(self):
        """Gets the mns_label of this ResourcesGenericNrm.


        :return: The mns_label of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._mns_label

    @mns_label.setter
    def mns_label(self, mns_label):
        """Sets the mns_label of this ResourcesGenericNrm.


        :param mns_label: The mns_label of this ResourcesGenericNrm.
        :type mns_label: str
        """

        self._mns_label = mns_label

    @property
    def mns_type(self):
        """Gets the mns_type of this ResourcesGenericNrm.


        :return: The mns_type of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._mns_type

    @mns_type.setter
    def mns_type(self, mns_type):
        """Sets the mns_type of this ResourcesGenericNrm.


        :param mns_type: The mns_type of this ResourcesGenericNrm.
        :type mns_type: str
        """
        allowed_values = ["ProvMnS", "FaultSupervisionMnS", "StreamingDataReportingMnS", "FileDataReportingMnS"]  # noqa: E501
        if mns_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mns_type` ({0}), must be one of {1}"
                .format(mns_type, allowed_values)
            )

        self._mns_type = mns_type

    @property
    def mns_version(self):
        """Gets the mns_version of this ResourcesGenericNrm.


        :return: The mns_version of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._mns_version

    @mns_version.setter
    def mns_version(self, mns_version):
        """Sets the mns_version of this ResourcesGenericNrm.


        :param mns_version: The mns_version of this ResourcesGenericNrm.
        :type mns_version: str
        """

        self._mns_version = mns_version

    @property
    def mns_address(self):
        """Gets the mns_address of this ResourcesGenericNrm.


        :return: The mns_address of this ResourcesGenericNrm.
        :rtype: str
        """
        return self._mns_address

    @mns_address.setter
    def mns_address(self, mns_address):
        """Sets the mns_address of this ResourcesGenericNrm.


        :param mns_address: The mns_address of this ResourcesGenericNrm.
        :type mns_address: str
        """

        self._mns_address = mns_address

    @property
    def mns_scope(self):
        """Gets the mns_scope of this ResourcesGenericNrm.

        List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork.  # noqa: E501

        :return: The mns_scope of this ResourcesGenericNrm.
        :rtype: List[str]
        """
        return self._mns_scope

    @mns_scope.setter
    def mns_scope(self, mns_scope):
        """Sets the mns_scope of this ResourcesGenericNrm.

        List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork.  # noqa: E501

        :param mns_scope: The mns_scope of this ResourcesGenericNrm.
        :type mns_scope: List[str]
        """

        self._mns_scope = mns_scope