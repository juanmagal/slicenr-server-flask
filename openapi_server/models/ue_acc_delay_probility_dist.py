# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UeAccDelayProbilityDist(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, target_probability=None, accessdelay=None):  # noqa: E501
        """UeAccDelayProbilityDist - a model defined in OpenAPI

        :param target_probability: The target_probability of this UeAccDelayProbilityDist.  # noqa: E501
        :type target_probability: int
        :param accessdelay: The accessdelay of this UeAccDelayProbilityDist.  # noqa: E501
        :type accessdelay: int
        """
        self.openapi_types = {
            'target_probability': int,
            'accessdelay': int
        }

        self.attribute_map = {
            'target_probability': 'targetProbability',
            'accessdelay': 'accessdelay'
        }

        self._target_probability = target_probability
        self._accessdelay = accessdelay

    @classmethod
    def from_dict(cls, dikt) -> 'UeAccDelayProbilityDist':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeAccDelayProbilityDist of this UeAccDelayProbilityDist.  # noqa: E501
        :rtype: UeAccDelayProbilityDist
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_probability(self):
        """Gets the target_probability of this UeAccDelayProbilityDist.


        :return: The target_probability of this UeAccDelayProbilityDist.
        :rtype: int
        """
        return self._target_probability

    @target_probability.setter
    def target_probability(self, target_probability):
        """Sets the target_probability of this UeAccDelayProbilityDist.


        :param target_probability: The target_probability of this UeAccDelayProbilityDist.
        :type target_probability: int
        """

        self._target_probability = target_probability

    @property
    def accessdelay(self):
        """Gets the accessdelay of this UeAccDelayProbilityDist.


        :return: The accessdelay of this UeAccDelayProbilityDist.
        :rtype: int
        """
        return self._accessdelay

    @accessdelay.setter
    def accessdelay(self, accessdelay):
        """Sets the accessdelay of this UeAccDelayProbilityDist.


        :param accessdelay: The accessdelay of this UeAccDelayProbilityDist.
        :type accessdelay: int
        """

        self._accessdelay = accessdelay