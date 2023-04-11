# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LoggingIntervalType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, umts=None, lte=None, nr=None):  # noqa: E501
        """LoggingIntervalType - a model defined in OpenAPI

        :param umts: The umts of this LoggingIntervalType.  # noqa: E501
        :type umts: List[str]
        :param lte: The lte of this LoggingIntervalType.  # noqa: E501
        :type lte: List[str]
        :param nr: The nr of this LoggingIntervalType.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'LoggingIntervalType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The loggingInterval-Type of this LoggingIntervalType.  # noqa: E501
        :rtype: LoggingIntervalType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def umts(self):
        """Gets the umts of this LoggingIntervalType.


        :return: The umts of this LoggingIntervalType.
        :rtype: List[str]
        """
        return self._umts

    @umts.setter
    def umts(self, umts):
        """Sets the umts of this LoggingIntervalType.


        :param umts: The umts of this LoggingIntervalType.
        :type umts: List[str]
        """
        allowed_values = ["1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s"]  # noqa: E501
        if not set(umts).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `umts` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(umts) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._umts = umts

    @property
    def lte(self):
        """Gets the lte of this LoggingIntervalType.


        :return: The lte of this LoggingIntervalType.
        :rtype: List[str]
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this LoggingIntervalType.


        :param lte: The lte of this LoggingIntervalType.
        :type lte: List[str]
        """
        allowed_values = ["1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s"]  # noqa: E501
        if not set(lte).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `lte` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(lte) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._lte = lte

    @property
    def nr(self):
        """Gets the nr of this LoggingIntervalType.


        :return: The nr of this LoggingIntervalType.
        :rtype: List[str]
        """
        return self._nr

    @nr.setter
    def nr(self, nr):
        """Sets the nr of this LoggingIntervalType.


        :param nr: The nr of this LoggingIntervalType.
        :type nr: List[str]
        """
        allowed_values = ["0.32s", "0.64s", "1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s", "INFINITY"]  # noqa: E501
        if not set(nr).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `nr` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(nr) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._nr = nr
