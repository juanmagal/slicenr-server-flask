# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ProcessMonitor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_id=None, status=None, progress_percentage=None, progress_state_info=None, result_state_info=None, start_time=None, end_time=None, timer=None):  # noqa: E501
        """ProcessMonitor - a model defined in OpenAPI

        :param job_id: The job_id of this ProcessMonitor.  # noqa: E501
        :type job_id: str
        :param status: The status of this ProcessMonitor.  # noqa: E501
        :type status: str
        :param progress_percentage: The progress_percentage of this ProcessMonitor.  # noqa: E501
        :type progress_percentage: int
        :param progress_state_info: The progress_state_info of this ProcessMonitor.  # noqa: E501
        :type progress_state_info: str
        :param result_state_info: The result_state_info of this ProcessMonitor.  # noqa: E501
        :type result_state_info: str
        :param start_time: The start_time of this ProcessMonitor.  # noqa: E501
        :type start_time: datetime
        :param end_time: The end_time of this ProcessMonitor.  # noqa: E501
        :type end_time: datetime
        :param timer: The timer of this ProcessMonitor.  # noqa: E501
        :type timer: int
        """
        self.openapi_types = {
            'job_id': str,
            'status': str,
            'progress_percentage': int,
            'progress_state_info': str,
            'result_state_info': str,
            'start_time': datetime,
            'end_time': datetime,
            'timer': int
        }

        self.attribute_map = {
            'job_id': 'jobId',
            'status': 'status',
            'progress_percentage': 'progressPercentage',
            'progress_state_info': 'progressStateInfo',
            'result_state_info': 'resultStateInfo',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'timer': 'timer'
        }

        self._job_id = job_id
        self._status = status
        self._progress_percentage = progress_percentage
        self._progress_state_info = progress_state_info
        self._result_state_info = result_state_info
        self._start_time = start_time
        self._end_time = end_time
        self._timer = timer

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessMonitor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProcessMonitor of this ProcessMonitor.  # noqa: E501
        :rtype: ProcessMonitor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self):
        """Gets the job_id of this ProcessMonitor.


        :return: The job_id of this ProcessMonitor.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ProcessMonitor.


        :param job_id: The job_id of this ProcessMonitor.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ProcessMonitor.


        :return: The status of this ProcessMonitor.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProcessMonitor.


        :param status: The status of this ProcessMonitor.
        :type status: str
        """
        allowed_values = ["NOT_STARTED", "RUNNING", "FINSHED", "FAILED", "PARTIALLY_FAILED", "CANCELLING", "CANCELLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress_percentage(self):
        """Gets the progress_percentage of this ProcessMonitor.


        :return: The progress_percentage of this ProcessMonitor.
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        """Sets the progress_percentage of this ProcessMonitor.


        :param progress_percentage: The progress_percentage of this ProcessMonitor.
        :type progress_percentage: int
        """
        if progress_percentage is not None and progress_percentage > 100:  # noqa: E501
            raise ValueError("Invalid value for `progress_percentage`, must be a value less than or equal to `100`")  # noqa: E501
        if progress_percentage is not None and progress_percentage < 0:  # noqa: E501
            raise ValueError("Invalid value for `progress_percentage`, must be a value greater than or equal to `0`")  # noqa: E501

        self._progress_percentage = progress_percentage

    @property
    def progress_state_info(self):
        """Gets the progress_state_info of this ProcessMonitor.


        :return: The progress_state_info of this ProcessMonitor.
        :rtype: str
        """
        return self._progress_state_info

    @progress_state_info.setter
    def progress_state_info(self, progress_state_info):
        """Sets the progress_state_info of this ProcessMonitor.


        :param progress_state_info: The progress_state_info of this ProcessMonitor.
        :type progress_state_info: str
        """

        self._progress_state_info = progress_state_info

    @property
    def result_state_info(self):
        """Gets the result_state_info of this ProcessMonitor.


        :return: The result_state_info of this ProcessMonitor.
        :rtype: str
        """
        return self._result_state_info

    @result_state_info.setter
    def result_state_info(self, result_state_info):
        """Sets the result_state_info of this ProcessMonitor.


        :param result_state_info: The result_state_info of this ProcessMonitor.
        :type result_state_info: str
        """

        self._result_state_info = result_state_info

    @property
    def start_time(self):
        """Gets the start_time of this ProcessMonitor.


        :return: The start_time of this ProcessMonitor.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ProcessMonitor.


        :param start_time: The start_time of this ProcessMonitor.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ProcessMonitor.


        :return: The end_time of this ProcessMonitor.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ProcessMonitor.


        :param end_time: The end_time of this ProcessMonitor.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def timer(self):
        """Gets the timer of this ProcessMonitor.


        :return: The timer of this ProcessMonitor.
        :rtype: int
        """
        return self._timer

    @timer.setter
    def timer(self, timer):
        """Sets the timer of this ProcessMonitor.


        :param timer: The timer of this ProcessMonitor.
        :type timer: int
        """

        self._timer = timer