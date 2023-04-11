# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SupportedDataSetId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SUBSCRIPTION = "SUBSCRIPTION"
    POLICY = "POLICY"
    EXPOSURE = "EXPOSURE"
    APPLICATION = "APPLICATION"
    def __init__(self):  # noqa: E501
        """SupportedDataSetId - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SupportedDataSetId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SupportedDataSetId of this SupportedDataSetId.  # noqa: E501
        :rtype: SupportedDataSetId
        """
        return util.deserialize_model(dikt, cls)