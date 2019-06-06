# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FetchBlacklistSuccess(object):
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
        'phone_numbers': 'list[str]'
    }

    attribute_map = {
        'phone_numbers': 'phoneNumbers'
    }

    def __init__(self, phone_numbers=None):  # noqa: E501
        """FetchBlacklistSuccess - a model defined in OpenAPI"""  # noqa: E501

        self._phone_numbers = None
        self.discriminator = None

        if phone_numbers is not None:
            self.phone_numbers = phone_numbers

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this FetchBlacklistSuccess.  # noqa: E501

        Array of unique phone numbers  # noqa: E501

        :return: The phone_numbers of this FetchBlacklistSuccess.  # noqa: E501
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this FetchBlacklistSuccess.

        Array of unique phone numbers  # noqa: E501

        :param phone_numbers: The phone_numbers of this FetchBlacklistSuccess.  # noqa: E501
        :type: list[str]
        """

        self._phone_numbers = phone_numbers

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
        if not isinstance(other, FetchBlacklistSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
