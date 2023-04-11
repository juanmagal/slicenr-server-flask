# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.correlated_notification import CorrelatedNotification
from openapi_server.models.notification_type import NotificationType
from openapi_server.models.source_indicator import SourceIndicator
from openapi_server import util

from openapi_server.models.correlated_notification import CorrelatedNotification  # noqa: E501
from openapi_server.models.notification_type import NotificationType  # noqa: E501
from openapi_server.models.source_indicator import SourceIndicator  # noqa: E501

class NotifyMoiDeletion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href=None, notification_id=None, notification_type=None, event_time=None, system_dn=None, correlated_notifications=None, additional_text=None, source_indicator=None, attribute_list=None):  # noqa: E501
        """NotifyMoiDeletion - a model defined in OpenAPI

        :param href: The href of this NotifyMoiDeletion.  # noqa: E501
        :type href: str
        :param notification_id: The notification_id of this NotifyMoiDeletion.  # noqa: E501
        :type notification_id: int
        :param notification_type: The notification_type of this NotifyMoiDeletion.  # noqa: E501
        :type notification_type: NotificationType
        :param event_time: The event_time of this NotifyMoiDeletion.  # noqa: E501
        :type event_time: datetime
        :param system_dn: The system_dn of this NotifyMoiDeletion.  # noqa: E501
        :type system_dn: str
        :param correlated_notifications: The correlated_notifications of this NotifyMoiDeletion.  # noqa: E501
        :type correlated_notifications: List[CorrelatedNotification]
        :param additional_text: The additional_text of this NotifyMoiDeletion.  # noqa: E501
        :type additional_text: str
        :param source_indicator: The source_indicator of this NotifyMoiDeletion.  # noqa: E501
        :type source_indicator: SourceIndicator
        :param attribute_list: The attribute_list of this NotifyMoiDeletion.  # noqa: E501
        :type attribute_list: Dict[str, object]
        """
        self.openapi_types = {
            'href': str,
            'notification_id': int,
            'notification_type': NotificationType,
            'event_time': datetime,
            'system_dn': str,
            'correlated_notifications': List[CorrelatedNotification],
            'additional_text': str,
            'source_indicator': SourceIndicator,
            'attribute_list': Dict[str, object]
        }

        self.attribute_map = {
            'href': 'href',
            'notification_id': 'notificationId',
            'notification_type': 'notificationType',
            'event_time': 'eventTime',
            'system_dn': 'systemDN',
            'correlated_notifications': 'correlatedNotifications',
            'additional_text': 'additionalText',
            'source_indicator': 'sourceIndicator',
            'attribute_list': 'attributeList'
        }

        self._href = href
        self._notification_id = notification_id
        self._notification_type = notification_type
        self._event_time = event_time
        self._system_dn = system_dn
        self._correlated_notifications = correlated_notifications
        self._additional_text = additional_text
        self._source_indicator = source_indicator
        self._attribute_list = attribute_list

    @classmethod
    def from_dict(cls, dikt) -> 'NotifyMoiDeletion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotifyMoiDeletion of this NotifyMoiDeletion.  # noqa: E501
        :rtype: NotifyMoiDeletion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self):
        """Gets the href of this NotifyMoiDeletion.


        :return: The href of this NotifyMoiDeletion.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this NotifyMoiDeletion.


        :param href: The href of this NotifyMoiDeletion.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def notification_id(self):
        """Gets the notification_id of this NotifyMoiDeletion.


        :return: The notification_id of this NotifyMoiDeletion.
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotifyMoiDeletion.


        :param notification_id: The notification_id of this NotifyMoiDeletion.
        :type notification_id: int
        """
        if notification_id is None:
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def notification_type(self):
        """Gets the notification_type of this NotifyMoiDeletion.


        :return: The notification_type of this NotifyMoiDeletion.
        :rtype: NotificationType
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this NotifyMoiDeletion.


        :param notification_type: The notification_type of this NotifyMoiDeletion.
        :type notification_type: NotificationType
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def event_time(self):
        """Gets the event_time of this NotifyMoiDeletion.


        :return: The event_time of this NotifyMoiDeletion.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this NotifyMoiDeletion.


        :param event_time: The event_time of this NotifyMoiDeletion.
        :type event_time: datetime
        """
        if event_time is None:
            raise ValueError("Invalid value for `event_time`, must not be `None`")  # noqa: E501

        self._event_time = event_time

    @property
    def system_dn(self):
        """Gets the system_dn of this NotifyMoiDeletion.


        :return: The system_dn of this NotifyMoiDeletion.
        :rtype: str
        """
        return self._system_dn

    @system_dn.setter
    def system_dn(self, system_dn):
        """Sets the system_dn of this NotifyMoiDeletion.


        :param system_dn: The system_dn of this NotifyMoiDeletion.
        :type system_dn: str
        """
        if system_dn is None:
            raise ValueError("Invalid value for `system_dn`, must not be `None`")  # noqa: E501

        self._system_dn = system_dn

    @property
    def correlated_notifications(self):
        """Gets the correlated_notifications of this NotifyMoiDeletion.


        :return: The correlated_notifications of this NotifyMoiDeletion.
        :rtype: List[CorrelatedNotification]
        """
        return self._correlated_notifications

    @correlated_notifications.setter
    def correlated_notifications(self, correlated_notifications):
        """Sets the correlated_notifications of this NotifyMoiDeletion.


        :param correlated_notifications: The correlated_notifications of this NotifyMoiDeletion.
        :type correlated_notifications: List[CorrelatedNotification]
        """

        self._correlated_notifications = correlated_notifications

    @property
    def additional_text(self):
        """Gets the additional_text of this NotifyMoiDeletion.


        :return: The additional_text of this NotifyMoiDeletion.
        :rtype: str
        """
        return self._additional_text

    @additional_text.setter
    def additional_text(self, additional_text):
        """Sets the additional_text of this NotifyMoiDeletion.


        :param additional_text: The additional_text of this NotifyMoiDeletion.
        :type additional_text: str
        """

        self._additional_text = additional_text

    @property
    def source_indicator(self):
        """Gets the source_indicator of this NotifyMoiDeletion.


        :return: The source_indicator of this NotifyMoiDeletion.
        :rtype: SourceIndicator
        """
        return self._source_indicator

    @source_indicator.setter
    def source_indicator(self, source_indicator):
        """Sets the source_indicator of this NotifyMoiDeletion.


        :param source_indicator: The source_indicator of this NotifyMoiDeletion.
        :type source_indicator: SourceIndicator
        """

        self._source_indicator = source_indicator

    @property
    def attribute_list(self):
        """Gets the attribute_list of this NotifyMoiDeletion.

        The key of this map is the attribute name, and the value the attribute value.  # noqa: E501

        :return: The attribute_list of this NotifyMoiDeletion.
        :rtype: Dict[str, object]
        """
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, attribute_list):
        """Sets the attribute_list of this NotifyMoiDeletion.

        The key of this map is the attribute name, and the value the attribute value.  # noqa: E501

        :param attribute_list: The attribute_list of this NotifyMoiDeletion.
        :type attribute_list: Dict[str, object]
        """
        if attribute_list is not None and len(attribute_list) < 1:
            raise ValueError("Invalid value for `attribute_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._attribute_list = attribute_list