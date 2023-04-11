# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AmfIdentifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amf_region_id=None, amf_set_id=None, amf_pointer=None):  # noqa: E501
        """AmfIdentifier - a model defined in OpenAPI

        :param amf_region_id: The amf_region_id of this AmfIdentifier.  # noqa: E501
        :type amf_region_id: int
        :param amf_set_id: The amf_set_id of this AmfIdentifier.  # noqa: E501
        :type amf_set_id: str
        :param amf_pointer: The amf_pointer of this AmfIdentifier.  # noqa: E501
        :type amf_pointer: int
        """
        self.openapi_types = {
            'amf_region_id': int,
            'amf_set_id': str,
            'amf_pointer': int
        }

        self.attribute_map = {
            'amf_region_id': 'amfRegionId',
            'amf_set_id': 'amfSetId',
            'amf_pointer': 'amfPointer'
        }

        self._amf_region_id = amf_region_id
        self._amf_set_id = amf_set_id
        self._amf_pointer = amf_pointer

    @classmethod
    def from_dict(cls, dikt) -> 'AmfIdentifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfIdentifier of this AmfIdentifier.  # noqa: E501
        :rtype: AmfIdentifier
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amf_region_id(self):
        """Gets the amf_region_id of this AmfIdentifier.

        AmfRegionId is defined in TS 23.003  # noqa: E501

        :return: The amf_region_id of this AmfIdentifier.
        :rtype: int
        """
        return self._amf_region_id

    @amf_region_id.setter
    def amf_region_id(self, amf_region_id):
        """Sets the amf_region_id of this AmfIdentifier.

        AmfRegionId is defined in TS 23.003  # noqa: E501

        :param amf_region_id: The amf_region_id of this AmfIdentifier.
        :type amf_region_id: int
        """
        if amf_region_id is not None and amf_region_id > 255:  # noqa: E501
            raise ValueError("Invalid value for `amf_region_id`, must be a value less than or equal to `255`")  # noqa: E501

        self._amf_region_id = amf_region_id

    @property
    def amf_set_id(self):
        """Gets the amf_set_id of this AmfIdentifier.

        AmfSetId is defined in TS 23.003  # noqa: E501

        :return: The amf_set_id of this AmfIdentifier.
        :rtype: str
        """
        return self._amf_set_id

    @amf_set_id.setter
    def amf_set_id(self, amf_set_id):
        """Sets the amf_set_id of this AmfIdentifier.

        AmfSetId is defined in TS 23.003  # noqa: E501

        :param amf_set_id: The amf_set_id of this AmfIdentifier.
        :type amf_set_id: str
        """

        self._amf_set_id = amf_set_id

    @property
    def amf_pointer(self):
        """Gets the amf_pointer of this AmfIdentifier.

        AmfPointer is defined in TS 23.003  # noqa: E501

        :return: The amf_pointer of this AmfIdentifier.
        :rtype: int
        """
        return self._amf_pointer

    @amf_pointer.setter
    def amf_pointer(self, amf_pointer):
        """Sets the amf_pointer of this AmfIdentifier.

        AmfPointer is defined in TS 23.003  # noqa: E501

        :param amf_pointer: The amf_pointer of this AmfIdentifier.
        :type amf_pointer: int
        """
        if amf_pointer is not None and amf_pointer > 63:  # noqa: E501
            raise ValueError("Invalid value for `amf_pointer`, must be a value less than or equal to `63`")  # noqa: E501

        self._amf_pointer = amf_pointer
