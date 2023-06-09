# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EventThresholdTypeEventThreshold1F(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cpich_rscp=None, cpich_ec_no=None, path_loss=None):  # noqa: E501
        """EventThresholdTypeEventThreshold1F - a model defined in OpenAPI

        :param cpich_rscp: The cpich_rscp of this EventThresholdTypeEventThreshold1F.  # noqa: E501
        :type cpich_rscp: int
        :param cpich_ec_no: The cpich_ec_no of this EventThresholdTypeEventThreshold1F.  # noqa: E501
        :type cpich_ec_no: int
        :param path_loss: The path_loss of this EventThresholdTypeEventThreshold1F.  # noqa: E501
        :type path_loss: int
        """
        self.openapi_types = {
            'cpich_rscp': int,
            'cpich_ec_no': int,
            'path_loss': int
        }

        self.attribute_map = {
            'cpich_rscp': 'CPICH_RSCP',
            'cpich_ec_no': 'CPICH_EcNo',
            'path_loss': 'PathLoss'
        }

        self._cpich_rscp = cpich_rscp
        self._cpich_ec_no = cpich_ec_no
        self._path_loss = path_loss

    @classmethod
    def from_dict(cls, dikt) -> 'EventThresholdTypeEventThreshold1F':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eventThreshold_Type_EventThreshold1F of this EventThresholdTypeEventThreshold1F.  # noqa: E501
        :rtype: EventThresholdTypeEventThreshold1F
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cpich_rscp(self):
        """Gets the cpich_rscp of this EventThresholdTypeEventThreshold1F.


        :return: The cpich_rscp of this EventThresholdTypeEventThreshold1F.
        :rtype: int
        """
        return self._cpich_rscp

    @cpich_rscp.setter
    def cpich_rscp(self, cpich_rscp):
        """Sets the cpich_rscp of this EventThresholdTypeEventThreshold1F.


        :param cpich_rscp: The cpich_rscp of this EventThresholdTypeEventThreshold1F.
        :type cpich_rscp: int
        """
        if cpich_rscp is not None and cpich_rscp > 25:  # noqa: E501
            raise ValueError("Invalid value for `cpich_rscp`, must be a value less than or equal to `25`")  # noqa: E501
        if cpich_rscp is not None and cpich_rscp < -120:  # noqa: E501
            raise ValueError("Invalid value for `cpich_rscp`, must be a value greater than or equal to `-120`")  # noqa: E501

        self._cpich_rscp = cpich_rscp

    @property
    def cpich_ec_no(self):
        """Gets the cpich_ec_no of this EventThresholdTypeEventThreshold1F.


        :return: The cpich_ec_no of this EventThresholdTypeEventThreshold1F.
        :rtype: int
        """
        return self._cpich_ec_no

    @cpich_ec_no.setter
    def cpich_ec_no(self, cpich_ec_no):
        """Sets the cpich_ec_no of this EventThresholdTypeEventThreshold1F.


        :param cpich_ec_no: The cpich_ec_no of this EventThresholdTypeEventThreshold1F.
        :type cpich_ec_no: int
        """
        if cpich_ec_no is not None and cpich_ec_no > 0:  # noqa: E501
            raise ValueError("Invalid value for `cpich_ec_no`, must be a value less than or equal to `0`")  # noqa: E501
        if cpich_ec_no is not None and cpich_ec_no < -24:  # noqa: E501
            raise ValueError("Invalid value for `cpich_ec_no`, must be a value greater than or equal to `-24`")  # noqa: E501

        self._cpich_ec_no = cpich_ec_no

    @property
    def path_loss(self):
        """Gets the path_loss of this EventThresholdTypeEventThreshold1F.


        :return: The path_loss of this EventThresholdTypeEventThreshold1F.
        :rtype: int
        """
        return self._path_loss

    @path_loss.setter
    def path_loss(self, path_loss):
        """Sets the path_loss of this EventThresholdTypeEventThreshold1F.


        :param path_loss: The path_loss of this EventThresholdTypeEventThreshold1F.
        :type path_loss: int
        """
        if path_loss is not None and path_loss > 165:  # noqa: E501
            raise ValueError("Invalid value for `path_loss`, must be a value less than or equal to `165`")  # noqa: E501
        if path_loss is not None and path_loss < 30:  # noqa: E501
            raise ValueError("Invalid value for `path_loss`, must be a value greater than or equal to `30`")  # noqa: E501

        self._path_loss = path_loss
