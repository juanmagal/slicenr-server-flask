# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RimRSReportInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, detected_set_id=None, propagation_delay=None, functionality_of_rimrs=None):  # noqa: E501
        """RimRSReportInfo - a model defined in OpenAPI

        :param detected_set_id: The detected_set_id of this RimRSReportInfo.  # noqa: E501
        :type detected_set_id: int
        :param propagation_delay: The propagation_delay of this RimRSReportInfo.  # noqa: E501
        :type propagation_delay: int
        :param functionality_of_rimrs: The functionality_of_rimrs of this RimRSReportInfo.  # noqa: E501
        :type functionality_of_rimrs: str
        """
        self.openapi_types = {
            'detected_set_id': int,
            'propagation_delay': int,
            'functionality_of_rimrs': str
        }

        self.attribute_map = {
            'detected_set_id': 'detectedSetID',
            'propagation_delay': 'propagationDelay',
            'functionality_of_rimrs': 'functionalityOfRIMRS'
        }

        self._detected_set_id = detected_set_id
        self._propagation_delay = propagation_delay
        self._functionality_of_rimrs = functionality_of_rimrs

    @classmethod
    def from_dict(cls, dikt) -> 'RimRSReportInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RimRSReportInfo of this RimRSReportInfo.  # noqa: E501
        :rtype: RimRSReportInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detected_set_id(self):
        """Gets the detected_set_id of this RimRSReportInfo.


        :return: The detected_set_id of this RimRSReportInfo.
        :rtype: int
        """
        return self._detected_set_id

    @detected_set_id.setter
    def detected_set_id(self, detected_set_id):
        """Sets the detected_set_id of this RimRSReportInfo.


        :param detected_set_id: The detected_set_id of this RimRSReportInfo.
        :type detected_set_id: int
        """

        self._detected_set_id = detected_set_id

    @property
    def propagation_delay(self):
        """Gets the propagation_delay of this RimRSReportInfo.


        :return: The propagation_delay of this RimRSReportInfo.
        :rtype: int
        """
        return self._propagation_delay

    @propagation_delay.setter
    def propagation_delay(self, propagation_delay):
        """Sets the propagation_delay of this RimRSReportInfo.


        :param propagation_delay: The propagation_delay of this RimRSReportInfo.
        :type propagation_delay: int
        """

        self._propagation_delay = propagation_delay

    @property
    def functionality_of_rimrs(self):
        """Gets the functionality_of_rimrs of this RimRSReportInfo.


        :return: The functionality_of_rimrs of this RimRSReportInfo.
        :rtype: str
        """
        return self._functionality_of_rimrs

    @functionality_of_rimrs.setter
    def functionality_of_rimrs(self, functionality_of_rimrs):
        """Sets the functionality_of_rimrs of this RimRSReportInfo.


        :param functionality_of_rimrs: The functionality_of_rimrs of this RimRSReportInfo.
        :type functionality_of_rimrs: str
        """
        allowed_values = ["RS1", "RS2", "RS1forEnoughMitigation", "RS1forNotEnoughMitigation"]  # noqa: E501
        if functionality_of_rimrs not in allowed_values:
            raise ValueError(
                "Invalid value for `functionality_of_rimrs` ({0}), must be one of {1}"
                .format(functionality_of_rimrs, allowed_values)
            )

        self._functionality_of_rimrs = functionality_of_rimrs
