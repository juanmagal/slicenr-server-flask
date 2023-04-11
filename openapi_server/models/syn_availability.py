# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SynAvailability(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NOT_SUPPORTED = "NOT SUPPORTED"
    BETWEEN_BS_AND_UE = "BETWEEN BS AND UE"
    BETWEEN_BS_AND_UE_UE_AND_UE = "BETWEEN BS AND UE & UE AND UE"
    def __init__(self):  # noqa: E501
        """SynAvailability - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SynAvailability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SynAvailability of this SynAvailability.  # noqa: E501
        :rtype: SynAvailability
        """
        return util.deserialize_model(dikt, cls)
