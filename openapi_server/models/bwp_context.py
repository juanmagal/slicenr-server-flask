# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class BwpContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DL = "DL"
    UL = "UL"
    SUL = "SUL"
    def __init__(self):  # noqa: E501
        """BwpContext - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'BwpContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BwpContext of this BwpContext.  # noqa: E501
        :rtype: BwpContext
        """
        return util.deserialize_model(dikt, cls)