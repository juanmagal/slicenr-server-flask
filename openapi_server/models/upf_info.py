# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UpfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, smf_serving_areas=None):  # noqa: E501
        """UpfInfo - a model defined in OpenAPI

        :param smf_serving_areas: The smf_serving_areas of this UpfInfo.  # noqa: E501
        :type smf_serving_areas: str
        """
        self.openapi_types = {
            'smf_serving_areas': str
        }

        self.attribute_map = {
            'smf_serving_areas': 'smfServingAreas'
        }

        self._smf_serving_areas = smf_serving_areas

    @classmethod
    def from_dict(cls, dikt) -> 'UpfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpfInfo of this UpfInfo.  # noqa: E501
        :rtype: UpfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def smf_serving_areas(self):
        """Gets the smf_serving_areas of this UpfInfo.


        :return: The smf_serving_areas of this UpfInfo.
        :rtype: str
        """
        return self._smf_serving_areas

    @smf_serving_areas.setter
    def smf_serving_areas(self, smf_serving_areas):
        """Sets the smf_serving_areas of this UpfInfo.


        :param smf_serving_areas: The smf_serving_areas of this UpfInfo.
        :type smf_serving_areas: str
        """

        self._smf_serving_areas = smf_serving_areas
