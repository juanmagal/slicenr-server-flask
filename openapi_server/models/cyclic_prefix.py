# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CyclicPrefix(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _15 = "15"
    _30 = "30"
    _60 = "60"
    _120 = "120"
    def __init__(self):  # noqa: E501
        """CyclicPrefix - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'CyclicPrefix':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CyclicPrefix of this CyclicPrefix.  # noqa: E501
        :rtype: CyclicPrefix
        """
        return util.deserialize_model(dikt, cls)