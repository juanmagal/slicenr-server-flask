# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EventThresholdTypeEventThresholdRSRQ(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """EventThresholdTypeEventThresholdRSRQ - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EventThresholdTypeEventThresholdRSRQ':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eventThreshold_Type_EventThresholdRSRQ of this EventThresholdTypeEventThresholdRSRQ.  # noqa: E501
        :rtype: EventThresholdTypeEventThresholdRSRQ
        """
        return util.deserialize_model(dikt, cls)
