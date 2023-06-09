# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.expectation_verb import ExpectationVerb
from openapi_server.models.fulfilment_info import FulfilmentInfo
from openapi_server.models.intent_expectation import IntentExpectation
from openapi_server.models.radio_network_expectation import RadioNetworkExpectation
from openapi_server.models.service_support_expectation import ServiceSupportExpectation
from openapi_server.models.service_support_expectation_expectation_contexts_inner import ServiceSupportExpectationExpectationContextsInner
from openapi_server.models.service_support_expectation_expectation_targets_inner import ServiceSupportExpectationExpectationTargetsInner
from openapi_server.models.service_support_expectation_object import ServiceSupportExpectationObject
from openapi_server import util

from openapi_server.models.expectation_verb import ExpectationVerb  # noqa: E501
from openapi_server.models.fulfilment_info import FulfilmentInfo  # noqa: E501
from openapi_server.models.intent_expectation import IntentExpectation  # noqa: E501
from openapi_server.models.radio_network_expectation import RadioNetworkExpectation  # noqa: E501
from openapi_server.models.service_support_expectation import ServiceSupportExpectation  # noqa: E501
from openapi_server.models.service_support_expectation_expectation_contexts_inner import ServiceSupportExpectationExpectationContextsInner  # noqa: E501
from openapi_server.models.service_support_expectation_expectation_targets_inner import ServiceSupportExpectationExpectationTargetsInner  # noqa: E501
from openapi_server.models.service_support_expectation_object import ServiceSupportExpectationObject  # noqa: E501

class IntentSingleAllOfIntentExpectationsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, expectation_id=None, expectation_verb=None, expectation_objects=None, expectation_targets=None, expectation_contexts=None, expectationfulfilment_info=None):  # noqa: E501
        """IntentSingleAllOfIntentExpectationsInner - a model defined in OpenAPI

        :param expectation_id: The expectation_id of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectation_id: str
        :param expectation_verb: The expectation_verb of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectation_verb: ExpectationVerb
        :param expectation_objects: The expectation_objects of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectation_objects: List[ServiceSupportExpectationObject]
        :param expectation_targets: The expectation_targets of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectation_targets: List[ServiceSupportExpectationExpectationTargetsInner]
        :param expectation_contexts: The expectation_contexts of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectation_contexts: List[ServiceSupportExpectationExpectationContextsInner]
        :param expectationfulfilment_info: The expectationfulfilment_info of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :type expectationfulfilment_info: FulfilmentInfo
        """
        self.openapi_types = {
            'expectation_id': str,
            'expectation_verb': ExpectationVerb,
            'expectation_objects': List[ServiceSupportExpectationObject],
            'expectation_targets': List[ServiceSupportExpectationExpectationTargetsInner],
            'expectation_contexts': List[ServiceSupportExpectationExpectationContextsInner],
            'expectationfulfilment_info': FulfilmentInfo
        }

        self.attribute_map = {
            'expectation_id': 'expectationId',
            'expectation_verb': 'expectationVerb',
            'expectation_objects': 'expectationObjects',
            'expectation_targets': 'expectationTargets',
            'expectation_contexts': 'expectationContexts',
            'expectationfulfilment_info': 'expectationfulfilmentInfo'
        }

        self._expectation_id = expectation_id
        self._expectation_verb = expectation_verb
        self._expectation_objects = expectation_objects
        self._expectation_targets = expectation_targets
        self._expectation_contexts = expectation_contexts
        self._expectationfulfilment_info = expectationfulfilment_info

    @classmethod
    def from_dict(cls, dikt) -> 'IntentSingleAllOfIntentExpectationsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Intent_Single_allOf_intentExpectations_inner of this IntentSingleAllOfIntentExpectationsInner.  # noqa: E501
        :rtype: IntentSingleAllOfIntentExpectationsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def expectation_id(self):
        """Gets the expectation_id of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectation_id of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: str
        """
        return self._expectation_id

    @expectation_id.setter
    def expectation_id(self, expectation_id):
        """Sets the expectation_id of this IntentSingleAllOfIntentExpectationsInner.


        :param expectation_id: The expectation_id of this IntentSingleAllOfIntentExpectationsInner.
        :type expectation_id: str
        """

        self._expectation_id = expectation_id

    @property
    def expectation_verb(self):
        """Gets the expectation_verb of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectation_verb of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: ExpectationVerb
        """
        return self._expectation_verb

    @expectation_verb.setter
    def expectation_verb(self, expectation_verb):
        """Sets the expectation_verb of this IntentSingleAllOfIntentExpectationsInner.


        :param expectation_verb: The expectation_verb of this IntentSingleAllOfIntentExpectationsInner.
        :type expectation_verb: ExpectationVerb
        """

        self._expectation_verb = expectation_verb

    @property
    def expectation_objects(self):
        """Gets the expectation_objects of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectation_objects of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: List[ServiceSupportExpectationObject]
        """
        return self._expectation_objects

    @expectation_objects.setter
    def expectation_objects(self, expectation_objects):
        """Sets the expectation_objects of this IntentSingleAllOfIntentExpectationsInner.


        :param expectation_objects: The expectation_objects of this IntentSingleAllOfIntentExpectationsInner.
        :type expectation_objects: List[ServiceSupportExpectationObject]
        """

        self._expectation_objects = expectation_objects

    @property
    def expectation_targets(self):
        """Gets the expectation_targets of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectation_targets of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: List[ServiceSupportExpectationExpectationTargetsInner]
        """
        return self._expectation_targets

    @expectation_targets.setter
    def expectation_targets(self, expectation_targets):
        """Sets the expectation_targets of this IntentSingleAllOfIntentExpectationsInner.


        :param expectation_targets: The expectation_targets of this IntentSingleAllOfIntentExpectationsInner.
        :type expectation_targets: List[ServiceSupportExpectationExpectationTargetsInner]
        """

        self._expectation_targets = expectation_targets

    @property
    def expectation_contexts(self):
        """Gets the expectation_contexts of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectation_contexts of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: List[ServiceSupportExpectationExpectationContextsInner]
        """
        return self._expectation_contexts

    @expectation_contexts.setter
    def expectation_contexts(self, expectation_contexts):
        """Sets the expectation_contexts of this IntentSingleAllOfIntentExpectationsInner.


        :param expectation_contexts: The expectation_contexts of this IntentSingleAllOfIntentExpectationsInner.
        :type expectation_contexts: List[ServiceSupportExpectationExpectationContextsInner]
        """

        self._expectation_contexts = expectation_contexts

    @property
    def expectationfulfilment_info(self):
        """Gets the expectationfulfilment_info of this IntentSingleAllOfIntentExpectationsInner.


        :return: The expectationfulfilment_info of this IntentSingleAllOfIntentExpectationsInner.
        :rtype: FulfilmentInfo
        """
        return self._expectationfulfilment_info

    @expectationfulfilment_info.setter
    def expectationfulfilment_info(self, expectationfulfilment_info):
        """Sets the expectationfulfilment_info of this IntentSingleAllOfIntentExpectationsInner.


        :param expectationfulfilment_info: The expectationfulfilment_info of this IntentSingleAllOfIntentExpectationsInner.
        :type expectationfulfilment_info: FulfilmentInfo
        """

        self._expectationfulfilment_info = expectationfulfilment_info
