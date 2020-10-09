# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from messente_api.configuration import Configuration


class StatisticsReport(object):
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
        'total_messages': 'int',
        'total_price': 'str',
        'country': 'str'
    }

    attribute_map = {
        'total_messages': 'total_messages',
        'total_price': 'total_price',
        'country': 'country'
    }

    def __init__(self, total_messages=None, total_price=None, country=None, local_vars_configuration=None):  # noqa: E501
        """StatisticsReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_messages = None
        self._total_price = None
        self._country = None
        self.discriminator = None

        self.total_messages = total_messages
        self.total_price = total_price
        self.country = country

    @property
    def total_messages(self):
        """Gets the total_messages of this StatisticsReport.  # noqa: E501

        Sum of all messages  # noqa: E501

        :return: The total_messages of this StatisticsReport.  # noqa: E501
        :rtype: int
        """
        return self._total_messages

    @total_messages.setter
    def total_messages(self, total_messages):
        """Sets the total_messages of this StatisticsReport.

        Sum of all messages  # noqa: E501

        :param total_messages: The total_messages of this StatisticsReport.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_messages is None:  # noqa: E501
            raise ValueError("Invalid value for `total_messages`, must not be `None`")  # noqa: E501

        self._total_messages = total_messages

    @property
    def total_price(self):
        """Gets the total_price of this StatisticsReport.  # noqa: E501

        Price for all messages  # noqa: E501

        :return: The total_price of this StatisticsReport.  # noqa: E501
        :rtype: str
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this StatisticsReport.

        Price for all messages  # noqa: E501

        :param total_price: The total_price of this StatisticsReport.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and total_price is None:  # noqa: E501
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501

        self._total_price = total_price

    @property
    def country(self):
        """Gets the country of this StatisticsReport.  # noqa: E501

        Target country of all messages  # noqa: E501

        :return: The country of this StatisticsReport.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this StatisticsReport.

        Target country of all messages  # noqa: E501

        :param country: The country of this StatisticsReport.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, StatisticsReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticsReport):
            return True

        return self.to_dict() != other.to_dict()
