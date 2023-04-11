# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single_all_of_attributes import GtpUPathQoSMonitoringControlSingleAllOfAttributes
from openapi_server import util

from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single_all_of_attributes import GtpUPathQoSMonitoringControlSingleAllOfAttributes  # noqa: E501

class GtpUPathQoSMonitoringControlSingleAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attributes=None):  # noqa: E501
        """GtpUPathQoSMonitoringControlSingleAllOf - a model defined in OpenAPI

        :param attributes: The attributes of this GtpUPathQoSMonitoringControlSingleAllOf.  # noqa: E501
        :type attributes: GtpUPathQoSMonitoringControlSingleAllOfAttributes
        """
        self.openapi_types = {
            'attributes': GtpUPathQoSMonitoringControlSingleAllOfAttributes
        }

        self.attribute_map = {
            'attributes': 'attributes'
        }

        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'GtpUPathQoSMonitoringControlSingleAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GtpUPathQoSMonitoringControl_Single_allOf of this GtpUPathQoSMonitoringControlSingleAllOf.  # noqa: E501
        :rtype: GtpUPathQoSMonitoringControlSingleAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attributes(self):
        """Gets the attributes of this GtpUPathQoSMonitoringControlSingleAllOf.


        :return: The attributes of this GtpUPathQoSMonitoringControlSingleAllOf.
        :rtype: GtpUPathQoSMonitoringControlSingleAllOfAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this GtpUPathQoSMonitoringControlSingleAllOf.


        :param attributes: The attributes of this GtpUPathQoSMonitoringControlSingleAllOf.
        :type attributes: GtpUPathQoSMonitoringControlSingleAllOfAttributes
        """

        self._attributes = attributes