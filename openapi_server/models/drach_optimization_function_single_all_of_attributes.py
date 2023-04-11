# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.ue_acc_delay_probility_dist import UeAccDelayProbilityDist
from openapi_server.models.ue_acc_probility_dist import UeAccProbilityDist
from openapi_server import util

from openapi_server.models.ue_acc_delay_probility_dist import UeAccDelayProbilityDist  # noqa: E501
from openapi_server.models.ue_acc_probility_dist import UeAccProbilityDist  # noqa: E501

class DRACHOptimizationFunctionSingleAllOfAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, drach_optimization_control=None, ue_acc_probility_dist=None, ue_acc_delay_probility_dist=None):  # noqa: E501
        """DRACHOptimizationFunctionSingleAllOfAttributes - a model defined in OpenAPI

        :param drach_optimization_control: The drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes.  # noqa: E501
        :type drach_optimization_control: bool
        :param ue_acc_probility_dist: The ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.  # noqa: E501
        :type ue_acc_probility_dist: UeAccProbilityDist
        :param ue_acc_delay_probility_dist: The ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.  # noqa: E501
        :type ue_acc_delay_probility_dist: UeAccDelayProbilityDist
        """
        self.openapi_types = {
            'drach_optimization_control': bool,
            'ue_acc_probility_dist': UeAccProbilityDist,
            'ue_acc_delay_probility_dist': UeAccDelayProbilityDist
        }

        self.attribute_map = {
            'drach_optimization_control': 'drachOptimizationControl',
            'ue_acc_probility_dist': 'ueAccProbilityDist',
            'ue_acc_delay_probility_dist': 'ueAccDelayProbilityDist'
        }

        self._drach_optimization_control = drach_optimization_control
        self._ue_acc_probility_dist = ue_acc_probility_dist
        self._ue_acc_delay_probility_dist = ue_acc_delay_probility_dist

    @classmethod
    def from_dict(cls, dikt) -> 'DRACHOptimizationFunctionSingleAllOfAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DRACHOptimizationFunction_Single_allOf_attributes of this DRACHOptimizationFunctionSingleAllOfAttributes.  # noqa: E501
        :rtype: DRACHOptimizationFunctionSingleAllOfAttributes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def drach_optimization_control(self):
        """Gets the drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :return: The drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :rtype: bool
        """
        return self._drach_optimization_control

    @drach_optimization_control.setter
    def drach_optimization_control(self, drach_optimization_control):
        """Sets the drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :param drach_optimization_control: The drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :type drach_optimization_control: bool
        """

        self._drach_optimization_control = drach_optimization_control

    @property
    def ue_acc_probility_dist(self):
        """Gets the ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :return: The ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :rtype: UeAccProbilityDist
        """
        return self._ue_acc_probility_dist

    @ue_acc_probility_dist.setter
    def ue_acc_probility_dist(self, ue_acc_probility_dist):
        """Sets the ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :param ue_acc_probility_dist: The ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :type ue_acc_probility_dist: UeAccProbilityDist
        """

        self._ue_acc_probility_dist = ue_acc_probility_dist

    @property
    def ue_acc_delay_probility_dist(self):
        """Gets the ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :return: The ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :rtype: UeAccDelayProbilityDist
        """
        return self._ue_acc_delay_probility_dist

    @ue_acc_delay_probility_dist.setter
    def ue_acc_delay_probility_dist(self, ue_acc_delay_probility_dist):
        """Sets the ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.


        :param ue_acc_delay_probility_dist: The ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes.
        :type ue_acc_delay_probility_dist: UeAccDelayProbilityDist
        """

        self._ue_acc_delay_probility_dist = ue_acc_delay_probility_dist