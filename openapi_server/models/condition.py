# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Condition(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    EQUAL_TO = "IS_EQUAL_TO"
    LESS_THAN = "IS_LESS_THAN"
    GREATER_THAN = "IS_GREATER_THAN"
    WITHIN_RANGE = "IS_WITHIN_RANGE"
    OUTSIDE_RANGE = "IS_OUTSIDE_RANGE"
    ONE_OF = "IS_ONE_OF"
    NOT_ONE_OF = "IS_NOT_ONE_OF"
    EQUAL_TO_OR_LESS_THAN = "IS_EQUAL_TO_OR_LESS_THAN"
    EQUAL_TO_OR_GREATER_THAN = "IS_EQUAL_TO_OR_GREATER_THAN"
    def __init__(self):  # noqa: E501
        """Condition - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Condition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Condition of this Condition.  # noqa: E501
        :rtype: Condition
        """
        return util.deserialize_model(dikt, cls)
