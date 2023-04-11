# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ReportingCtrlOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_reporting_period=None):  # noqa: E501
        """ReportingCtrlOneOf - a model defined in OpenAPI

        :param file_reporting_period: The file_reporting_period of this ReportingCtrlOneOf.  # noqa: E501
        :type file_reporting_period: int
        """
        self.openapi_types = {
            'file_reporting_period': int
        }

        self.attribute_map = {
            'file_reporting_period': 'fileReportingPeriod'
        }

        self._file_reporting_period = file_reporting_period

    @classmethod
    def from_dict(cls, dikt) -> 'ReportingCtrlOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportingCtrl_oneOf of this ReportingCtrlOneOf.  # noqa: E501
        :rtype: ReportingCtrlOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_reporting_period(self):
        """Gets the file_reporting_period of this ReportingCtrlOneOf.


        :return: The file_reporting_period of this ReportingCtrlOneOf.
        :rtype: int
        """
        return self._file_reporting_period

    @file_reporting_period.setter
    def file_reporting_period(self, file_reporting_period):
        """Sets the file_reporting_period of this ReportingCtrlOneOf.


        :param file_reporting_period: The file_reporting_period of this ReportingCtrlOneOf.
        :type file_reporting_period: int
        """

        self._file_reporting_period = file_reporting_period
