# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.threshold_level_ind import ThresholdLevelInd
from openapi_server import util

from openapi_server.models.threshold_level_ind import ThresholdLevelInd  # noqa: E501

class ThresholdMeasurementInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, observed_measurement=None, observed_value=None, threshold_level=None, arm_time=None):  # noqa: E501
        """ThresholdMeasurementInfo - a model defined in OpenAPI

        :param observed_measurement: The observed_measurement of this ThresholdMeasurementInfo.  # noqa: E501
        :type observed_measurement: str
        :param observed_value: The observed_value of this ThresholdMeasurementInfo.  # noqa: E501
        :type observed_value: float
        :param threshold_level: The threshold_level of this ThresholdMeasurementInfo.  # noqa: E501
        :type threshold_level: ThresholdLevelInd
        :param arm_time: The arm_time of this ThresholdMeasurementInfo.  # noqa: E501
        :type arm_time: datetime
        """
        self.openapi_types = {
            'observed_measurement': str,
            'observed_value': float,
            'threshold_level': ThresholdLevelInd,
            'arm_time': datetime
        }

        self.attribute_map = {
            'observed_measurement': 'observedMeasurement',
            'observed_value': 'observedValue',
            'threshold_level': 'thresholdLevel',
            'arm_time': 'armTime'
        }

        self._observed_measurement = observed_measurement
        self._observed_value = observed_value
        self._threshold_level = threshold_level
        self._arm_time = arm_time

    @classmethod
    def from_dict(cls, dikt) -> 'ThresholdMeasurementInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ThresholdMeasurementInfo of this ThresholdMeasurementInfo.  # noqa: E501
        :rtype: ThresholdMeasurementInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def observed_measurement(self):
        """Gets the observed_measurement of this ThresholdMeasurementInfo.


        :return: The observed_measurement of this ThresholdMeasurementInfo.
        :rtype: str
        """
        return self._observed_measurement

    @observed_measurement.setter
    def observed_measurement(self, observed_measurement):
        """Sets the observed_measurement of this ThresholdMeasurementInfo.


        :param observed_measurement: The observed_measurement of this ThresholdMeasurementInfo.
        :type observed_measurement: str
        """
        if observed_measurement is None:
            raise ValueError("Invalid value for `observed_measurement`, must not be `None`")  # noqa: E501

        self._observed_measurement = observed_measurement

    @property
    def observed_value(self):
        """Gets the observed_value of this ThresholdMeasurementInfo.


        :return: The observed_value of this ThresholdMeasurementInfo.
        :rtype: float
        """
        return self._observed_value

    @observed_value.setter
    def observed_value(self, observed_value):
        """Sets the observed_value of this ThresholdMeasurementInfo.


        :param observed_value: The observed_value of this ThresholdMeasurementInfo.
        :type observed_value: float
        """
        if observed_value is None:
            raise ValueError("Invalid value for `observed_value`, must not be `None`")  # noqa: E501

        self._observed_value = observed_value

    @property
    def threshold_level(self):
        """Gets the threshold_level of this ThresholdMeasurementInfo.


        :return: The threshold_level of this ThresholdMeasurementInfo.
        :rtype: ThresholdLevelInd
        """
        return self._threshold_level

    @threshold_level.setter
    def threshold_level(self, threshold_level):
        """Sets the threshold_level of this ThresholdMeasurementInfo.


        :param threshold_level: The threshold_level of this ThresholdMeasurementInfo.
        :type threshold_level: ThresholdLevelInd
        """

        self._threshold_level = threshold_level

    @property
    def arm_time(self):
        """Gets the arm_time of this ThresholdMeasurementInfo.


        :return: The arm_time of this ThresholdMeasurementInfo.
        :rtype: datetime
        """
        return self._arm_time

    @arm_time.setter
    def arm_time(self, arm_time):
        """Sets the arm_time of this ThresholdMeasurementInfo.


        :param arm_time: The arm_time of this ThresholdMeasurementInfo.
        :type arm_time: datetime
        """

        self._arm_time = arm_time