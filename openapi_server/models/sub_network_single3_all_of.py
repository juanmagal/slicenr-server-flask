# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.assurance_closed_control_loop_single import AssuranceClosedControlLoopSingle
from openapi_server import util

from openapi_server.models.assurance_closed_control_loop_single import AssuranceClosedControlLoopSingle  # noqa: E501

class SubNetworkSingle3AllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, assurance_closed_control_loop=None):  # noqa: E501
        """SubNetworkSingle3AllOf - a model defined in OpenAPI

        :param assurance_closed_control_loop: The assurance_closed_control_loop of this SubNetworkSingle3AllOf.  # noqa: E501
        :type assurance_closed_control_loop: List[AssuranceClosedControlLoopSingle]
        """
        self.openapi_types = {
            'assurance_closed_control_loop': List[AssuranceClosedControlLoopSingle]
        }

        self.attribute_map = {
            'assurance_closed_control_loop': 'AssuranceClosedControlLoop'
        }

        self._assurance_closed_control_loop = assurance_closed_control_loop

    @classmethod
    def from_dict(cls, dikt) -> 'SubNetworkSingle3AllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubNetwork_Single_3_allOf of this SubNetworkSingle3AllOf.  # noqa: E501
        :rtype: SubNetworkSingle3AllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def assurance_closed_control_loop(self):
        """Gets the assurance_closed_control_loop of this SubNetworkSingle3AllOf.


        :return: The assurance_closed_control_loop of this SubNetworkSingle3AllOf.
        :rtype: List[AssuranceClosedControlLoopSingle]
        """
        return self._assurance_closed_control_loop

    @assurance_closed_control_loop.setter
    def assurance_closed_control_loop(self, assurance_closed_control_loop):
        """Sets the assurance_closed_control_loop of this SubNetworkSingle3AllOf.


        :param assurance_closed_control_loop: The assurance_closed_control_loop of this SubNetworkSingle3AllOf.
        :type assurance_closed_control_loop: List[AssuranceClosedControlLoopSingle]
        """

        self._assurance_closed_control_loop = assurance_closed_control_loop
