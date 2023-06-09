# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ExcessPacketDelayThresholdsType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, five_qi_value=None, excess_packet_delay_threshold_value=None):  # noqa: E501
        """ExcessPacketDelayThresholdsType - a model defined in OpenAPI

        :param five_qi_value: The five_qi_value of this ExcessPacketDelayThresholdsType.  # noqa: E501
        :type five_qi_value: int
        :param excess_packet_delay_threshold_value: The excess_packet_delay_threshold_value of this ExcessPacketDelayThresholdsType.  # noqa: E501
        :type excess_packet_delay_threshold_value: str
        """
        self.openapi_types = {
            'five_qi_value': int,
            'excess_packet_delay_threshold_value': str
        }

        self.attribute_map = {
            'five_qi_value': 'fiveQIValue',
            'excess_packet_delay_threshold_value': 'excessPacketDelayThresholdValue'
        }

        self._five_qi_value = five_qi_value
        self._excess_packet_delay_threshold_value = excess_packet_delay_threshold_value

    @classmethod
    def from_dict(cls, dikt) -> 'ExcessPacketDelayThresholdsType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The excessPacketDelayThresholds-Type of this ExcessPacketDelayThresholdsType.  # noqa: E501
        :rtype: ExcessPacketDelayThresholdsType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def five_qi_value(self):
        """Gets the five_qi_value of this ExcessPacketDelayThresholdsType.


        :return: The five_qi_value of this ExcessPacketDelayThresholdsType.
        :rtype: int
        """
        return self._five_qi_value

    @five_qi_value.setter
    def five_qi_value(self, five_qi_value):
        """Sets the five_qi_value of this ExcessPacketDelayThresholdsType.


        :param five_qi_value: The five_qi_value of this ExcessPacketDelayThresholdsType.
        :type five_qi_value: int
        """

        self._five_qi_value = five_qi_value

    @property
    def excess_packet_delay_threshold_value(self):
        """Gets the excess_packet_delay_threshold_value of this ExcessPacketDelayThresholdsType.


        :return: The excess_packet_delay_threshold_value of this ExcessPacketDelayThresholdsType.
        :rtype: str
        """
        return self._excess_packet_delay_threshold_value

    @excess_packet_delay_threshold_value.setter
    def excess_packet_delay_threshold_value(self, excess_packet_delay_threshold_value):
        """Sets the excess_packet_delay_threshold_value of this ExcessPacketDelayThresholdsType.


        :param excess_packet_delay_threshold_value: The excess_packet_delay_threshold_value of this ExcessPacketDelayThresholdsType.
        :type excess_packet_delay_threshold_value: str
        """
        allowed_values = ["0.25ms", "0.5ms", "1ms", "2ms", "4ms", "5ms", "10ms", "20ms", "30ms", "40ms", "50ms", "60ms", "70ms", "80ms", "90ms", "100ms", "150ms", "300ms", "500ms"]  # noqa: E501
        if excess_packet_delay_threshold_value not in allowed_values:
            raise ValueError(
                "Invalid value for `excess_packet_delay_threshold_value` ({0}), must be one of {1}"
                .format(excess_packet_delay_threshold_value, allowed_values)
            )

        self._excess_packet_delay_threshold_value = excess_packet_delay_threshold_value
