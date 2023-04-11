# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.serv_attr_com import ServAttrCom
from openapi_server.models.support import Support
from openapi_server import util

from openapi_server.models.serv_attr_com import ServAttrCom  # noqa: E501
from openapi_server.models.support import Support  # noqa: E501

class V2XCommModels(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, serv_attr_com=None, v2_x_mode=None):  # noqa: E501
        """V2XCommModels - a model defined in OpenAPI

        :param serv_attr_com: The serv_attr_com of this V2XCommModels.  # noqa: E501
        :type serv_attr_com: ServAttrCom
        :param v2_x_mode: The v2_x_mode of this V2XCommModels.  # noqa: E501
        :type v2_x_mode: Support
        """
        self.openapi_types = {
            'serv_attr_com': ServAttrCom,
            'v2_x_mode': Support
        }

        self.attribute_map = {
            'serv_attr_com': 'servAttrCom',
            'v2_x_mode': 'v2XMode'
        }

        self._serv_attr_com = serv_attr_com
        self._v2_x_mode = v2_x_mode

    @classmethod
    def from_dict(cls, dikt) -> 'V2XCommModels':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The V2XCommModels of this V2XCommModels.  # noqa: E501
        :rtype: V2XCommModels
        """
        return util.deserialize_model(dikt, cls)

    @property
    def serv_attr_com(self):
        """Gets the serv_attr_com of this V2XCommModels.


        :return: The serv_attr_com of this V2XCommModels.
        :rtype: ServAttrCom
        """
        return self._serv_attr_com

    @serv_attr_com.setter
    def serv_attr_com(self, serv_attr_com):
        """Sets the serv_attr_com of this V2XCommModels.


        :param serv_attr_com: The serv_attr_com of this V2XCommModels.
        :type serv_attr_com: ServAttrCom
        """

        self._serv_attr_com = serv_attr_com

    @property
    def v2_x_mode(self):
        """Gets the v2_x_mode of this V2XCommModels.


        :return: The v2_x_mode of this V2XCommModels.
        :rtype: Support
        """
        return self._v2_x_mode

    @v2_x_mode.setter
    def v2_x_mode(self, v2_x_mode):
        """Sets the v2_x_mode of this V2XCommModels.


        :param v2_x_mode: The v2_x_mode of this V2XCommModels.
        :type v2_x_mode: Support
        """

        self._v2_x_mode = v2_x_mode
