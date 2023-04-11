# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AusfInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, n_f_srv_group_id=None):  # noqa: E501
        """AusfInfo - a model defined in OpenAPI

        :param n_f_srv_group_id: The n_f_srv_group_id of this AusfInfo.  # noqa: E501
        :type n_f_srv_group_id: str
        """
        self.openapi_types = {
            'n_f_srv_group_id': str
        }

        self.attribute_map = {
            'n_f_srv_group_id': 'nFSrvGroupId'
        }

        self._n_f_srv_group_id = n_f_srv_group_id

    @classmethod
    def from_dict(cls, dikt) -> 'AusfInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AusfInfo of this AusfInfo.  # noqa: E501
        :rtype: AusfInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n_f_srv_group_id(self):
        """Gets the n_f_srv_group_id of this AusfInfo.


        :return: The n_f_srv_group_id of this AusfInfo.
        :rtype: str
        """
        return self._n_f_srv_group_id

    @n_f_srv_group_id.setter
    def n_f_srv_group_id(self, n_f_srv_group_id):
        """Sets the n_f_srv_group_id of this AusfInfo.


        :param n_f_srv_group_id: The n_f_srv_group_id of this AusfInfo.
        :type n_f_srv_group_id: str
        """

        self._n_f_srv_group_id = n_f_srv_group_id
