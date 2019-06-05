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


class DeliveryReportResponse(object):
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
        'statuses': 'list[DeliveryResult]',
        'to': 'str',
        'omnimessage_id': 'str'
    }

    attribute_map = {
        'statuses': 'statuses',
        'to': 'to',
        'omnimessage_id': 'omnimessage_id'
    }

    def __init__(self, statuses=None, to=None, omnimessage_id=None):  # noqa: E501
        """DeliveryReportResponse - a model defined in OpenAPI"""  # noqa: E501

        self._statuses = None
        self._to = None
        self._omnimessage_id = None
        self.discriminator = None

        self.statuses = statuses
        self.to = to
        self.omnimessage_id = omnimessage_id

    @property
    def statuses(self):
        """Gets the statuses of this DeliveryReportResponse.  # noqa: E501

        Contains the delivery reports for each channel, ordered by send order  # noqa: E501

        :return: The statuses of this DeliveryReportResponse.  # noqa: E501
        :rtype: list[DeliveryResult]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this DeliveryReportResponse.

        Contains the delivery reports for each channel, ordered by send order  # noqa: E501

        :param statuses: The statuses of this DeliveryReportResponse.  # noqa: E501
        :type: list[DeliveryResult]
        """
        if statuses is None:
            raise ValueError("Invalid value for `statuses`, must not be `None`")  # noqa: E501

        self._statuses = statuses

    @property
    def to(self):
        """Gets the to of this DeliveryReportResponse.  # noqa: E501

        Phone number in e.164 format  # noqa: E501

        :return: The to of this DeliveryReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DeliveryReportResponse.

        Phone number in e.164 format  # noqa: E501

        :param to: The to of this DeliveryReportResponse.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def omnimessage_id(self):
        """Gets the omnimessage_id of this DeliveryReportResponse.  # noqa: E501

        Unique identifier for the omnimessage  # noqa: E501

        :return: The omnimessage_id of this DeliveryReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._omnimessage_id

    @omnimessage_id.setter
    def omnimessage_id(self, omnimessage_id):
        """Sets the omnimessage_id of this DeliveryReportResponse.

        Unique identifier for the omnimessage  # noqa: E501

        :param omnimessage_id: The omnimessage_id of this DeliveryReportResponse.  # noqa: E501
        :type: str
        """
        if omnimessage_id is None:
            raise ValueError("Invalid value for `omnimessage_id`, must not be `None`")  # noqa: E501

        self._omnimessage_id = omnimessage_id

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
        if not isinstance(other, DeliveryReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
