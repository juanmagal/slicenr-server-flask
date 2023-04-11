# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn33_single import EPN33Single
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.nef_function_single_all_of_attributes import NefFunctionSingleAllOfAttributes
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.epn33_single import EPN33Single  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.nef_function_single_all_of_attributes import NefFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class NefFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None, ep_n33=None):  # noqa: E501
        """NefFunctionSingle - a model defined in OpenAPI

        :param id: The id of this NefFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this NefFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this NefFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this NefFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this NefFunctionSingle.  # noqa: E501
        :type attributes: NefFunctionSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this NefFunctionSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this NefFunctionSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this NefFunctionSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this NefFunctionSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ep_n33: The ep_n33 of this NefFunctionSingle.  # noqa: E501
        :type ep_n33: List[EPN33Single]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': NefFunctionSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle],
            'ep_n33': List[EPN33Single]
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
            'ep_n33': 'EP_N33'
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
        self._ep_n33 = ep_n33

    @classmethod
    def from_dict(cls, dikt) -> 'NefFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NefFunction-Single of this NefFunctionSingle.  # noqa: E501
        :rtype: NefFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this NefFunctionSingle.


        :return: The id of this NefFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NefFunctionSingle.


        :param id: The id of this NefFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this NefFunctionSingle.


        :return: The object_class of this NefFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this NefFunctionSingle.


        :param object_class: The object_class of this NefFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this NefFunctionSingle.


        :return: The object_instance of this NefFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this NefFunctionSingle.


        :param object_instance: The object_instance of this NefFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this NefFunctionSingle.


        :return: The vs_data_container of this NefFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this NefFunctionSingle.


        :param vs_data_container: The vs_data_container of this NefFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this NefFunctionSingle.


        :return: The attributes of this NefFunctionSingle.
        :rtype: NefFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NefFunctionSingle.


        :param attributes: The attributes of this NefFunctionSingle.
        :type attributes: NefFunctionSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this NefFunctionSingle.


        :return: The perf_metric_job of this NefFunctionSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this NefFunctionSingle.


        :param perf_metric_job: The perf_metric_job of this NefFunctionSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this NefFunctionSingle.


        :return: The threshold_monitor of this NefFunctionSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this NefFunctionSingle.


        :param threshold_monitor: The threshold_monitor of this NefFunctionSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this NefFunctionSingle.


        :return: The managed_nf_service of this NefFunctionSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this NefFunctionSingle.


        :param managed_nf_service: The managed_nf_service of this NefFunctionSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this NefFunctionSingle.


        :return: The trace_job of this NefFunctionSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this NefFunctionSingle.


        :param trace_job: The trace_job of this NefFunctionSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ep_n33(self):
        """Gets the ep_n33 of this NefFunctionSingle.


        :return: The ep_n33 of this NefFunctionSingle.
        :rtype: List[EPN33Single]
        """
        return self._ep_n33

    @ep_n33.setter
    def ep_n33(self, ep_n33):
        """Sets the ep_n33 of this NefFunctionSingle.


        :param ep_n33: The ep_n33 of this NefFunctionSingle.
        :type ep_n33: List[EPN33Single]
        """

        self._ep_n33 = ep_n33
