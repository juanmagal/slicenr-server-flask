# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.sec_func import SecFunc
from openapi_server.models.serv_attr_com import ServAttrCom
from openapi_server import util

from openapi_server.models.sec_func import SecFunc  # noqa: E501
from openapi_server.models.serv_attr_com import ServAttrCom  # noqa: E501

class N6Protection(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, serv_attr_com=None, sec_func_list=None):  # noqa: E501
        """N6Protection - a model defined in OpenAPI

        :param serv_attr_com: The serv_attr_com of this N6Protection.  # noqa: E501
        :type serv_attr_com: ServAttrCom
        :param sec_func_list: The sec_func_list of this N6Protection.  # noqa: E501
        :type sec_func_list: List[SecFunc]
        """
        self.openapi_types = {
            'serv_attr_com': ServAttrCom,
            'sec_func_list': List[SecFunc]
        }

        self.attribute_map = {
            'serv_attr_com': 'servAttrCom',
            'sec_func_list': 'secFuncList'
        }

        self._serv_attr_com = serv_attr_com
        self._sec_func_list = sec_func_list

    @classmethod
    def from_dict(cls, dikt) -> 'N6Protection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The N6Protection of this N6Protection.  # noqa: E501
        :rtype: N6Protection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def serv_attr_com(self):
        """Gets the serv_attr_com of this N6Protection.


        :return: The serv_attr_com of this N6Protection.
        :rtype: ServAttrCom
        """
        return self._serv_attr_com

    @serv_attr_com.setter
    def serv_attr_com(self, serv_attr_com):
        """Sets the serv_attr_com of this N6Protection.


        :param serv_attr_com: The serv_attr_com of this N6Protection.
        :type serv_attr_com: ServAttrCom
        """

        self._serv_attr_com = serv_attr_com

    @property
    def sec_func_list(self):
        """Gets the sec_func_list of this N6Protection.


        :return: The sec_func_list of this N6Protection.
        :rtype: List[SecFunc]
        """
        return self._sec_func_list

    @sec_func_list.setter
    def sec_func_list(self, sec_func_list):
        """Sets the sec_func_list of this N6Protection.


        :param sec_func_list: The sec_func_list of this N6Protection.
        :type sec_func_list: List[SecFunc]
        """

        self._sec_func_list = sec_func_list