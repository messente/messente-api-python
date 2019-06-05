# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Omnimessage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'to': 'str',
        'messages': 'list[OneOfViberSMSWhatsApp]',
        'dlr_url': 'str',
        'text_store': 'TextStore',
        'time_to_send': 'datetime'
    }

    attribute_map = {
        'to': 'to',
        'messages': 'messages',
        'dlr_url': 'dlr_url',
        'text_store': 'text_store',
        'time_to_send': 'time_to_send'
    }

    def __init__(self, to=None, messages=None, dlr_url=None, text_store=None, time_to_send=None):  # noqa: E501
        """Omnimessage - a model defined in OpenAPI"""  # noqa: E501

        self._to = None
        self._messages = None
        self._dlr_url = None
        self._text_store = None
        self._time_to_send = None
        self.discriminator = None

        self.to = to
        self.messages = messages
        if dlr_url is not None:
            self.dlr_url = dlr_url
        if text_store is not None:
            self.text_store = text_store
        if time_to_send is not None:
            self.time_to_send = time_to_send

    @property
    def to(self):
        """Gets the to of this Omnimessage.  # noqa: E501

        Phone number in e.164 format  # noqa: E501

        :return: The to of this Omnimessage.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Omnimessage.

        Phone number in e.164 format  # noqa: E501

        :param to: The to of this Omnimessage.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def messages(self):
        """Gets the messages of this Omnimessage.  # noqa: E501

        An array of messages  # noqa: E501

        :return: The messages of this Omnimessage.  # noqa: E501
        :rtype: list[OneOfViberSMSWhatsApp]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Omnimessage.

        An array of messages  # noqa: E501

        :param messages: The messages of this Omnimessage.  # noqa: E501
        :type: list[OneOfViberSMSWhatsApp]
        """
        if messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages

    @property
    def dlr_url(self):
        """Gets the dlr_url of this Omnimessage.  # noqa: E501

        URL where the delivery report will be sent  # noqa: E501

        :return: The dlr_url of this Omnimessage.  # noqa: E501
        :rtype: str
        """
        return self._dlr_url

    @dlr_url.setter
    def dlr_url(self, dlr_url):
        """Sets the dlr_url of this Omnimessage.

        URL where the delivery report will be sent  # noqa: E501

        :param dlr_url: The dlr_url of this Omnimessage.  # noqa: E501
        :type: str
        """

        self._dlr_url = dlr_url

    @property
    def text_store(self):
        """Gets the text_store of this Omnimessage.  # noqa: E501


        :return: The text_store of this Omnimessage.  # noqa: E501
        :rtype: TextStore
        """
        return self._text_store

    @text_store.setter
    def text_store(self, text_store):
        """Sets the text_store of this Omnimessage.


        :param text_store: The text_store of this Omnimessage.  # noqa: E501
        :type: TextStore
        """

        self._text_store = text_store

    @property
    def time_to_send(self):
        """Gets the time_to_send of this Omnimessage.  # noqa: E501

        Optional parameter for sending messages at some specific time in the future.   Time must be specified in the ISO-8601 format.   If no timezone is specified, then the timezone is assumed to be UTC    Examples:    * Time specified with timezone: 2018-06-22T09:05:07+00:00 Time specified in UTC: 2018-06-22T09:05:07Z   * Time specified without timezone: 2018-06-22T09:05 (equivalent to 2018-06-22T09:05+00:00)  # noqa: E501

        :return: The time_to_send of this Omnimessage.  # noqa: E501
        :rtype: datetime
        """
        return self._time_to_send

    @time_to_send.setter
    def time_to_send(self, time_to_send):
        """Sets the time_to_send of this Omnimessage.

        Optional parameter for sending messages at some specific time in the future.   Time must be specified in the ISO-8601 format.   If no timezone is specified, then the timezone is assumed to be UTC    Examples:    * Time specified with timezone: 2018-06-22T09:05:07+00:00 Time specified in UTC: 2018-06-22T09:05:07Z   * Time specified without timezone: 2018-06-22T09:05 (equivalent to 2018-06-22T09:05+00:00)  # noqa: E501

        :param time_to_send: The time_to_send of this Omnimessage.  # noqa: E501
        :type: datetime
        """

        self._time_to_send = time_to_send

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Omnimessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
