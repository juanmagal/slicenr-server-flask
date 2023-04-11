# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InterRatEsActivationCandidateCellParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, load_threshold=None, time_duration=None):  # noqa: E501
        """InterRatEsActivationCandidateCellParameters - a model defined in OpenAPI

        :param load_threshold: The load_threshold of this InterRatEsActivationCandidateCellParameters.  # noqa: E501
        :type load_threshold: int
        :param time_duration: The time_duration of this InterRatEsActivationCandidateCellParameters.  # noqa: E501
        :type time_duration: int
        """
        self.openapi_types = {
            'load_threshold': int,
            'time_duration': int
        }

        self.attribute_map = {
            'load_threshold': 'loadThreshold',
            'time_duration': 'timeDuration'
        }

        self._load_threshold = load_threshold
        self._time_duration = time_duration

    @classmethod
    def from_dict(cls, dikt) -> 'InterRatEsActivationCandidateCellParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterRatEsActivationCandidateCellParameters of this InterRatEsActivationCandidateCellParameters.  # noqa: E501
        :rtype: InterRatEsActivationCandidateCellParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def load_threshold(self):
        """Gets the load_threshold of this InterRatEsActivationCandidateCellParameters.


        :return: The load_threshold of this InterRatEsActivationCandidateCellParameters.
        :rtype: int
        """
        return self._load_threshold

    @load_threshold.setter
    def load_threshold(self, load_threshold):
        """Sets the load_threshold of this InterRatEsActivationCandidateCellParameters.


        :param load_threshold: The load_threshold of this InterRatEsActivationCandidateCellParameters.
        :type load_threshold: int
        """

        self._load_threshold = load_threshold

    @property
    def time_duration(self):
        """Gets the time_duration of this InterRatEsActivationCandidateCellParameters.


        :return: The time_duration of this InterRatEsActivationCandidateCellParameters.
        :rtype: int
        """
        return self._time_duration

    @time_duration.setter
    def time_duration(self, time_duration):
        """Sets the time_duration of this InterRatEsActivationCandidateCellParameters.


        :param time_duration: The time_duration of this InterRatEsActivationCandidateCellParameters.
        :type time_duration: int
        """

        self._time_duration = time_duration