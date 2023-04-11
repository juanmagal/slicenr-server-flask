# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AlarmType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    COMMUNICATIONS_ALARM = "COMMUNICATIONS_ALARM"
    QUALITY_OF_SERVICE_ALARM = "QUALITY_OF_SERVICE_ALARM"
    PROCESSING_ERROR_ALARM = "PROCESSING_ERROR_ALARM"
    EQUIPMENT_ALARM = "EQUIPMENT_ALARM"
    ENVIRONMENTAL_ALARM = "ENVIRONMENTAL_ALARM"
    INTEGRITY_VIOLATION = "INTEGRITY_VIOLATION"
    OPERATIONAL_VIOLATION = "OPERATIONAL_VIOLATION"
    PHYSICAL_VIOLATION = "PHYSICAL_VIOLATION"
    SECURITY_SERVICE_OR_MECHANISM_VIOLATION = "SECURITY_SERVICE_OR_MECHANISM_VIOLATION"
    TIME_DOMAIN_VIOLATION = "TIME_DOMAIN_VIOLATION"
    def __init__(self):  # noqa: E501
        """AlarmType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AlarmType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlarmType of this AlarmType.  # noqa: E501
        :rtype: AlarmType
        """
        return util.deserialize_model(dikt, cls)
