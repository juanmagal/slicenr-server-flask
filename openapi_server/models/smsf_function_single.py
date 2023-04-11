# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn21_single import EPN21Single
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.smsf_function_single_all_of_attributes import SmsfFunctionSingleAllOfAttributes
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle  # noqa: E501
from openapi_server.models.epn20_single import EPN20Single  # noqa: E501
from openapi_server.models.epn21_single import EPN21Single  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.smsf_function_single_all_of_attributes import SmsfFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class SmsfFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None, ep_n20=None, ep_n21=None, ep_map_smsc=None):  # noqa: E501
        """SmsfFunctionSingle - a model defined in OpenAPI

        :param id: The id of this SmsfFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this SmsfFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this SmsfFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this SmsfFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this SmsfFunctionSingle.  # noqa: E501
        :type attributes: SmsfFunctionSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this SmsfFunctionSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this SmsfFunctionSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this SmsfFunctionSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this SmsfFunctionSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ep_n20: The ep_n20 of this SmsfFunctionSingle.  # noqa: E501
        :type ep_n20: List[EPN20Single]
        :param ep_n21: The ep_n21 of this SmsfFunctionSingle.  # noqa: E501
        :type ep_n21: List[EPN21Single]
        :param ep_map_smsc: The ep_map_smsc of this SmsfFunctionSingle.  # noqa: E501
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': SmsfFunctionSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle],
            'ep_n20': List[EPN20Single],
            'ep_n21': List[EPN21Single],
            'ep_map_smsc': List[EPMAPSMSCSingle]
        }

        self.attribute_map = {
            'id': 'id',
            'object_class': 'objectClass',
            'object_instance': 'objectInstance',
            'vs_data_container': 'VsDataContainer',
            'attributes': 'attributes',
            'perf_metric_job': 'PerfMetricJob',
            'threshold_monitor': 'ThresholdMonitor',
            'managed_nf_service': 'ManagedNFService',
            'trace_job': 'TraceJob',
            'ep_n20': 'EP_N20',
            'ep_n21': 'EP_N21',
            'ep_map_smsc': 'EP_MAP_SMSC'
        }

        self._id = id
        self._object_class = object_class
        self._object_instance = object_instance
        self._vs_data_container = vs_data_container
        self._attributes = attributes
        self._perf_metric_job = perf_metric_job
        self._threshold_monitor = threshold_monitor
        self._managed_nf_service = managed_nf_service
        self._trace_job = trace_job
        self._ep_n20 = ep_n20
        self._ep_n21 = ep_n21
        self._ep_map_smsc = ep_map_smsc

    @classmethod
    def from_dict(cls, dikt) -> 'SmsfFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmsfFunction-Single of this SmsfFunctionSingle.  # noqa: E501
        :rtype: SmsfFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SmsfFunctionSingle.


        :return: The id of this SmsfFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmsfFunctionSingle.


        :param id: The id of this SmsfFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this SmsfFunctionSingle.


        :return: The object_class of this SmsfFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this SmsfFunctionSingle.


        :param object_class: The object_class of this SmsfFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this SmsfFunctionSingle.


        :return: The object_instance of this SmsfFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this SmsfFunctionSingle.


        :param object_instance: The object_instance of this SmsfFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this SmsfFunctionSingle.


        :return: The vs_data_container of this SmsfFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this SmsfFunctionSingle.


        :param vs_data_container: The vs_data_container of this SmsfFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this SmsfFunctionSingle.


        :return: The attributes of this SmsfFunctionSingle.
        :rtype: SmsfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SmsfFunctionSingle.


        :param attributes: The attributes of this SmsfFunctionSingle.
        :type attributes: SmsfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this SmsfFunctionSingle.


        :return: The perf_metric_job of this SmsfFunctionSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this SmsfFunctionSingle.


        :param perf_metric_job: The perf_metric_job of this SmsfFunctionSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this SmsfFunctionSingle.


        :return: The threshold_monitor of this SmsfFunctionSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this SmsfFunctionSingle.


        :param threshold_monitor: The threshold_monitor of this SmsfFunctionSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this SmsfFunctionSingle.


        :return: The managed_nf_service of this SmsfFunctionSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this SmsfFunctionSingle.


        :param managed_nf_service: The managed_nf_service of this SmsfFunctionSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this SmsfFunctionSingle.


        :return: The trace_job of this SmsfFunctionSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this SmsfFunctionSingle.


        :param trace_job: The trace_job of this SmsfFunctionSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ep_n20(self):
        """Gets the ep_n20 of this SmsfFunctionSingle.


        :return: The ep_n20 of this SmsfFunctionSingle.
        :rtype: List[EPN20Single]
        """
        return self._ep_n20

    @ep_n20.setter
    def ep_n20(self, ep_n20):
        """Sets the ep_n20 of this SmsfFunctionSingle.


        :param ep_n20: The ep_n20 of this SmsfFunctionSingle.
        :type ep_n20: List[EPN20Single]
        """

        self._ep_n20 = ep_n20

    @property
    def ep_n21(self):
        """Gets the ep_n21 of this SmsfFunctionSingle.


        :return: The ep_n21 of this SmsfFunctionSingle.
        :rtype: List[EPN21Single]
        """
        return self._ep_n21

    @ep_n21.setter
    def ep_n21(self, ep_n21):
        """Sets the ep_n21 of this SmsfFunctionSingle.


        :param ep_n21: The ep_n21 of this SmsfFunctionSingle.
        :type ep_n21: List[EPN21Single]
        """

        self._ep_n21 = ep_n21

    @property
    def ep_map_smsc(self):
        """Gets the ep_map_smsc of this SmsfFunctionSingle.


        :return: The ep_map_smsc of this SmsfFunctionSingle.
        :rtype: List[EPMAPSMSCSingle]
        """
        return self._ep_map_smsc

    @ep_map_smsc.setter
    def ep_map_smsc(self, ep_map_smsc):
        """Sets the ep_map_smsc of this SmsfFunctionSingle.


        :param ep_map_smsc: The ep_map_smsc of this SmsfFunctionSingle.
        :type ep_map_smsc: List[EPMAPSMSCSingle]
        """

        self._ep_map_smsc = ep_map_smsc