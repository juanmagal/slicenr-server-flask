# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class EventListForEventTriggeredMeasurementType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    OUT_OF_COVERAGE = "OUT_OF_COVERAGE"
    A2_EVENT = "A2_EVENT"
    def __init__(self):  # noqa: E501
        """EventListForEventTriggeredMeasurementType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'EventListForEventTriggeredMeasurementType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eventListForEventTriggeredMeasurement-Type of this EventListForEventTriggeredMeasurementType.  # noqa: E501
        :rtype: EventListForEventTriggeredMeasurementType
        """
        return util.deserialize_model(dikt, cls)
