# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.upf_function_single_all_of_attributes import UpfFunctionSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle
from openapi_server import util

from openapi_server.models.epn3_single import EPN3Single  # noqa: E501
from openapi_server.models.epn4_single import EPN4Single  # noqa: E501
from openapi_server.models.epn6_single import EPN6Single  # noqa: E501
from openapi_server.models.epn9_single import EPN9Single  # noqa: E501
from openapi_server.models.eps5_u_single import EPS5USingle  # noqa: E501
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle  # noqa: E501
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle  # noqa: E501
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle  # noqa: E501
from openapi_server.models.trace_job_single import TraceJobSingle  # noqa: E501
from openapi_server.models.upf_function_single_all_of_attributes import UpfFunctionSingleAllOfAttributes  # noqa: E501
from openapi_server.models.vs_data_container_single import VsDataContainerSingle  # noqa: E501

class UpfFunctionSingle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, object_class=None, object_instance=None, vs_data_container=None, attributes=None, perf_metric_job=None, threshold_monitor=None, managed_nf_service=None, trace_job=None, ep_n3=None, ep_n4=None, ep_n6=None, ep_n9=None, ep_s5_u=None):  # noqa: E501
        """UpfFunctionSingle - a model defined in OpenAPI

        :param id: The id of this UpfFunctionSingle.  # noqa: E501
        :type id: str
        :param object_class: The object_class of this UpfFunctionSingle.  # noqa: E501
        :type object_class: str
        :param object_instance: The object_instance of this UpfFunctionSingle.  # noqa: E501
        :type object_instance: str
        :param vs_data_container: The vs_data_container of this UpfFunctionSingle.  # noqa: E501
        :type vs_data_container: List[VsDataContainerSingle]
        :param attributes: The attributes of this UpfFunctionSingle.  # noqa: E501
        :type attributes: UpfFunctionSingleAllOfAttributes
        :param perf_metric_job: The perf_metric_job of this UpfFunctionSingle.  # noqa: E501
        :type perf_metric_job: List[PerfMetricJobSingle]
        :param threshold_monitor: The threshold_monitor of this UpfFunctionSingle.  # noqa: E501
        :type threshold_monitor: List[ThresholdMonitorSingle]
        :param managed_nf_service: The managed_nf_service of this UpfFunctionSingle.  # noqa: E501
        :type managed_nf_service: List[ManagedNFServiceSingle]
        :param trace_job: The trace_job of this UpfFunctionSingle.  # noqa: E501
        :type trace_job: List[TraceJobSingle]
        :param ep_n3: The ep_n3 of this UpfFunctionSingle.  # noqa: E501
        :type ep_n3: List[EPN3Single]
        :param ep_n4: The ep_n4 of this UpfFunctionSingle.  # noqa: E501
        :type ep_n4: List[EPN4Single]
        :param ep_n6: The ep_n6 of this UpfFunctionSingle.  # noqa: E501
        :type ep_n6: List[EPN6Single]
        :param ep_n9: The ep_n9 of this UpfFunctionSingle.  # noqa: E501
        :type ep_n9: List[EPN9Single]
        :param ep_s5_u: The ep_s5_u of this UpfFunctionSingle.  # noqa: E501
        :type ep_s5_u: List[EPS5USingle]
        """
        self.openapi_types = {
            'id': str,
            'object_class': str,
            'object_instance': str,
            'vs_data_container': List[VsDataContainerSingle],
            'attributes': UpfFunctionSingleAllOfAttributes,
            'perf_metric_job': List[PerfMetricJobSingle],
            'threshold_monitor': List[ThresholdMonitorSingle],
            'managed_nf_service': List[ManagedNFServiceSingle],
            'trace_job': List[TraceJobSingle],
            'ep_n3': List[EPN3Single],
            'ep_n4': List[EPN4Single],
            'ep_n6': List[EPN6Single],
            'ep_n9': List[EPN9Single],
            'ep_s5_u': List[EPS5USingle]
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
            'ep_n3': 'EP_N3',
            'ep_n4': 'EP_N4',
            'ep_n6': 'EP_N6',
            'ep_n9': 'EP_N9',
            'ep_s5_u': 'EP_S5U'
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
        self._ep_n3 = ep_n3
        self._ep_n4 = ep_n4
        self._ep_n6 = ep_n6
        self._ep_n9 = ep_n9
        self._ep_s5_u = ep_s5_u

    @classmethod
    def from_dict(cls, dikt) -> 'UpfFunctionSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpfFunction-Single of this UpfFunctionSingle.  # noqa: E501
        :rtype: UpfFunctionSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this UpfFunctionSingle.


        :return: The id of this UpfFunctionSingle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpfFunctionSingle.


        :param id: The id of this UpfFunctionSingle.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def object_class(self):
        """Gets the object_class of this UpfFunctionSingle.


        :return: The object_class of this UpfFunctionSingle.
        :rtype: str
        """
        return self._object_class

    @object_class.setter
    def object_class(self, object_class):
        """Sets the object_class of this UpfFunctionSingle.


        :param object_class: The object_class of this UpfFunctionSingle.
        :type object_class: str
        """

        self._object_class = object_class

    @property
    def object_instance(self):
        """Gets the object_instance of this UpfFunctionSingle.


        :return: The object_instance of this UpfFunctionSingle.
        :rtype: str
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """Sets the object_instance of this UpfFunctionSingle.


        :param object_instance: The object_instance of this UpfFunctionSingle.
        :type object_instance: str
        """

        self._object_instance = object_instance

    @property
    def vs_data_container(self):
        """Gets the vs_data_container of this UpfFunctionSingle.


        :return: The vs_data_container of this UpfFunctionSingle.
        :rtype: List[VsDataContainerSingle]
        """
        return self._vs_data_container

    @vs_data_container.setter
    def vs_data_container(self, vs_data_container):
        """Sets the vs_data_container of this UpfFunctionSingle.


        :param vs_data_container: The vs_data_container of this UpfFunctionSingle.
        :type vs_data_container: List[VsDataContainerSingle]
        """

        self._vs_data_container = vs_data_container

    @property
    def attributes(self):
        """Gets the attributes of this UpfFunctionSingle.


        :return: The attributes of this UpfFunctionSingle.
        :rtype: UpfFunctionSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpfFunctionSingle.


        :param attributes: The attributes of this UpfFunctionSingle.
        :type attributes: UpfFunctionSingleAllOfAttributes
        """

        self._attributes = attributes

    @property
    def perf_metric_job(self):
        """Gets the perf_metric_job of this UpfFunctionSingle.


        :return: The perf_metric_job of this UpfFunctionSingle.
        :rtype: List[PerfMetricJobSingle]
        """
        return self._perf_metric_job

    @perf_metric_job.setter
    def perf_metric_job(self, perf_metric_job):
        """Sets the perf_metric_job of this UpfFunctionSingle.


        :param perf_metric_job: The perf_metric_job of this UpfFunctionSingle.
        :type perf_metric_job: List[PerfMetricJobSingle]
        """

        self._perf_metric_job = perf_metric_job

    @property
    def threshold_monitor(self):
        """Gets the threshold_monitor of this UpfFunctionSingle.


        :return: The threshold_monitor of this UpfFunctionSingle.
        :rtype: List[ThresholdMonitorSingle]
        """
        return self._threshold_monitor

    @threshold_monitor.setter
    def threshold_monitor(self, threshold_monitor):
        """Sets the threshold_monitor of this UpfFunctionSingle.


        :param threshold_monitor: The threshold_monitor of this UpfFunctionSingle.
        :type threshold_monitor: List[ThresholdMonitorSingle]
        """

        self._threshold_monitor = threshold_monitor

    @property
    def managed_nf_service(self):
        """Gets the managed_nf_service of this UpfFunctionSingle.


        :return: The managed_nf_service of this UpfFunctionSingle.
        :rtype: List[ManagedNFServiceSingle]
        """
        return self._managed_nf_service

    @managed_nf_service.setter
    def managed_nf_service(self, managed_nf_service):
        """Sets the managed_nf_service of this UpfFunctionSingle.


        :param managed_nf_service: The managed_nf_service of this UpfFunctionSingle.
        :type managed_nf_service: List[ManagedNFServiceSingle]
        """

        self._managed_nf_service = managed_nf_service

    @property
    def trace_job(self):
        """Gets the trace_job of this UpfFunctionSingle.


        :return: The trace_job of this UpfFunctionSingle.
        :rtype: List[TraceJobSingle]
        """
        return self._trace_job

    @trace_job.setter
    def trace_job(self, trace_job):
        """Sets the trace_job of this UpfFunctionSingle.


        :param trace_job: The trace_job of this UpfFunctionSingle.
        :type trace_job: List[TraceJobSingle]
        """

        self._trace_job = trace_job

    @property
    def ep_n3(self):
        """Gets the ep_n3 of this UpfFunctionSingle.


        :return: The ep_n3 of this UpfFunctionSingle.
        :rtype: List[EPN3Single]
        """
        return self._ep_n3

    @ep_n3.setter
    def ep_n3(self, ep_n3):
        """Sets the ep_n3 of this UpfFunctionSingle.


        :param ep_n3: The ep_n3 of this UpfFunctionSingle.
        :type ep_n3: List[EPN3Single]
        """

        self._ep_n3 = ep_n3

    @property
    def ep_n4(self):
        """Gets the ep_n4 of this UpfFunctionSingle.


        :return: The ep_n4 of this UpfFunctionSingle.
        :rtype: List[EPN4Single]
        """
        return self._ep_n4

    @ep_n4.setter
    def ep_n4(self, ep_n4):
        """Sets the ep_n4 of this UpfFunctionSingle.


        :param ep_n4: The ep_n4 of this UpfFunctionSingle.
        :type ep_n4: List[EPN4Single]
        """

        self._ep_n4 = ep_n4

    @property
    def ep_n6(self):
        """Gets the ep_n6 of this UpfFunctionSingle.


        :return: The ep_n6 of this UpfFunctionSingle.
        :rtype: List[EPN6Single]
        """
        return self._ep_n6

    @ep_n6.setter
    def ep_n6(self, ep_n6):
        """Sets the ep_n6 of this UpfFunctionSingle.


        :param ep_n6: The ep_n6 of this UpfFunctionSingle.
        :type ep_n6: List[EPN6Single]
        """

        self._ep_n6 = ep_n6

    @property
    def ep_n9(self):
        """Gets the ep_n9 of this UpfFunctionSingle.


        :return: The ep_n9 of this UpfFunctionSingle.
        :rtype: List[EPN9Single]
        """
        return self._ep_n9

    @ep_n9.setter
    def ep_n9(self, ep_n9):
        """Sets the ep_n9 of this UpfFunctionSingle.


        :param ep_n9: The ep_n9 of this UpfFunctionSingle.
        :type ep_n9: List[EPN9Single]
        """

        self._ep_n9 = ep_n9

    @property
    def ep_s5_u(self):
        """Gets the ep_s5_u of this UpfFunctionSingle.


        :return: The ep_s5_u of this UpfFunctionSingle.
        :rtype: List[EPS5USingle]
        """
        return self._ep_s5_u

    @ep_s5_u.setter
    def ep_s5_u(self, ep_s5_u):
        """Sets the ep_s5_u of this UpfFunctionSingle.


        :param ep_s5_u: The ep_s5_u of this UpfFunctionSingle.
        :type ep_s5_u: List[EPS5USingle]
        """

        self._ep_s5_u = ep_s5_u
