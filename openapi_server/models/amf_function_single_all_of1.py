# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn12_single import EPN12Single
from openapi_server.models.epn14_single import EPN14Single
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn17_single import EPN17Single
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn26_single import EPN26Single
from openapi_server.models.epn2_single import EPN2Single
from openapi_server.models.epn8_single import EPN8Single
from openapi_server.models.epnlg_single import EPNLGSingle
from openapi_server.models.epnls_single import EPNLSSingle
from openapi_server import util

from openapi_server.models.epn11_single import EPN11Single  # noqa: E501
from openapi_server.models.epn12_single import EPN12Single  # noqa: E501
from openapi_server.models.epn14_single import EPN14Single  # noqa: E501
from openapi_server.models.epn15_single import EPN15Single  # noqa: E501
from openapi_server.models.epn17_single import EPN17Single  # noqa: E501
from openapi_server.models.epn20_single import EPN20Single  # noqa: E501
from openapi_server.models.epn22_single import EPN22Single  # noqa: E501
from openapi_server.models.epn26_single import EPN26Single  # noqa: E501
from openapi_server.models.epn2_single import EPN2Single  # noqa: E501
from openapi_server.models.epn8_single import EPN8Single  # noqa: E501
from openapi_server.models.epnlg_single import EPNLGSingle  # noqa: E501
from openapi_server.models.epnls_single import EPNLSSingle  # noqa: E501

class AmfFunctionSingleAllOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ep_n2=None, ep_n8=None, ep_n11=None, ep_n12=None, ep_n14=None, ep_n15=None, ep_n17=None, ep_n20=None, ep_n22=None, ep_n26=None, ep_nls=None, ep_nlg=None):  # noqa: E501
        """AmfFunctionSingleAllOf1 - a model defined in OpenAPI

        :param ep_n2: The ep_n2 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n2: List[EPN2Single]
        :param ep_n8: The ep_n8 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n8: List[EPN8Single]
        :param ep_n11: The ep_n11 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n11: List[EPN11Single]
        :param ep_n12: The ep_n12 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n12: List[EPN12Single]
        :param ep_n14: The ep_n14 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n14: List[EPN14Single]
        :param ep_n15: The ep_n15 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n15: List[EPN15Single]
        :param ep_n17: The ep_n17 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n17: List[EPN17Single]
        :param ep_n20: The ep_n20 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n20: List[EPN20Single]
        :param ep_n22: The ep_n22 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n22: List[EPN22Single]
        :param ep_n26: The ep_n26 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_n26: List[EPN26Single]
        :param ep_nls: The ep_nls of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_nls: List[EPNLSSingle]
        :param ep_nlg: The ep_nlg of this AmfFunctionSingleAllOf1.  # noqa: E501
        :type ep_nlg: List[EPNLGSingle]
        """
        self.openapi_types = {
            'ep_n2': List[EPN2Single],
            'ep_n8': List[EPN8Single],
            'ep_n11': List[EPN11Single],
            'ep_n12': List[EPN12Single],
            'ep_n14': List[EPN14Single],
            'ep_n15': List[EPN15Single],
            'ep_n17': List[EPN17Single],
            'ep_n20': List[EPN20Single],
            'ep_n22': List[EPN22Single],
            'ep_n26': List[EPN26Single],
            'ep_nls': List[EPNLSSingle],
            'ep_nlg': List[EPNLGSingle]
        }

        self.attribute_map = {
            'ep_n2': 'EP_N2',
            'ep_n8': 'EP_N8',
            'ep_n11': 'EP_N11',
            'ep_n12': 'EP_N12',
            'ep_n14': 'EP_N14',
            'ep_n15': 'EP_N15',
            'ep_n17': 'EP_N17',
            'ep_n20': 'EP_N20',
            'ep_n22': 'EP_N22',
            'ep_n26': 'EP_N26',
            'ep_nls': 'EP_NLS',
            'ep_nlg': 'EP_NLG'
        }

        self._ep_n2 = ep_n2
        self._ep_n8 = ep_n8
        self._ep_n11 = ep_n11
        self._ep_n12 = ep_n12
        self._ep_n14 = ep_n14
        self._ep_n15 = ep_n15
        self._ep_n17 = ep_n17
        self._ep_n20 = ep_n20
        self._ep_n22 = ep_n22
        self._ep_n26 = ep_n26
        self._ep_nls = ep_nls
        self._ep_nlg = ep_nlg

    @classmethod
    def from_dict(cls, dikt) -> 'AmfFunctionSingleAllOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmfFunction_Single_allOf_1 of this AmfFunctionSingleAllOf1.  # noqa: E501
        :rtype: AmfFunctionSingleAllOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ep_n2(self):
        """Gets the ep_n2 of this AmfFunctionSingleAllOf1.


        :return: The ep_n2 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN2Single]
        """
        return self._ep_n2

    @ep_n2.setter
    def ep_n2(self, ep_n2):
        """Sets the ep_n2 of this AmfFunctionSingleAllOf1.


        :param ep_n2: The ep_n2 of this AmfFunctionSingleAllOf1.
        :type ep_n2: List[EPN2Single]
        """

        self._ep_n2 = ep_n2

    @property
    def ep_n8(self):
        """Gets the ep_n8 of this AmfFunctionSingleAllOf1.


        :return: The ep_n8 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN8Single]
        """
        return self._ep_n8

    @ep_n8.setter
    def ep_n8(self, ep_n8):
        """Sets the ep_n8 of this AmfFunctionSingleAllOf1.


        :param ep_n8: The ep_n8 of this AmfFunctionSingleAllOf1.
        :type ep_n8: List[EPN8Single]
        """

        self._ep_n8 = ep_n8

    @property
    def ep_n11(self):
        """Gets the ep_n11 of this AmfFunctionSingleAllOf1.


        :return: The ep_n11 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN11Single]
        """
        return self._ep_n11

    @ep_n11.setter
    def ep_n11(self, ep_n11):
        """Sets the ep_n11 of this AmfFunctionSingleAllOf1.


        :param ep_n11: The ep_n11 of this AmfFunctionSingleAllOf1.
        :type ep_n11: List[EPN11Single]
        """

        self._ep_n11 = ep_n11

    @property
    def ep_n12(self):
        """Gets the ep_n12 of this AmfFunctionSingleAllOf1.


        :return: The ep_n12 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN12Single]
        """
        return self._ep_n12

    @ep_n12.setter
    def ep_n12(self, ep_n12):
        """Sets the ep_n12 of this AmfFunctionSingleAllOf1.


        :param ep_n12: The ep_n12 of this AmfFunctionSingleAllOf1.
        :type ep_n12: List[EPN12Single]
        """

        self._ep_n12 = ep_n12

    @property
    def ep_n14(self):
        """Gets the ep_n14 of this AmfFunctionSingleAllOf1.


        :return: The ep_n14 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN14Single]
        """
        return self._ep_n14

    @ep_n14.setter
    def ep_n14(self, ep_n14):
        """Sets the ep_n14 of this AmfFunctionSingleAllOf1.


        :param ep_n14: The ep_n14 of this AmfFunctionSingleAllOf1.
        :type ep_n14: List[EPN14Single]
        """

        self._ep_n14 = ep_n14

    @property
    def ep_n15(self):
        """Gets the ep_n15 of this AmfFunctionSingleAllOf1.


        :return: The ep_n15 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN15Single]
        """
        return self._ep_n15

    @ep_n15.setter
    def ep_n15(self, ep_n15):
        """Sets the ep_n15 of this AmfFunctionSingleAllOf1.


        :param ep_n15: The ep_n15 of this AmfFunctionSingleAllOf1.
        :type ep_n15: List[EPN15Single]
        """

        self._ep_n15 = ep_n15

    @property
    def ep_n17(self):
        """Gets the ep_n17 of this AmfFunctionSingleAllOf1.


        :return: The ep_n17 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN17Single]
        """
        return self._ep_n17

    @ep_n17.setter
    def ep_n17(self, ep_n17):
        """Sets the ep_n17 of this AmfFunctionSingleAllOf1.


        :param ep_n17: The ep_n17 of this AmfFunctionSingleAllOf1.
        :type ep_n17: List[EPN17Single]
        """

        self._ep_n17 = ep_n17

    @property
    def ep_n20(self):
        """Gets the ep_n20 of this AmfFunctionSingleAllOf1.


        :return: The ep_n20 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN20Single]
        """
        return self._ep_n20

    @ep_n20.setter
    def ep_n20(self, ep_n20):
        """Sets the ep_n20 of this AmfFunctionSingleAllOf1.


        :param ep_n20: The ep_n20 of this AmfFunctionSingleAllOf1.
        :type ep_n20: List[EPN20Single]
        """

        self._ep_n20 = ep_n20

    @property
    def ep_n22(self):
        """Gets the ep_n22 of this AmfFunctionSingleAllOf1.


        :return: The ep_n22 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN22Single]
        """
        return self._ep_n22

    @ep_n22.setter
    def ep_n22(self, ep_n22):
        """Sets the ep_n22 of this AmfFunctionSingleAllOf1.


        :param ep_n22: The ep_n22 of this AmfFunctionSingleAllOf1.
        :type ep_n22: List[EPN22Single]
        """

        self._ep_n22 = ep_n22

    @property
    def ep_n26(self):
        """Gets the ep_n26 of this AmfFunctionSingleAllOf1.


        :return: The ep_n26 of this AmfFunctionSingleAllOf1.
        :rtype: List[EPN26Single]
        """
        return self._ep_n26

    @ep_n26.setter
    def ep_n26(self, ep_n26):
        """Sets the ep_n26 of this AmfFunctionSingleAllOf1.


        :param ep_n26: The ep_n26 of this AmfFunctionSingleAllOf1.
        :type ep_n26: List[EPN26Single]
        """

        self._ep_n26 = ep_n26

    @property
    def ep_nls(self):
        """Gets the ep_nls of this AmfFunctionSingleAllOf1.


        :return: The ep_nls of this AmfFunctionSingleAllOf1.
        :rtype: List[EPNLSSingle]
        """
        return self._ep_nls

    @ep_nls.setter
    def ep_nls(self, ep_nls):
        """Sets the ep_nls of this AmfFunctionSingleAllOf1.


        :param ep_nls: The ep_nls of this AmfFunctionSingleAllOf1.
        :type ep_nls: List[EPNLSSingle]
        """

        self._ep_nls = ep_nls

    @property
    def ep_nlg(self):
        """Gets the ep_nlg of this AmfFunctionSingleAllOf1.


        :return: The ep_nlg of this AmfFunctionSingleAllOf1.
        :rtype: List[EPNLGSingle]
        """
        return self._ep_nlg

    @ep_nlg.setter
    def ep_nlg(self, ep_nlg):
        """Sets the ep_nlg of this AmfFunctionSingleAllOf1.


        :param ep_nlg: The ep_nlg of this AmfFunctionSingleAllOf1.
        :type ep_nlg: List[EPNLGSingle]
        """

        self._ep_nlg = ep_nlg
