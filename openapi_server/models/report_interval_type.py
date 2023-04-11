# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ReportIntervalType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, umts=None, lte=None, nr=None):  # noqa: E501
        """ReportIntervalType - a model defined in OpenAPI

        :param umts: The umts of this ReportIntervalType.  # noqa: E501
        :type umts: List[str]
        :param lte: The lte of this ReportIntervalType.  # noqa: E501
        :type lte: List[str]
        :param nr: The nr of this ReportIntervalType.  # noqa: E501
        :type nr: List[str]
        """
        self.openapi_types = {
            'umts': List[str],
            'lte': List[str],
            'nr': List[str]
        }

        self.attribute_map = {
            'umts': 'UMTS',
            'lte': 'LTE',
            'nr': 'NR'
        }

        self._umts = umts
        self._lte = lte
        self._nr = nr

    @classmethod
    def from_dict(cls, dikt) -> 'ReportIntervalType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The reportInterval-Type of this ReportIntervalType.  # noqa: E501
        :rtype: ReportIntervalType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def umts(self):
        """Gets the umts of this ReportIntervalType.


        :return: The umts of this ReportIntervalType.
        :rtype: List[str]
        """
        return self._umts

    @umts.setter
    def umts(self, umts):
        """Sets the umts of this ReportIntervalType.


        :param umts: The umts of this ReportIntervalType.
        :type umts: List[str]
        """
        allowed_values = ["250ms", "500ms", "1000ms", "2000ms", "3000ms", "4000ms", "6000ms", "8000ms", "12000ms", "16000ms", "20000ms", "24000ms", "28000ms", "32000ms", "64000ms"]  # noqa: E501
        if not set(umts).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `umts` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(umts) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._umts = umts

    @property
    def lte(self):
        """Gets the lte of this ReportIntervalType.


        :return: The lte of this ReportIntervalType.
        :rtype: List[str]
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this ReportIntervalType.


        :param lte: The lte of this ReportIntervalType.
        :type lte: List[str]
        """
        allowed_values = ["120ms", "240ms", "480ms", "640ms", "1024ms", "2048ms", "5120ms", "10240ms", "60000ms", "360000ms", "720000ms", "1800000ms", "3600000ms"]  # noqa: E501
        if not set(lte).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `lte` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(lte) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._lte = lte

    @property
    def nr(self):
        """Gets the nr of this ReportIntervalType.


        :return: The nr of this ReportIntervalType.
        :rtype: List[str]
        """
        return self._nr

    @nr.setter
    def nr(self, nr):
        """Sets the nr of this ReportIntervalType.


        :param nr: The nr of this ReportIntervalType.
        :type nr: List[str]
        """
        allowed_values = ["120ms", "240ms", "480ms", "640ms", "1024ms", "2048ms", "5120ms", "10240ms", "20480ms", "40960ms", "60000ms", "360000ms", "720000ms", "1800000ms"]  # noqa: E501
        if not set(nr).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `nr` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(nr) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._nr = nr
