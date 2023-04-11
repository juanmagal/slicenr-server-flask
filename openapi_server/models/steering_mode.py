# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_type import AccessType
from openapi_server.models.access_type_rm import AccessTypeRm
from openapi_server.models.steer_mode_value import SteerModeValue
from openapi_server import util

from openapi_server.models.access_type import AccessType  # noqa: E501
from openapi_server.models.access_type_rm import AccessTypeRm  # noqa: E501
from openapi_server.models.steer_mode_value import SteerModeValue  # noqa: E501

class SteeringMode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, steer_mode_value=None, active=None, standby=None, three_g_load=None, prio_acc=None):  # noqa: E501
        """SteeringMode - a model defined in OpenAPI

        :param steer_mode_value: The steer_mode_value of this SteeringMode.  # noqa: E501
        :type steer_mode_value: SteerModeValue
        :param active: The active of this SteeringMode.  # noqa: E501
        :type active: AccessType
        :param standby: The standby of this SteeringMode.  # noqa: E501
        :type standby: AccessTypeRm
        :param three_g_load: The three_g_load of this SteeringMode.  # noqa: E501
        :type three_g_load: int
        :param prio_acc: The prio_acc of this SteeringMode.  # noqa: E501
        :type prio_acc: AccessType
        """
        self.openapi_types = {
            'steer_mode_value': SteerModeValue,
            'active': AccessType,
            'standby': AccessTypeRm,
            'three_g_load': int,
            'prio_acc': AccessType
        }

        self.attribute_map = {
            'steer_mode_value': 'steerModeValue',
            'active': 'active',
            'standby': 'standby',
            'three_g_load': 'threeGLoad',
            'prio_acc': 'prioAcc'
        }

        self._steer_mode_value = steer_mode_value
        self._active = active
        self._standby = standby
        self._three_g_load = three_g_load
        self._prio_acc = prio_acc

    @classmethod
    def from_dict(cls, dikt) -> 'SteeringMode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SteeringMode of this SteeringMode.  # noqa: E501
        :rtype: SteeringMode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def steer_mode_value(self):
        """Gets the steer_mode_value of this SteeringMode.


        :return: The steer_mode_value of this SteeringMode.
        :rtype: SteerModeValue
        """
        return self._steer_mode_value

    @steer_mode_value.setter
    def steer_mode_value(self, steer_mode_value):
        """Sets the steer_mode_value of this SteeringMode.


        :param steer_mode_value: The steer_mode_value of this SteeringMode.
        :type steer_mode_value: SteerModeValue
        """

        self._steer_mode_value = steer_mode_value

    @property
    def active(self):
        """Gets the active of this SteeringMode.


        :return: The active of this SteeringMode.
        :rtype: AccessType
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SteeringMode.


        :param active: The active of this SteeringMode.
        :type active: AccessType
        """

        self._active = active

    @property
    def standby(self):
        """Gets the standby of this SteeringMode.


        :return: The standby of this SteeringMode.
        :rtype: AccessTypeRm
        """
        return self._standby

    @standby.setter
    def standby(self, standby):
        """Sets the standby of this SteeringMode.


        :param standby: The standby of this SteeringMode.
        :type standby: AccessTypeRm
        """

        self._standby = standby

    @property
    def three_g_load(self):
        """Gets the three_g_load of this SteeringMode.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The three_g_load of this SteeringMode.
        :rtype: int
        """
        return self._three_g_load

    @three_g_load.setter
    def three_g_load(self, three_g_load):
        """Sets the three_g_load of this SteeringMode.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param three_g_load: The three_g_load of this SteeringMode.
        :type three_g_load: int
        """
        if three_g_load is not None and three_g_load < 0:  # noqa: E501
            raise ValueError("Invalid value for `three_g_load`, must be a value greater than or equal to `0`")  # noqa: E501

        self._three_g_load = three_g_load

    @property
    def prio_acc(self):
        """Gets the prio_acc of this SteeringMode.


        :return: The prio_acc of this SteeringMode.
        :rtype: AccessType
        """
        return self._prio_acc

    @prio_acc.setter
    def prio_acc(self, prio_acc):
        """Sets the prio_acc of this SteeringMode.


        :param prio_acc: The prio_acc of this SteeringMode.
        :type prio_acc: AccessType
        """

        self._prio_acc = prio_acc
