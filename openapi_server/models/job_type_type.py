# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class JobTypeType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    IMMEDIATE_MDT_ONLY = "IMMEDIATE_MDT_ONLY"
    LOGGED_MDT_ONLY = "LOGGED_MDT_ONLY"
    TRACE_ONLY = "TRACE_ONLY"
    IMMEDIATE_MDT_AND_TRACE = "IMMEDIATE_MDT AND TRACE"
    RLF_REPORT_ONLY = "RLF_REPORT_ONLY"
    RCEF_REPORT_ONLY = "RCEF_REPORT_ONLY"
    LOGGED_MBSFN_MDT = "LOGGED_MBSFN_MDT"
    def __init__(self):  # noqa: E501
        """JobTypeType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'JobTypeType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jobType-Type of this JobTypeType.  # noqa: E501
        :rtype: JobTypeType
        """
        return util.deserialize_model(dikt, cls)
