# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.threshold_monitor_single_all_of_attributes import ThresholdMonitorSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.threshold_monitor_single_all_of_attributes import ThresholdMonitorSingleAllOfAttributes  # noqa: E501

class ThresholdMonitorSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """ThresholdMonitorSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this ThresholdMonitorSingleAllOf.  # noqa: E501
        :type attributes: ThresholdMonitorSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': ThresholdMonitorSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'ThresholdMonitorSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ThresholdMonitor_Single_allOf of this ThresholdMonitorSingleAllOf.  # noqa: E501
        :rtype: ThresholdMonitorSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this ThresholdMonitorSingleAllOf.


        :return: The attributes of this ThresholdMonitorSingleAllOf.
        :rtype: ThresholdMonitorSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ThresholdMonitorSingleAllOf.


        :param attributes: The attributes of this ThresholdMonitorSingleAllOf.
        :type attributes: ThresholdMonitorSingleAllOfAttributes
        """

        self._attributes = attributes
