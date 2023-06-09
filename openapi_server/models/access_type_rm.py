# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_type import AccessType
from openapi_server.models.null_value import NullValue
from openapi_server import util

from openapi_server.models.access_type import AccessType  # noqa: E501
from openapi_server.models.null_value import NullValue  # noqa: E501

class AccessTypeRm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """AccessTypeRm - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AccessTypeRm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessTypeRm of this AccessTypeRm.  # noqa: E501
        :rtype: AccessTypeRm
        """
        return util.deserialize_model(dikt, cls)
