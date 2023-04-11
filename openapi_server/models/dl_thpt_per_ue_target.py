# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.xl_thpt import XLThpt
from openapi_server import util

from openapi_server.models.xl_thpt import XLThpt  # noqa: E501

class DLThptPerUETarget(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, target_name=None, target_condition=None, target_value_range=None):  # noqa: E501
        """DLThptPerUETarget - a model defined in OpenAPI

        :param target_name: The target_name of this DLThptPerUETarget.  # noqa: E501
        :type target_name: str
        :param target_condition: The target_condition of this DLThptPerUETarget.  # noqa: E501
        :type target_condition: str
        :param target_value_range: The target_value_range of this DLThptPerUETarget.  # noqa: E501
        :type target_value_range: XLThpt
        """
        self.openapi_types = {
            'target_name': str,
            'target_condition': str,
            'target_value_range': XLThpt
        }

        self.attribute_map = {
            'target_name': 'targetName',
            'target_condition': 'targetCondition',
            'target_value_range': 'targetValueRange'
        }

        self._target_name = target_name
        self._target_condition = target_condition
        self._target_value_range = target_value_range

    @classmethod
    def from_dict(cls, dikt) -> 'DLThptPerUETarget':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DLThptPerUETarget of this DLThptPerUETarget.  # noqa: E501
        :rtype: DLThptPerUETarget
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_name(self):
        """Gets the target_name of this DLThptPerUETarget.


        :return: The target_name of this DLThptPerUETarget.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this DLThptPerUETarget.


        :param target_name: The target_name of this DLThptPerUETarget.
        :type target_name: str
        """
        allowed_values = ["DlThptPerUE"]  # noqa: E501
        if target_name not in allowed_values:
            raise ValueError(
                "Invalid value for `target_name` ({0}), must be one of {1}"
                .format(target_name, allowed_values)
            )

        self._target_name = target_name

    @property
    def target_condition(self):
        """Gets the target_condition of this DLThptPerUETarget.


        :return: The target_condition of this DLThptPerUETarget.
        :rtype: str
        """
        return self._target_condition

    @target_condition.setter
    def target_condition(self, target_condition):
        """Sets the target_condition of this DLThptPerUETarget.


        :param target_condition: The target_condition of this DLThptPerUETarget.
        :type target_condition: str
        """
        allowed_values = ["IS_GREATER_THAN"]  # noqa: E501
        if target_condition not in allowed_values:
            raise ValueError(
                "Invalid value for `target_condition` ({0}), must be one of {1}"
                .format(target_condition, allowed_values)
            )

        self._target_condition = target_condition

    @property
    def target_value_range(self):
        """Gets the target_value_range of this DLThptPerUETarget.


        :return: The target_value_range of this DLThptPerUETarget.
        :rtype: XLThpt
        """
        return self._target_value_range

    @target_value_range.setter
    def target_value_range(self, target_value_range):
        """Sets the target_value_range of this DLThptPerUETarget.


        :param target_value_range: The target_value_range of this DLThptPerUETarget.
        :type target_value_range: XLThpt
        """

        self._target_value_range = target_value_range
